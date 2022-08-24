#!/usr/bin/env python3

from pathlib import Path
import re
import logging

logger = logging.getLogger('parser')


class Node:
    def __init__(self, ref, pin, pinfunction, pintype):
        self.ref = ref
        self.pin = pin
        self.pinfunction = pinfunction
        self.pintype = pintype

    @property
    def no_connect(self) -> bool:
        if self.pintype == "free" or "no_connect" in self.pintype:
            return True
        return False

    def __repr__(self):
        return f"{self.ref}.{self.pin}"

class Net:
    def __init__(self, code, name):
        self.code = code
        self.name = name
        self.nodes = []

class Netlist:
    re_nets = re.compile(r"\s+\(nets\s*$")

    re_net = re.compile(r"""\s+
                            \(net\s
                                \(code\s\"(\d+)\"\)\s
                                \(name\s\"(.+?)\"\)
                            """, re.X)

    re_net_node = re.compile(r"""\s+
                                 \(node\s
                                    \(ref\s\"(.+?)\"\)\s
                                    \(pin\s\"(.+?)\"\)\s
                                    (?:\(pinfunction\s\"(.+?)\"\)\s)?
                                    \(pintype\s\"(.+?)\"\)
                                 \)
                                 """, re.X)

    def __init__(self, path):
        self.nets = []
        self.net = None
        self.indent = 0
        with path.open() as f:
            line = f.readline()
            state = 'start'
            while line:
                line = line.rstrip()
                logger.debug(f"state={state}")
                if state == 'start':
                    if self.re_nets.match(line):
                        state = 'nets'
                elif state == 'nets':
                    logger.debug(f"line={line}")
                    if match := self.re_net.match(line):
                        logger.debug(f"matched net")
                        if self.net is not None:
                            self.nets.append(self.net)
                        self.net = Net(*match.groups())
                    elif match := self.re_net_node.match(line):
                        logger.debug(f"matched node")
                        logger.debug(match.groups())
                        self.net.nodes.append(Node(*match.groups()))
                    else:
                        logger.debug(f"unrecognised line: {line}")
                        exit(1)
                line = f.readline()





if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="debug printing")
    args = parser.parse_args()

    level = logging.INFO
    if args.verbose:
        level = logging.DEBUG
    logging.basicConfig(format="%(levelname)s: %(message)s", level=level)


    n = Netlist(Path("orbtrace-fmc-breakout.net"))
    for net in n.nets:
        if len(net.nodes) < 2:
            node = net.nodes[0]
            if not node.no_connect:
                logger.warning(f"net {net.name} has only 1 node: {node}")
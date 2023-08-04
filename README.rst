###########################
Orbtrace FMC Breakout Board
###########################

This FMC based breakout board is designed to interface an
`ORBTrace mini <https://orbcode.org/orbtrace-mini/>`_ to an Avnet
`Mini-ITX <https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/mini-itx/>`_
Zynq-7000 development board.

The board utilises the `Hirose DF40 <https://www.hirose.com/product/series/DF40>`_
series of board-to-board connectors.  This range is available in differing pin counts
and different stack heights.  However, many of the heights were unobtanium when putting
together the prototypes so your mileage may vary.  The part number used was the
`DF40C-(2.0)-70DS-0.4V <https://www.hirose.com/en/product/p/CL0684-4016-5-51>`_ which
is a 2mm mated stacking height.

****************
Revision History
****************

+--------+-------------------------------------------------------------------------------------+
| Tag    | Description                                                                         |
+========+=====================================================================================+
| 0.2.0  | Fixed orientation of FMC connector. Originally put down 180 degrees out after       |
|        | reviewing dimensions of a board that was viewed mirrored. D'oh.                     |
|        | Also added a legacy 20-pin IDC conector for JLink support and some 0.1" pin headers |
|        | for debug access when the ORBTrace is not mounted.                                  |
+--------+-------------------------------------------------------------------------------------+
| 0.1.0  | Initial commit.                                                                     |
+--------+-------------------------------------------------------------------------------------+


****************
Board Dimensions
****************

The board outline conforms to the ANSI/VITA 57.1 standard and I followed the mechanical
data section of the product pages for the
`FMCHUB LPC Breakout <https://fmchub.github.io/projects/FMC_LPC_BREAKOUT/Datasheet/FMC_LPC_BREAKOUT_datasheet.html>`_.

The mounting location of the FMC connector itself doesn't seem to be easily available
unless you pay for the specification. However, a few useful dimensions found on the net
and some scribbling on paper enabled the relative locations to the mounting holes to be
calculated.

This forum post for the
`Nexys4 DDR <https://forum.digilent.com/topic/1402-nexys4-ddr-mechanicals/?do=findComment&comment=9315>`_
shows the relative offsets.

**Note:** The ``User.Drawings`` layer of the PCB Editor has the exterior dimensions annotated.

**********
FMC Pinout
**********

The following tables show the pin assignments for each of the connectors on the board.

ORBTrace Mini
=============

The ORBTrace uses a high density 70 pin connector that is unused by default and is
available for user expansion purposes.  The use case for this breakout board is to
re-route the SWD interface from the 0.1" headers to use the high density connector.
Enough pins are available for further functionality to be implemented too.

+------+---------+-----------+---------+-----------------------------------------+
|  Pin | Signal  | Net       | FMC Pin | Function                                |
+======+=========+===========+=========+=========================================+
|  08  | LED_EXT |  N/A      | N/A     | RGB LED drive from Orbtrace; unused.    |
+------+---------+-----------+---------+-----------------------------------------+
|  09  | JTMS    | LA24_N    | H29     | FPGA JTAG lines.                        |
+------+---------+-----------+---------+-----------------------------------------+
|  11  | JTCK    | LA24_P    | H28     | FPGA JTAG lines.                        |
+------+---------+-----------+---------+-----------------------------------------+
|  13  | JTDI    | LA25_N    | G28     | FPGA JTAG lines.                        |
+------+---------+-----------+---------+-----------------------------------------+
|  15  | JTDO    | LA25_P    | G27     | FPGA JTAG lines.                        |
+------+---------+-----------+---------+-----------------------------------------+
|  14  | SDA     | LA28_N    | H32     | I2C from Orbtrace; unused.              |
+------+---------+-----------+---------+-----------------------------------------+
|  16  | SCL     | LA28_P    | H31     | I2C from Orbtrace; unused.              |
+------+---------+-----------+---------+-----------------------------------------+
|  22  | EXT_31  | LA29_P    | G30     | User IO free to use.                    |
+------+---------+-----------+---------+-----------------------------------------+
|  20  | EXT_30  | LA29_N    | G31     | User IO free to use.                    |
+------+---------+-----------+---------+-----------------------------------------+
|  28  | EXT_29  | TP2       | N/A     | User IO free to use.                    |
+------+---------+-----------+---------+-----------------------------------------+
|  26  | EXT_28  | TP1       | N/A     | User IO free to use.                    |
+------+---------+-----------+---------+-----------------------------------------+
|  25  | EXT_27  | LA22_N    | G25     | User IO free to use.                    |
+------+---------+-----------+---------+-----------------------------------------+
|  27  | EXT_26  | LA22_P    | G24     | User IO free to use.                    |
+------+---------+-----------+---------+-----------------------------------------+
|  32  | EXT_25  | TP3       | N/A     | User IO free to use.                    |
+------+---------+-----------+---------+-----------------------------------------+
|  34  | EXT_24  | TP4       | N/A     | User IO free to use.                    |
+------+---------+-----------+---------+-----------------------------------------+
|  19  | EXT_23  | LA21_N    | H26     | User IO free to use.                    |
+------+---------+-----------+---------+-----------------------------------------+
|  21  | EXT_22  | LA21_P    | H25     | User IO free to use.                    |
+------+---------+-----------+---------+-----------------------------------------+
|  31  | EXT_21  | LA19_N    | H23     | User IO free to use.                    |
+------+---------+-----------+---------+-----------------------------------------+
|  33  | EXT_20  | LA19_P    | H22     | User IO free to use.                    |
+------+---------+-----------+---------+-----------------------------------------+
|  39  | EXT_19  | LA20_P    | G21     | User IO free to use.                    |
+------+---------+-----------+---------+-----------------------------------------+
|  37  | EXT_18  | LA20_N    | G22     | User IO free to use.                    |
+------+---------+-----------+---------+-----------------------------------------+
|  38  | EXT_17  | LA07_N    | H14     | User IO free to use.                    |
+------+---------+-----------+---------+-----------------------------------------+
|  40  | EXT_16  | LA07_P    | H13     | User IO free to use.                    |
+------+---------+-----------+---------+-----------------------------------------+
|  46  | EXT_15  | LA04_P    | H10     | User IO free to use.                    |
+------+---------+-----------+---------+-----------------------------------------+
|  44  | EXT_14  | LA04_N    | H11     | User IO free to use.                    |
+------+---------+-----------+---------+-----------------------------------------+
|  43  | EXT_13  | LA15_N    | H20     | User IO free to use.                    |
+------+---------+-----------+---------+-----------------------------------------+
|  45  | EXT_12  | LA15_P    | H19     | User IO free to use.                    |
+------+---------+-----------+---------+-----------------------------------------+
|  57  | EXT_11  | LA11_P    | H16     | User IO free to use.                    |
+------+---------+-----------+---------+-----------------------------------------+
|  55  | EXT_10  | LA11_N    | H17     | User IO free to use.                    |
+------+---------+-----------+---------+-----------------------------------------+
|  50  | EXT_09  | LA03_N    | G10     | User IO free to use.                    |
+------+---------+-----------+---------+-----------------------------------------+
|  52  | EXT_08  | LA03_P    | G9      | User IO free to use.                    |
+------+---------+-----------+---------+-----------------------------------------+
|  49  | EXT_07  | LA16_N    | G19     | User IO free to use.                    |
+------+---------+-----------+---------+-----------------------------------------+
|  51  | EXT_06  | LA16_P    | G18     | User IO free to use.                    |
+------+---------+-----------+---------+-----------------------------------------+
|  58  | EXT_05  | LA00_P_CC | G6      | User IO free to use. Clock capable.     |
+------+---------+-----------+---------+-----------------------------------------+
|  56  | EXT_04  | LA00_N_CC | G7      | User IO free to use. Clock capable.     |
+------+---------+-----------+---------+-----------------------------------------+
|  61  | EXT_03  | CFG1      | N/A     | User config; driven from DIP switch.    |
+------+---------+-----------+---------+-----------------------------------------+
|  63  | EXT_02  | CFG2      | N/A     | User config; driven from DIP switch.    |
+------+---------+-----------+---------+-----------------------------------------+
|  64  | EXT_01  | PB2       | N/A     | User push button.                       |
+------+---------+-----------+---------+-----------------------------------------+
|  62  | EXT_00  | PB4       | N/A     | User push button.                       |
+------+---------+-----------+---------+-----------------------------------------+


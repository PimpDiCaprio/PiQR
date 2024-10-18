import numpy as np
from Conversions import *

class DataAnalysis():
    def __init__(self):
        self.ecc_list = [
            # Version and EC Level,
            # Total Number of Data Codewords for this Version and EC Level,
            # EC Codewords Per Block,
            # Number of Blocks in Group 1,
            # Number of Data Codewords in Each of Group 1's Blocks,
            # Number of Blocks in Group 2,
            # Number of Data Codewords in Each of Group 2's Blocks,
            # Total Data Codewords
            ('1-L', 19, 7, 1, 19, '', '', '(19*1) = 19'),
            ('1-M', 16, 10, 1, 16, '', '', '(16*1) = 16'),
            ('1-Q', 13, 13, 1, 13, '', '', '(13*1) = 13'),
            ('1-H', 9, 17, 1, 9, '', '', '(9*1) = 9'),
            ('2-L', 34, 10, 1, 34, '', '', '(34*1) = 34'),
            ('2-M', 28, 16, 1, 28, '', '', '(28*1) = 28'),
            ('2-Q', 22, 22, 1, 22, '', '', '(22*1) = 22'),
            ('2-H', 16, 28, 1, 16, '', '', '(16*1) = 16'),
            ('3-L', 55, 15, 1, 55, '', '', '(55*1) = 55'),
            ('3-M', 44, 26, 1, 44, '', '', '(44*1) = 44'),
            ('3-Q', 34, 18, 2, 17, '', '', '(17*2) = 34'),
            ('3-H', 26, 22, 2, 13, '', '', '(13*2) = 26'),
            ('4-L', 80, 20, 1, 80, '', '', '(80*1) = 80'),
            ('4-M', 64, 18, 2, 32, '', '', '(32*2) = 64'),
            ('4-Q', 48, 26, 2, 24, '', '', '(24*2) = 48'),
            ('4-H', 36, 16, 4, 9, '', '', '(9*4) = 36'),
            ('5-L', 108, 26, 1, 108, '', '', '(108*1) = 108'),
            ('5-M', 86, 24, 2, 43, '', '', '(43*2) = 86'),
            ('5-Q', 62, 18, 2, 15, 2, 16, '(15*2) + (16*2) = 62'),
            ('5-H', 46, 22, 2, 11, 2, 12, '(11*2) + (12*2) = 46'),
            ('6-L', 136, 18, 2, 68, '', '', '(68*2) = 136'),
            ('6-M', 108, 16, 4, 27, '', '', '(27*4) = 108'),
            ('6-Q', 76, 24, 4, 19, '', '', '(19*4) = 76'),
            ('6-H', 60, 28, 4, 15, '', '', '(15*4) = 60'),
            ('7-L', 156, 20, 2, 78, '', '', '(78*2) = 156'),
            ('7-M', 124, 18, 4, 31, '', '', '(31*4) = 124'),
            ('7-Q', 88, 18, 2, 14, 4, 15, '(14*2) + (15*4) = 88'),
            ('7-H', 66, 26, 4, 13, 1, 14, '(13*4) + (14*1) = 66'),
            ('8-L', 194, 24, 2, 97, '', '', '(97*2) = 194'),
            ('8-M', 154, 22, 2, 38, 2, 39, '(38*2) + (39*2) = 154'),
            ('8-Q', 110, 22, 4, 18, 2, 19, '(18*4) + (19*2) = 110'),
            ('8-H', 86, 26, 4, 14, 2, 15, '(14*4) + (15*2) = 86'),
            ('9-L', 232, 30, 2, 116, '', '', '(116*2) = 232'),
            ('9-M', 182, 22, 3, 36, 2, 37, '(36*3) + (37*2) = 182'),
            ('9-Q', 132, 20, 4, 16, 4, 17, '(16*4) + (17*4) = 132'),
            ('9-H', 100, 24, 4, 12, 4, 13, '(12*4) + (13*4) = 100'),
            ('10-L', 274, 18, 2, 68, 2, 69, '(68*2) + (69*2) = 274'),
            ('10-M', 216, 26, 4, 43, 1, 44, '(43*4) + (44*1) = 216'),
            ('10-Q', 154, 24, 6, 19, 2, 20, '(19*6) + (20*2) = 154'),
            ('10-H', 122, 28, 6, 15, 2, 16, '(15*6) + (16*2) = 122'),
            ('11-L', 324, 20, 4, 81, '', '', '(81*4) = 324'),
            ('11-M', 254, 30, 1, 50, 4, 51, '(50*1) + (51*4) = 254'),
            ('11-Q', 180, 28, 4, 22, 4, 23, '(22*4) + (23*4) = 180'),
            ('11-H', 140, 24, 3, 12, 8, 13, '(12*3) + (13*8) = 140'),
            ('12-L', 370, 24, 2, 92, 2, 93, '(92*2) + (93*2) = 370'),
            ('12-M', 290, 22, 6, 36, 2, 37, '(36*6) + (37*2) = 290'),
            ('12-Q', 206, 26, 4, 20, 6, 21, '(20*4) + (21*6) = 206'),
            ('12-H', 158, 28, 7, 14, 4, 15, '(14*7) + (15*4) = 158'),
            ('13-L', 428, 26, 4, 107, '', '', '(107*4) = 428'),
            ('13-M', 334, 22, 8, 37, 1, 38, '(37*8) + (38*1) = 334'),
            ('13-Q', 244, 24, 8, 20, 4, 21, '(20*8) + (21*4) = 244'),
            ('13-H', 180, 22, 12, 11, 4, 12, '(11*12) + (12*4) = 180'),
            ('14-L', 461, 30, 3, 115, 1, 116, '(115*3) + (116*1) = 461'),
            ('14-M', 365, 24, 4, 40, 5, 41, '(40*4) + (41*5) = 365'),
            ('14-Q', 261, 20, 11, 16, 5, 17, '(16*11) + (17*5) = 261'),
            ('14-H', 197, 24, 11, 12, 5, 13, '(12*11) + (13*5) = 197'),
            ('15-L', 523, 22, 5, 87, 1, 88, '(87*5) + (88*1) = 523'),
            ('15-M', 415, 24, 5, 41, 5, 42, '(41*5) + (42*5) = 415'),
            ('15-Q', 295, 30, 5, 24, 7, 25, '(24*5) + (25*7) = 295'),
            ('15-H', 223, 24, 11, 12, 7, 13, '(12*11) + (13*7) = 223'),
            ('16-L', 589, 24, 5, 98, 1, 99, '(98*5) + (99*1) = 589'),
            ('16-M', 453, 28, 7, 45, 3, 46, '(45*7) + (46*3) = 453'),
            ('16-Q', 325, 24, 15, 19, 2, 20, '(19*15) + (20*2) = 325'),
            ('16-H', 253, 30, 3, 15, 13, 16, '(15*3) + (16*13) = 253'),
            ('17-L', 647, 28, 1, 107, 5, 108, '(107*1) + (108*5) = 647'),
            ('17-M', 507, 28, 10, 46, 1, 47, '(46*10) + (47*1) = 507'),
            ('17-Q', 367, 28, 1, 22, 15, 23, '(22*1) + (23*15) = 367'),
            ('17-H', 283, 28, 2, 14, 17, 15, '(14*2) + (15*17) = 283'),
            ('18-L', 721, 30, 5, 120, 1, 121, '(120*5) + (121*1) = 721'),
            ('18-M', 563, 26, 9, 43, 4, 44, '(43*9) + (44*4) = 563'),
            ('18-Q', 397, 28, 17, 22, 1, 23, '(22*17) + (23*1) = 397'),
            ('18-H', 313, 28, 2, 14, 19, 15, '(14*2) + (15*19) = 313'),
            ('19-L', 795, 28, 3, 113, 4, 114, '(113*3) + (114*4) = 795'),
            ('19-M', 627, 26, 3, 44, 11, 45, '(44*3) + (45*11) = 627'),
            ('19-Q', 445, 26, 17, 21, 4, 22, '(21*17) + (22*4) = 445'),
            ('19-H', 341, 26, 9, 13, 16, 14, '(13*9) + (14*16) = 341'),
            ('20-L', 861, 28, 3, 107, 5, 108, '(107*3) + (108*5) = 861'),
            ('20-M', 669, 26, 3, 41, 13, 42, '(41*3) + (42*13) = 669'),
            ('20-Q', 485, 30, 15, 24, 5, 25, '(24*15) + (25*5) = 485'),
            ('20-H', 385, 28, 15, 15, 10, 16, '(15*15) + (16*10) = 385'),
            ('21-L', 932, 28, 4, 116, 4, 117, '(116*4) + (117*4) = 932'),
            ('21-M', 714, 26, 17, 42, '', '', '(42*17) = 714'),
            ('21-Q', 512, 28, 17, 22, 6, 23, '(22*17) + (23*6) = 512'),
            ('21-H', 406, 30, 19, 16, 6, 17, '(16*19) + (17*6) = 406'),
            ('22-L', 1006, 28, 2, 111, 7, 112, '(111*2) + (112*7) = 1006'),
            ('22-M', 782, 28, 17, 46, '', '', '(46*17) = 782'),
            ('22-Q', 568, 30, 7, 24, 16, 25, '(24*7) + (25*16) = 568'),
            ('22-H', 442, 24, 34, 13, '', '', '(13*34) = 442'),
            ('23-L', 1094, 30, 4, 121, 5, 122, '(121*4) + (122*5) = 1094'),
            ('23-M', 860, 28, 4, 47, 14, 48, '(47*4) + (48*14) = 860'),
            ('23-Q', 614, 30, 11, 24, 14, 25, '(24*11) + (25*14) = 614'),
            ('23-H', 464, 30, 16, 15, 14, 16, '(15*16) + (16*14) = 464'),
            ('24-L', 1174, 30, 6, 117, 4, 118, '(117*6) + (118*4) = 1174'),
            ('24-M', 914, 28, 6, 45, 14, 46, '(45*6) + (46*14) = 914'),
            ('24-Q', 664, 30, 11, 24, 16, 25, '(24*11) + (25*16) = 664'),
            ('24-H', 514, 30, 30, 16, 2, 17, '(16*30) + (17*2) = 514'),
            ('25-L', 1276, 26, 8, 106, 4, 107, '(106*8) + (107*4) = 1276'),
            ('25-M', 1000, 28, 8, 47, 13, 48, '(47*8) + (48*13) = 1000'),
            ('25-Q', 718, 30, 7, 24, 22, 25, '(24*7) + (25*22) = 718'),
            ('25-H', 538, 30, 22, 15, 13, 16, '(15*22) + (16*13) = 538'),
            ('26-L', 1370, 28, 10, 114, 2, 115, '(114*10) + (115*2) = 1370'),
            ('26-M', 1062, 28, 19, 46, 4, 47, '(46*19) + (47*4) = 1062'),
            ('26-Q', 754, 28, 28, 22, 6, 23, '(22*28) + (23*6) = 754'),
            ('26-H', 596, 30, 33, 16, 4, 17, '(16*33) + (17*4) = 596'),
            ('27-L', 1468, 30, 8, 122, 4, 123, '(122*8) + (123*4) = 1468'),
            ('27-M', 1128, 28, 22, 45, 3, 46, '(45*22) + (46*3) = 1128'),
            ('27-Q', 808, 30, 8, 23, 26, 24, '(23*8) + (24*26) = 808'),
            ('27-H', 628, 30, 12, 15, 28, 16, '(15*12) + (16*28) = 628'),
            ('28-L', 1531, 30, 3, 117, 10, 118, '(117*3) + (118*10) = 1531'),
            ('28-M', 1193, 28, 3, 45, 23, 46, '(45*3) + (46*23) = 1193'),
            ('28-Q', 871, 30, 4, 24, 31, 25, '(24*4) + (25*31) = 871'),
            ('28-H', 661, 30, 11, 15, 31, 16, '(15*11) + (16*31) = 661'),
            ('29-L', 1631, 30, 7, 116, 7, 117, '(116*7) + (117*7) = 1631'),
            ('29-M', 1267, 28, 21, 45, 7, 46, '(45*21) + (46*7) = 1267'),
            ('29-Q', 911, 30, 1, 23, 37, 24, '(23*1) + (24*37) = 911'),
            ('29-H', 701, 30, 19, 15, 26, 16, '(15*19) + (16*26) = 701'),
            ('30-L', 1735, 30, 5, 115, 10, 116, '(115*5) + (116*10) = 1735'),
            ('30-M', 1373, 28, 19, 47, 10, 48, '(47*19) + (48*10) = 1373'),
            ('30-Q', 985, 30, 15, 24, 25, 25, '(24*15) + (25*25) = 985'),
            ('30-H', 745, 30, 23, 15, 25, 16, '(15*23) + (16*25) = 745'),
            ('31-L', 1843, 30, 13, 115, 3, 116, '(115*13) + (116*3) = 1843'),
            ('31-M', 1455, 28, 2, 46, 29, 47, '(46*2) + (47*29) = 1455'),
            ('31-Q', 1033, 30, 42, 24, 1, 25, '(24*42) + (25*1) = 1033'),
            ('31-H', 793, 30, 23, 15, 28, 16, '(15*23) + (16*28) = 793'),
            ('32-L', 1955, 30, 17, 115, '', '', '(115*17) = 1955'),
            ('32-M', 1541, 28, 10, 46, 23, 47, '(46*10) + (47*23) = 1541'),
            ('32-Q', 1115, 30, 10, 24, 35, 25, '(24*10) + (25*35) = 1115'),
            ('32-H', 845, 30, 19, 15, 35, 16, '(15*19) + (16*35) = 845'),
            ('33-L', 2071, 30, 17, 115, 1, 116, '(115*17) + (116*1) = 2071'),
            ('33-M', 1631, 28, 14, 46, 21, 47, '(46*14) + (47*21) = 1631'),
            ('33-Q', 1171, 30, 29, 24, 19, 25, '(24*29) + (25*19) = 1171'),
            ('33-H', 901, 30, 11, 15, 46, 16, '(15*11) + (16*46) = 901'),
            ('34-L', 2191, 30, 13, 115, 6, 116, '(115*13) + (116*6) = 2191'),
            ('34-M', 1725, 28, 14, 46, 23, 47, '(46*14) + (47*23) = 1725'),
            ('34-Q', 1231, 30, 44, 24, 7, 25, '(24*44) + (25*7) = 1231'),
            ('34-H', 961, 30, 59, 16, 1, 17, '(16*59) + (17*1) = 961'),
            ('35-L', 2306, 30, 12, 121, 7, 122, '(121*12) + (122*7) = 2306'),
            ('35-M', 1812, 28, 12, 47, 26, 48, '(47*12) + (48*26) = 1812'),
            ('35-Q', 1286, 30, 39, 24, 14, 25, '(24*39) + (25*14) = 1286'),
            ('35-H', 986, 30, 22, 15, 41, 16, '(15*22) + (16*41) = 986'),
            ('36-L', 2434, 30, 6, 121, 14, 122, '(121*6) + (122*14) = 2434'),
            ('36-M', 1914, 28, 6, 47, 34, 48, '(47*6) + (48*34) = 1914'),
            ('36-Q', 1354, 30, 46, 24, 10, 25, '(24*46) + (25*10) = 1354'),
            ('36-H', 1054, 30, 2, 15, 64, 16, '(15*2) + (16*64) = 1054'),
            ('37-L', 2566, 30, 17, 122, 4, 123, '(122*17) + (123*4) = 2566'),
            ('37-M', 1992, 28, 29, 46, 14, 47, '(46*29) + (47*14) = 1992'),
            ('37-Q', 1426, 30, 49, 24, 10, 25, '(24*49) + (25*10) = 1426'),
            ('37-H', 1096, 30, 24, 15, 46, 16, '(15*24) + (16*46) = 1096'),
            ('38-L', 2702, 30, 4, 122, 18, 123, '(122*4) + (123*18) = 2702'),
            ('38-M', 2102, 28, 13, 46, 32, 47, '(46*13) + (47*32) = 2102'),
            ('38-Q', 1502, 30, 48, 24, 14, 25, '(24*48) + (25*14) = 1502'),
            ('38-H', 1142, 30, 42, 15, 32, 16, '(15*42) + (16*32) = 1142'),
            ('39-L', 2812, 30, 20, 117, 4, 118, '(117*20) + (118*4) = 2812'),
            ('39-M', 2216, 28, 40, 47, 7, 48, '(47*40) + (48*7) = 2216'),
            ('39-Q', 1582, 30, 43, 24, 22, 25, '(24*43) + (25*22) = 1582'),
            ('39-H', 1222, 30, 10, 15, 67, 16, '(15*10) + (16*67) = 1222'),
            ('40-L', 2956, 30, 19, 118, 6, 119, '(118*19) + (119*6) = 2956'),
            ('40-M', 2334, 28, 18, 47, 31, 48, '(47*18) + (48*31) = 2334'),
            ('40-Q', 1666, 30, 34, 24, 34, 25, '(24*34) + (25*34) = 1666'),
            ('40-H', 1276, 30, 20, 15, 61, 16, '(15*20) + (16*61) = 1276')
        ]
        self.character_capacities = {
            'Low': {
                'Value_Data': [
                    (1, 41, 25, 17, 10),
                    (2, 77, 47, 32, 20),
                    (3, 127, 77, 53, 32),
                    (4, 187, 114, 78, 48),
                    (5, 255, 154, 106, 65),
                    (6, 322, 195, 134, 82),
                    (7, 370, 224, 154, 95),
                    (8, 461, 279, 192, 118),
                    (9, 552, 335, 230, 141),
                    (10, 652, 395, 271, 167),
                    (11, 772, 468, 321, 198),
                    (12, 883, 535, 367, 226),
                    (13, 1022, 619, 425, 262),
                    (14, 1101, 667, 458, 282),
                    (15, 1250, 758, 520, 320),
                    (16, 1408, 854, 586, 361),
                    (17, 1548, 938, 644, 397),
                    (18, 1725, 1046, 718, 442),
                    (19, 1903, 1153, 792, 488),
                    (20, 2061, 1249, 858, 528),
                    (21, 2232, 1352, 929, 572),
                    (22, 2409, 1460, 1003, 618),
                    (23, 2620, 1588, 1091, 672),
                    (24, 2812, 1704, 1171, 721),
                    (25, 3057, 1853, 1273, 784),
                    (26, 3283, 1990, 1367, 842),
                    (27, 3517, 2132, 1465, 902),
                    (28, 3669, 2223, 1528, 940),
                    (29, 3909, 2369, 1628, 1002),
                    (30, 4158, 2520, 1732, 1066),
                    (31, 4417, 2677, 1840, 1132),
                    (32, 4686, 2840, 1952, 1201),
                    (33, 4965, 3009, 2068, 1273),
                    (34, 5253, 3183, 2188, 1347),
                    (35, 5529, 3351, 2303, 1417),
                    (36, 5836, 3537, 2431, 1496),
                    (37, 6153, 3729, 2563, 1577),
                    (38, 6479, 3927, 2699, 1661),
                    (39, 6743, 4087, 2809, 1729),
                    (40, 7089, 4296, 2953, 1817),
                ]
            },
            'Medium': {
                'Value_Data': [
                    (1, 34, 20, 14, 8),
                    (2, 63, 38, 26, 16),
                    (3, 101, 61, 42, 26),
                    (4, 149, 90, 62, 38),
                    (5, 202, 122, 84, 52),
                    (6, 255, 154, 106, 65),
                    (7, 293, 178, 122, 75),
                    (8, 365, 221, 152, 93),
                    (9, 432, 262, 180, 111),
                    (10, 513, 311, 213, 131),
                    (11, 604, 366, 251, 155),
                    (12, 691, 419, 287, 177),
                    (13, 796, 483, 331, 204),
                    (14, 871, 528, 362, 223),
                    (15, 991, 600, 412, 254),
                    (16, 1082, 656, 450, 277),
                    (17, 1212, 734, 504, 310),
                    (18, 1346, 816, 560, 345),
                    (19, 1500, 909, 624, 384),
                    (20, 1600, 970, 666, 410),
                    (21, 1708, 1035, 711, 438),
                    (22, 1872, 1134, 779, 480),
                    (23, 2059, 1248, 857, 528),
                    (24, 2188, 1326, 911, 561),
                    (25, 2395, 1451, 997, 614),
                    (26, 2544, 1542, 1059, 652),
                    (27, 2701, 1637, 1125, 692),
                    (28, 2857, 1732, 1190, 732),
                    (29, 3035, 1839, 1264, 778),
                    (30, 3289, 1994, 1370, 843),
                    (31, 3486, 2113, 1452, 894),
                    (32, 3693, 2238, 1538, 947),
                    (33, 3909, 2369, 1628, 1002),
                    (34, 4134, 2506, 1722, 1060),
                    (35, 4343, 2632, 1809, 1113),
                    (36, 4588, 2780, 1911, 1176),
                    (37, 4775, 2894, 1989, 1224),
                    (38, 5039, 3054, 2099, 1292),
                    (39, 5313, 3220, 2213, 1362),
                    (40, 5596, 3391, 2331, 1435),
                ]
            },
            'Quartile': {
                'Value_Data': [
                    (1, 27, 16, 11, 7),
                    (2, 48, 29, 20, 12),
                    (3, 77, 47, 32, 20),
                    (4, 111, 67, 46, 28),
                    (5, 144, 87, 60, 37),
                    (6, 178, 108, 74, 45),
                    (7, 207, 125, 86, 53),
                    (8, 259, 157, 108, 66),
                    (9, 312, 189, 130, 80),
                    (10, 364, 221, 151, 93),
                    (11, 427, 259, 177, 109),
                    (12, 489, 296, 203, 125),
                    (13, 580, 352, 241, 149),
                    (14, 621, 376, 258, 159),
                    (15, 703, 426, 292, 180),
                    (16, 775, 470, 322, 198),
                    (17, 876, 531, 364, 224),
                    (18, 948, 574, 394, 243),
                    (19, 1063, 644, 442, 272),
                    (20, 1159, 702, 482, 297),
                    (21, 1224, 742, 509, 314),
                    (22, 1358, 823, 565, 348),
                    (23, 1468, 890, 611, 376),
                    (24, 1588, 963, 661, 407),
                    (25, 1718, 1041, 715, 440),
                    (26, 1804, 1094, 751, 462),
                    (27, 1933, 1172, 805, 496),
                    (28, 2085, 1263, 868, 534),
                    (29, 2181, 1322, 908, 559),
                    (30, 2358, 1429, 982, 604),
                    (31, 2473, 1499, 1030, 634),
                    (32, 2670, 1618, 1112, 684),
                    (33, 2805, 1700, 1168, 719),
                    (34, 2949, 1787, 1228, 756),
                    (35, 3081, 1867, 1283, 790),
                    (36, 3244, 1966, 1351, 832),
                    (37, 3417, 2071, 1423, 876),
                    (38, 3599, 2181, 1499, 923),
                    (39, 3791, 2298, 1579, 972),
                    (40, 3993, 2420, 1663, 1024),
                ]
            },
            'High': {
                'Value_Data': [
                    (1, 17, 10, 7, 4),
                    (2, 34, 20, 14, 8),
                    (3, 58, 35, 24, 15),
                    (4, 82, 50, 34, 21),
                    (5, 106, 64, 44, 27),
                    (6, 139, 84, 58, 36),
                    (7, 154, 93, 64, 39),
                    (8, 202, 122, 84, 52),
                    (9, 235, 143, 98, 60),
                    (10, 288, 174, 119, 74),
                    (11, 331, 200, 137, 85),
                    (12, 374, 227, 155, 96),
                    (13, 427, 259, 177, 109),
                    (14, 468, 283, 194, 120),
                    (15, 530, 321, 220, 136),
                    (16, 602, 365, 250, 154),
                    (17, 674, 408, 280, 173),
                    (18, 746, 452, 310, 191),
                    (19, 813, 493, 338, 208),
                    (20, 919, 557, 382, 235),
                    (21, 969, 587, 403, 248),
                    (22, 1056, 640, 439, 270),
                    (23, 1108, 672, 461, 284),
                    (24, 1228, 744, 511, 315),
                    (25, 1286, 779, 535, 330),
                    (26, 1425, 864, 593, 365),
                    (27, 1501, 910, 625, 385),
                    (28, 1581, 958, 658, 405),
                    (29, 1677, 1016, 698, 430),
                    (30, 1782, 1080, 742, 457),
                    (31, 1897, 1150, 790, 486),
                    (32, 2022, 1226, 842, 518),
                    (33, 2157, 1307, 898, 553),
                    (34, 2301, 1394, 958, 590),
                    (35, 2361, 1431, 983, 605),
                    (36, 2524, 1530, 1051, 647),
                    (37, 2625, 1591, 1093, 673),
                    (38, 2735, 1658, 1139, 701),
                    (39, 2927, 1774, 1219, 750),
                    (40, 3057, 1852, 1273, 784),
                ]
            },
        }
        self.alpha_numberic = [(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'),
                          (9, '9'),
                          (10, 'A'), (11, 'B'), (12, 'C'), (13, 'D'), (14, 'E'), (15, 'F'), (16, 'G'), (17, 'H'),
                          (18, 'I'),
                          (19, 'J'), (20, 'K'), (21, 'L'), (22, 'M'), (23, 'N'), (24, 'O'), (25, 'P'), (26, 'Q'),
                          (27, 'R'),
                          (28, 'S'), (29, 'T'), (30, 'U'), (31, 'V'), (32, 'W'), (33, 'X'), (34, 'Y'), (35, 'Z'),
                          (36, ' '),
                          (37, '$'), (38, '%'), (39, '*'), (40, '+'), (41, '-'), (42, '.'), (43, '/'), (44, ':')
                          ]
        self.mode_indicators = [('Numeric', '0001'),
                           ('Alphanumeric', '0010'),
                           ('Byte', '0100'),
                           ('Kanji', '1000'), # not currently configured
                           ('ECI', '0111')] # not currently configured
        self.char_fill = {
            'Numeric': {
                '9': 10,
                '26': 12,
                '40': 14
            },
            'Alphanumeric': {
                '9': 9,
                '26': 11,
                '40': 13
            },
            'Byte': {
                '9': 8,
                '26': 16,
                '40': 16
            },
        }

    def place_data_codewords(self, qr_size, binary, reserve_pixels):
        start_x, start_y = qr_size - 1, 0
        orientation = 'Up'
        last_direction = ''
        next_direction = 'Left'
        dir_change = False

        total_coords = qr_size * qr_size
        bit_coords = []
        bit_coords.append((start_x, start_y))

        while start_x >= 0:
            if last_direction == 'Left':
                if dir_change:
                    next_direction = 'Left'
                    start_x -= 1
                    if start_x == 6:
                        start_x -= 1
                    dir_change = False
                else:
                    next_direction = 'Right'
            elif last_direction == 'Right':
                next_direction = 'Left'

            if orientation == 'Up':
                if next_direction == 'Left':
                    start_x -= 1
                    if (start_x, start_y) in [i[0] for i in reserve_pixels]:
                        pass
                    else:
                        if start_x >= 0:
                            bit_coords.append((start_x, start_y))

                    last_direction = next_direction
                    if start_y == qr_size - 1:
                        # start heading down
                        if (start_x + 1, start_y) in bit_coords:
                            if (start_x + 1, start_y) not in [i[0] for i in reserve_pixels]:
                                bit_coords.append((start_x - 1, start_y))
                        orientation = 'Down'
                        dir_change = True
                elif next_direction == 'Right':
                    start_x += 1
                    start_y += 1
                    if (start_x, start_y) in [i[0] for i in reserve_pixels]:
                        pass
                    else:
                        if start_x >= 0:
                            bit_coords.append((start_x, start_y))
                    last_direction = next_direction
            else:
                if next_direction == 'Left':
                    start_x -= 1
                    if (start_x, start_y) in [i[0] for i in reserve_pixels]:
                        pass
                    else:
                        if start_x >= 0:
                            bit_coords.append((start_x, start_y))
                    last_direction = next_direction
                    if start_y == 0:
                        # start heading down
                        if (start_x - 1, start_y) not in [i[0] for i in reserve_pixels]:
                            bit_coords.append((start_x - 1, start_y))
                        orientation = 'Up'
                        dir_change = True
                elif next_direction == 'Right':
                    start_x += 1
                    start_y -= 1
                    if (start_x, start_y) in [i[0] for i in reserve_pixels]:
                        pass
                    else:
                        if start_x >= 0:
                            bit_coords.append((start_x, start_y))
                    last_direction = next_direction

        data_pixels = []
        binary_index = 0
        for io in binary:
            line = bit_coords[binary_index]
            if io == '1':
                state_bit = 1
            else:
                state_bit = 0
            binary_index += 1
            data_pixels.append((line, state_bit))

        return data_pixels

    # Function to convert binary to ASCII value




    def binary_to_decimal(self, n):
        num = str(n);
        dec_value = 0;
        # Initializing base
        # value to 1, i.e 2 ^ 0
        base1 = 1;

        len1 = len(num);
        for i in range(len1 - 1, -1, -1):
            if (num[i] == '1'):
                dec_value += base1;
            base1 = base1 * 2;

        return dec_value;

    def get_block_data(self, group_1_blocks, data_codewords_per_block_1, group_2_blocks, data_codewords_per_block_2, binary_values):
        block_list = []
        codeword_index = 0
        for group in range(group_1_blocks):
            codeword_list = []
            for codeword in range(data_codewords_per_block_1):
                codeword_list.append(binary_values[codeword_index])
                codeword_index += 1
            block_list.append(codeword_list)

        if group_2_blocks != '':
            for group in range(group_2_blocks):
                codeword_list = []
                for codeword in range(data_codewords_per_block_2):
                    codeword_list.append(binary_values[codeword_index])
                    codeword_index += 1
                block_list.append(codeword_list)

        return block_list

    def equalize_list(self, list_of_lists):
        max_length = max(len(sublist) for sublist in list_of_lists)
        for sublist in list_of_lists:
            sublist.extend([''] * (max_length - len(sublist)))
        return list_of_lists

    def interlace_lists(self, lists):
        interlaced = [[i[x] for i in lists] for x in range(len(lists[0]))]
        flattened_list = [item for sublist in interlaced for item in sublist]
        x = len(lists[0])
        split_list = [flattened_list[i:i + x] for i in range(0, len(flattened_list), x)]

        return split_list

    def interlace_data(self, block_ecc_codewords, block_list):
        full_codeword_list = []
        int_blocks = [[self.binary_to_decimal(b) for b in i] for i in block_list]
        int_blocks = self.equalize_list(int_blocks)
        interlaced_codewords = self.interlace_lists(int_blocks) #self.interlace_lists(int_blocks) [[row[i] for row in int_blocks] for i in range(len(int_blocks[0]))]
        for sublist in interlaced_codewords:
            if '' in sublist:
                while '' in sublist:
                    sublist.remove('')

        interlaced_ecc_codewords = self.interlace_lists(block_ecc_codewords) #[[row[i] for row in block_ecc_codewords] for i in range(len(block_ecc_codewords[0]))]
        #for item in block_ecc_codewords:
            #print(int_to_hex(item))

        full_interlaced_codewords = [format(int(item), 'b').zfill(8) for sublist in interlaced_codewords for item in sublist]
        full_interlaced_ecc_codewords = [format(int(item), 'b').zfill(8) for sublist in interlaced_ecc_codewords for item in sublist]
        [full_codeword_list.append(i) for i in full_interlaced_codewords]
        [full_codeword_list.append(i) for i in full_interlaced_ecc_codewords]
        return full_codeword_list

    def get_remainder_bits(self, version):
        remainder_bits = [
            (1, 0),
            (2, 7),
            (3, 7),
            (4, 7),
            (5, 7),
            (6, 7),
            (7, 0),
            (8, 0),
            (9, 0),
            (10, 0),
            (11, 0),
            (12, 0),
            (13, 0),
            (14, 3),
            (15, 3),
            (16, 3),
            (17, 3),
            (18, 3),
            (19, 3),
            (20, 3),
            (21, 4),
            (22, 4),
            (23, 4),
            (24, 4),
            (25, 4),
            (26, 4),
            (27, 4),
            (28, 3),
            (29, 3),
            (30, 3),
            (31, 3),
            (32, 3),
            (33, 3),
            (34, 3),
            (35, 0),
            (36, 0),
            (37, 0),
            (38, 0),
            (39, 0),
            (40, 0),
        ]
        return [i[1] for i in remainder_bits if i[0] == int(version)][0]

    def analyze(self, input_text, ecc_level):
        Numeric = False
        Byte = False
        Alphanumeric = True
        ecc_type = ''
        binary_values = []

        try:
            numbers = [int(i) for i in input_text]
            #number = int(input_text)
            Numeric = True
            Alphanumeric = False
            ecc_type = 'Numeric'
            cc_index = 1
        except:
            for i in input_text:
                if i in [a[1] for a in self.alpha_numberic]:
                    Alphanumeric = True
                    ecc_type = 'Alphanumeric'
                    cc_index = 2
                else:
                    Byte = True
                    Alphanumeric = False
                    ecc_type = 'Byte'
                    cc_index = 3
                    break

        if Numeric:
            x = 3
            input_text_list = [input_text[y - x:y] for y in range(x, len(input_text) + x, x)]

            code_words = len(input_text_list)

            for i in input_text_list:
                if len(str(i)) == 2:
                    binary = format(int(i), 'b').zfill(7)
                elif len(str(i)) == 1:
                    binary = format(int(i), 'b').zfill(4)
                else:
                    binary = format(int(i), 'b').zfill(10)
                binary_values.append(binary)

        if Alphanumeric:
            # split string into segments of length 2
            x = 2
            input_text_list = [input_text[y - x:y] for y in range(x, len(input_text) + x, x)]

            char_values = []
            code_words = len(input_text_list)
            # determine alphanumeric binary value
            for segment in input_text_list:
                char_num = 0
                char_value = 0
                if len(segment) == 2:
                    char1value = int([i[0] for i in self.alpha_numberic if i[1] == segment[0]][0])
                    char2value = int([i[0] for i in self.alpha_numberic if i[1] == segment[1]][0])
                    char_value = (char1value * 45) + char2value
                else:
                    char_value = int([i[0] for i in self.alpha_numberic if i[1] == segment][0])
                char_values.append(char_value)
            # convert each value to binary

            value_index = 0
            for item in char_values:
                segment = input_text_list[value_index]
                if len(input_text) % 2 != 0:
                    if item == char_values[-1]:
                        binary = format(int(item), 'b').zfill(6)
                    else:
                        binary = format(int(item), 'b').zfill(11)
                else:
                    binary = format(int(item), 'b').zfill(11)
                binary_values.append(binary)

        if Byte:
            code_words = 0
            for i in input_text:
                try:
                    i.encode('utf-8')
                    binary = bin(int(ord(i)))[2:].zfill(8)
                except:
                    break
                code_words += 1
                binary_values.append(binary)

        #print('ECC Type', ecc_type)

        mode = [i[1] for i in self.mode_indicators if i[0] == ecc_type][0]
        version_capacity_data = self.character_capacities[ecc_level]['Value_Data']
        version = min([i[0] for i in version_capacity_data if i[cc_index] > len(input_text)])
        capacity = [i[cc_index] for i in version_capacity_data if i[0] == version][0]
        ecc_code = f'{version}-{ecc_level[0]}'
        ec_codewords_per_block = [i[2] for i in self.ecc_list if i[0] == ecc_code][0]
        char_len = '9' if version <= 9 else ('26' if version <= 26 else '40')
        character_count = format(len(input_text), 'b').zfill(self.char_fill[ecc_type][char_len])

        group_1_blocks = [i[3] for i in self.ecc_list if i[0] == ecc_code][0]
        data_codewords_per_block_1 = [i[4] for i in self.ecc_list if i[0] == ecc_code][0]
        group_2_blocks = [i[5] for i in self.ecc_list if i[0] == ecc_code][0]
        data_codewords_per_block_2 = [i[6] for i in self.ecc_list if i[0] == ecc_code][0]

        #print('group_1_blocks', group_1_blocks)
        #print('data_codewords_per_block_1', data_codewords_per_block_1)
        #print('group_2_blocks', group_2_blocks)
        #print('data_codewords_per_block_2', data_codewords_per_block_2)

        total_blocks = int(group_1_blocks) + int(group_2_blocks) if group_2_blocks != '' else group_1_blocks
        total_codewords = int(int(data_codewords_per_block_1)*int(group_1_blocks)) + (int(int(data_codewords_per_block_2)*int(group_2_blocks)) if group_2_blocks != '' else 0)

        return version, capacity, ecc_code, mode, character_count, ec_codewords_per_block, group_1_blocks, data_codewords_per_block_1, group_2_blocks, data_codewords_per_block_2, total_blocks, binary_values, total_codewords




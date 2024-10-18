import math
class ErrorCorrection():
    def __init__(self):
        self.log_antilog = [
            (0, 1, 0, 0),
            (1, 2, 1, 0),
            (2, 4, 2, 1),
            (3, 8, 3, 25),
            (4, 16, 4, 2),
            (5, 32, 5, 50),
            (6, 64, 6, 26),
            (7, 128, 7, 198),
            (8, 29, 8, 3),
            (9, 58, 9, 223),
            (10, 116, 10, 51),
            (11, 232, 11, 238),
            (12, 205, 12, 27),
            (13, 135, 13, 104),
            (14, 19, 14, 199),
            (15, 38, 15, 75),
            (16, 76, 16, 4),
            (17, 152, 17, 100),
            (18, 45, 18, 224),
            (19, 90, 19, 14),
            (20, 180, 20, 52),
            (21, 117, 21, 141),
            (22, 234, 22, 239),
            (23, 201, 23, 129),
            (24, 143, 24, 28),
            (25, 3, 25, 193),
            (26, 6, 26, 105),
            (27, 12, 27, 248),
            (28, 24, 28, 200),
            (29, 48, 29, 8),
            (30, 96, 30, 76),
            (31, 192, 31, 113),
            (32, 157, 32, 5),
            (33, 39, 33, 138),
            (34, 78, 34, 101),
            (35, 156, 35, 47),
            (36, 37, 36, 225),
            (37, 74, 37, 36),
            (38, 148, 38, 15),
            (39, 53, 39, 33),
            (40, 106, 40, 53),
            (41, 212, 41, 147),
            (42, 181, 42, 142),
            (43, 119, 43, 218),
            (44, 238, 44, 240),
            (45, 193, 45, 18),
            (46, 159, 46, 130),
            (47, 35, 47, 69),
            (48, 70, 48, 29),
            (49, 140, 49, 181),
            (50, 5, 50, 194),
            (51, 10, 51, 125),
            (52, 20, 52, 106),
            (53, 40, 53, 39),
            (54, 80, 54, 249),
            (55, 160, 55, 185),
            (56, 93, 56, 201),
            (57, 186, 57, 154),
            (58, 105, 58, 9),
            (59, 210, 59, 120),
            (60, 185, 60, 77),
            (61, 111, 61, 228),
            (62, 222, 62, 114),
            (63, 161, 63, 166),
            (64, 95, 64, 6),
            (65, 190, 65, 191),
            (66, 97, 66, 139),
            (67, 194, 67, 98),
            (68, 153, 68, 102),
            (69, 47, 69, 221),
            (70, 94, 70, 48),
            (71, 188, 71, 253),
            (72, 101, 72, 226),
            (73, 202, 73, 152),
            (74, 137, 74, 37),
            (75, 15, 75, 179),
            (76, 30, 76, 16),
            (77, 60, 77, 145),
            (78, 120, 78, 34),
            (79, 240, 79, 136),
            (80, 253, 80, 54),
            (81, 231, 81, 208),
            (82, 211, 82, 148),
            (83, 187, 83, 206),
            (84, 107, 84, 143),
            (85, 214, 85, 150),
            (86, 177, 86, 219),
            (87, 127, 87, 189),
            (88, 254, 88, 241),
            (89, 225, 89, 210),
            (90, 223, 90, 19),
            (91, 163, 91, 92),
            (92, 91, 92, 131),
            (93, 182, 93, 56),
            (94, 113, 94, 70),
            (95, 226, 95, 64),
            (96, 217, 96, 30),
            (97, 175, 97, 66),
            (98, 67, 98, 182),
            (99, 134, 99, 163),
            (100, 17, 100, 195),
            (101, 34, 101, 72),
            (102, 68, 102, 126),
            (103, 136, 103, 110),
            (104, 13, 104, 107),
            (105, 26, 105, 58),
            (106, 52, 106, 40),
            (107, 104, 107, 84),
            (108, 208, 108, 250),
            (109, 189, 109, 133),
            (110, 103, 110, 186),
            (111, 206, 111, 61),
            (112, 129, 112, 202),
            (113, 31, 113, 94),
            (114, 62, 114, 155),
            (115, 124, 115, 159),
            (116, 248, 116, 10),
            (117, 237, 117, 21),
            (118, 199, 118, 121),
            (119, 147, 119, 43),
            (120, 59, 120, 78),
            (121, 118, 121, 212),
            (122, 236, 122, 229),
            (123, 197, 123, 172),
            (124, 151, 124, 115),
            (125, 51, 125, 243),
            (126, 102, 126, 167),
            (127, 204, 127, 87),
            (128, 133, 128, 7),
            (129, 23, 129, 112),
            (130, 46, 130, 192),
            (131, 92, 131, 247),
            (132, 184, 132, 140),
            (133, 109, 133, 128),
            (134, 218, 134, 99),
            (135, 169, 135, 13),
            (136, 79, 136, 103),
            (137, 158, 137, 74),
            (138, 33, 138, 222),
            (139, 66, 139, 237),
            (140, 132, 140, 49),
            (141, 21, 141, 197),
            (142, 42, 142, 254),
            (143, 84, 143, 24),
            (144, 168, 144, 227),
            (145, 77, 145, 165),
            (146, 154, 146, 153),
            (147, 41, 147, 119),
            (148, 82, 148, 38),
            (149, 164, 149, 184),
            (150, 85, 150, 180),
            (151, 170, 151, 124),
            (152, 73, 152, 17),
            (153, 146, 153, 68),
            (154, 57, 154, 146),
            (155, 114, 155, 217),
            (156, 228, 156, 35),
            (157, 213, 157, 32),
            (158, 183, 158, 137),
            (159, 115, 159, 46),
            (160, 230, 160, 55),
            (161, 209, 161, 63),
            (162, 191, 162, 209),
            (163, 99, 163, 91),
            (164, 198, 164, 149),
            (165, 145, 165, 188),
            (166, 63, 166, 207),
            (167, 126, 167, 205),
            (168, 252, 168, 144),
            (169, 229, 169, 135),
            (170, 215, 170, 151),
            (171, 179, 171, 178),
            (172, 123, 172, 220),
            (173, 246, 173, 252),
            (174, 241, 174, 190),
            (175, 255, 175, 97),
            (176, 227, 176, 242),
            (177, 219, 177, 86),
            (178, 171, 178, 211),
            (179, 75, 179, 171),
            (180, 150, 180, 20),
            (181, 49, 181, 42),
            (182, 98, 182, 93),
            (183, 196, 183, 158),
            (184, 149, 184, 132),
            (185, 55, 185, 60),
            (186, 110, 186, 57),
            (187, 220, 187, 83),
            (188, 165, 188, 71),
            (189, 87, 189, 109),
            (190, 174, 190, 65),
            (191, 65, 191, 162),
            (192, 130, 192, 31),
            (193, 25, 193, 45),
            (194, 50, 194, 67),
            (195, 100, 195, 216),
            (196, 200, 196, 183),
            (197, 141, 197, 123),
            (198, 7, 198, 164),
            (199, 14, 199, 118),
            (200, 28, 200, 196),
            (201, 56, 201, 23),
            (202, 112, 202, 73),
            (203, 224, 203, 236),
            (204, 221, 204, 127),
            (205, 167, 205, 12),
            (206, 83, 206, 111),
            (207, 166, 207, 246),
            (208, 81, 208, 108),
            (209, 162, 209, 161),
            (210, 89, 210, 59),
            (211, 178, 211, 82),
            (212, 121, 212, 41),
            (213, 242, 213, 157),
            (214, 249, 214, 85),
            (215, 239, 215, 170),
            (216, 195, 216, 251),
            (217, 155, 217, 96),
            (218, 43, 218, 134),
            (219, 86, 219, 177),
            (220, 172, 220, 187),
            (221, 69, 221, 204),
            (222, 138, 222, 62),
            (223, 9, 223, 90),
            (224, 18, 224, 203),
            (225, 36, 225, 89),
            (226, 72, 226, 95),
            (227, 144, 227, 176),
            (228, 61, 228, 156),
            (229, 122, 229, 169),
            (230, 244, 230, 160),
            (231, 245, 231, 81),
            (232, 247, 232, 11),
            (233, 243, 233, 245),
            (234, 251, 234, 22),
            (235, 235, 235, 235),
            (236, 203, 236, 122),
            (237, 139, 237, 117),
            (238, 11, 238, 44),
            (239, 22, 239, 215),
            (240, 44, 240, 79),
            (241, 88, 241, 174),
            (242, 176, 242, 213),
            (243, 125, 243, 233),
            (244, 250, 244, 230),
            (245, 233, 245, 231),
            (246, 207, 246, 173),
            (247, 131, 247, 232),
            (248, 27, 248, 116),
            (249, 54, 249, 214),
            (250, 108, 250, 244),
            (251, 216, 251, 234),
            (252, 173, 252, 168),
            (253, 71, 253, 80),
            (254, 142, 254, 88),
            (255, 1, 255, 175),
        ]

        self.alpha_numberic = [(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'),
                          (10, 'A'), (11, 'B'), (12, 'C'), (13, 'D'), (14, 'E'), (15, 'F'), (16, 'G'), (17, 'H'), (18, 'I'),
                          (19, 'J'), (20, 'K'), (21, 'L'), (22, 'M'), (23, 'N'), (24, 'O'), (25, 'P'), (26, 'Q'), (27, 'R'),
                          (28, 'S'), (29, 'T'), (30, 'U'), (31, 'V'), (32, 'W'), (33, 'X'), (34, 'Y'), (35, 'Z'), (36, ' '),
                          (37, '$'), (38, '%'), (39, '*'), (40, '+'), (41, '-'), (42, '.'), (43, '/'), (44, ':')
                          ]


        input_text = '00010101011101011010001000000100001001000011011011100101011101100111010000000100101101110111001101110011011101110011001010010110011101011110001100100101000101010110011010110111011100100011011001000111'
        ec_codewords_per_block = 30
        input_text = '11010101000101000100010010010111100101001111010000100011011101101011011110100110100001010110011001100010000000110000011010010100111001001100011110000100001001101111011011110010011001101000010010010101000000101010011110010101000000101000011110010101000001101011011100010110111101001101010100010101001101110011010011110011010101111010010110010011011101000000010001100111000001100111011011100101111001010100011010110010010001011010010011110110110101001011010011110110011000110111001110010110011101101000011011110100100100110111010001000101100100110010010010100100010001101100001000000110011101111010010101110101100101100101010100110101000001100010001110010011100101101111010101010100111101100001001101110111001101000100011101110100000100110010011100000110101100100001011010000100110001000010011110100111001000110001011011100111010001001100010000000100101001101100001001100101011100100000010000010111000001011010011101010111'
        ec_codewords_per_block = 30
        [143, 112, 146, 193, 134, 105, 87, 151, 128, 219, 125, 125, 46, 234, 203, 223, 40, 123, 252, 38, 14, 220, 168, 15, 34, 54, 71, 190, 62, 0]
        #self.get_ecc(ec_codewords_per_block, input_text, verbose=True)


    def get_message_polynomial(self, input_text, ec_codewords_per_block):
        # Getting the decimal value of each character
        x = 8
        bits = [input_text[y - x:y] for y in range(x, len(input_text) + x, x)]

        decimal_values = []
        for item in bits:
            decimal_value = int(item, 2)
            decimal_values.append(decimal_value)
        poly_count = len(decimal_values) - 1
        message_polynomial = []
        for item in decimal_values:
            message_polynomial.append([item, poly_count + ec_codewords_per_block]) # adding number of codewords to make sure leading exponent isnt too small
            poly_count -= 1
        return message_polynomial

    def get_message_polynomial_string(self, input_text, ec_codewords_per_block):
        'This will be set up solely to print out a string version of the message polynomial'
        # Getting the decimal value of each character
        x = 8
        bits = [input_text[y - x:y] for y in range(x, len(input_text) + x, x)]
        decimal_values = []
        for item in bits:
            decimal_value = int(item, 2)
            decimal_values.append(decimal_value)

        poly_count = len(decimal_values) - 1
        message_polynomial = ''
        for item in decimal_values:
            if poly_count == 0:
                message = f'{item}x^{poly_count + ec_codewords_per_block}'
            else:
                message = f'{item}x^{poly_count + ec_codewords_per_block}+'  # adding number of codewords to make sure leading exponent isnt too small
            message_polynomial = message_polynomial + message
            poly_count -= 1

        return message_polynomial

    def poly_split(self, poly_string):
        side1, side2 = poly_string.split('*')
        add1 = side1.split('+')
        add2 = side2.split('+')
        items_1 = []
        for item in add1:
            items = item.split('x^')
            items = [i.replace('a^', '') for i in items]
            items_1.append(items)

        items_2 = []
        for item in add2:
            items = item.split('x^')
            items = [i.replace('a^', '') for i in items]
            items_2.append(items)
        return items_1, items_2

    def poly_join(self, poly_list):
        poly_string = ''
        count = 1
        for item in poly_list:
            if count == len(poly_list):
                poly_string = poly_string + f'a^{item[0]}x^{item[1]}'
            else:
                poly_string = poly_string + f'a^{item[0]}x^{item[1]}+'
            count += 1
        return poly_string

    def multiply_generator_xor(self, lead_term, generator_polynomial):
        # convert to alpha
        lead_term = self.get_antilog(lead_term)
        step_1 = []
        for a_term, x_term in generator_polynomial:
            a_exp = a_term
            output = lead_term + a_exp
            #output = (output % 256) + math.floor(output / 256) if output > 255 else output
            output = (output % 255) if output > 255 else output
            # convert to integer
            int_output = self.get_log(output)
            step_1.append(int_output)
        return step_1

    def multiply_generator_xor2(self, lead_term, generator_polynomial):
        # convert to alpha
        lead_term = self.get_antilog(lead_term)
        step_1 = []
        for a_term, _ in [i.split('x^') for i in generator_polynomial.split('+')]:
            a_exp = int(a_term.split('a^')[1])
            output = int(lead_term) + a_exp
            #output = (output % 256) + math.floor(output / 256) if output > 255 else output
            output = (output % 255) if output > 255 else output
            # convert to integer
            int_output = self.get_log(output)
            step_1.append(int_output)
        return step_1

    def xor_results(self, multiplied_list, last_list):
        step_2 = []
        var_index = 0
        for item in last_list:
            exp_1b = int(item)
            if var_index < len(multiplied_list):
                output = exp_1b ^ int(multiplied_list[var_index])
            else:
                output = exp_1b ^ 0
            step_2.append(output)
            var_index += 1

        # discard the lead zero
        if step_2[0] == 0:
            step_2.pop(0)
        elif step_2[0] == 1:
            step_2.pop(0)

        return step_2

    def make_even(self, list1, list2):
        if len(list1) < len(list2):
            [list1.append(0) for i in range(len(list2) - len(list1))]
        else:
            [list2.append(0) for i in range(len(list1) - len(list2))]

        return list1, list2

    def get_antilog(self, value):
        return [i[3] for i in self.log_antilog if i[2] == int(value)][0]

    def get_log(self, value):
        return [i[1] for i in self.log_antilog if i[0] == int(value)][0]

    def get_generator_polynomial(self, ec_codewords_per_block, lead_exponent):
        previous_poly_list = [[0, 1], [0, 0]]
        for step in range(ec_codewords_per_block - 1):
            step = step + 1
            new_poly_list = [[0, 1], [step, 0]]
            grouping = []
            index_2 = 0
            for i in previous_poly_list:
                for a in new_poly_list:
                    grouping.append((i, a))

            terms = []
            for item in grouping:
                a, x = item
                a1, a2 = a
                x1, x2 = x

                a1 = (a1 % 256) + math.floor(a1 / 256) if a1 > 255 else a1
                a2 = (a2 % 256) + math.floor(a2 / 256) if a2 > 255 else a2
                x1 = (x1 % 256) + math.floor(x1 / 256) if x1 > 255 else x1
                x2 = (x2 % 256) + math.floor(x2 / 256) if x2 > 255 else x2

                #a1 = (a1 % 255) if a1 > 255 else a1
                #a2 = (a2 % 255) if a2 > 255 else a2
                #x1 = (x1 % 255) if x1 > 255 else x1
                #x2 = (x2 % 255) if x2 > 255 else x2

                exp1 = a1 + x1
                exp2 = a2 + x2
                terms.append((exp1, exp2))

            # combine terms if multiple x^n factors
            single_terms = list(set([i[1] for i in terms]))
            combine_list = []
            for item in single_terms:
                dups = len([i[0] for i in terms if i[1] == item])
                if dups > 1:
                    combine_list.append(item)


            for item in combine_list:
                items_to_combine = [i for i in terms if i[1] == item]
                xor_items = []
                for term in items_to_combine:
                    terms.remove(term)
                    a, x = term
                    #a = (a % 256) + math.floor(a / 256) if a > 255 else a
                    a = (a % 255) if a > 255 else a
                    tolog = self.get_log(a)
                    xor_items.append(tolog)

                item_no = 0
                last_item = 0
                for item in xor_items:
                    if item_no == 0:
                        last_item = item
                    else:
                        last_item = last_item ^ item
                    item_no += 1
                antilog = self.get_antilog(last_item)
                terms.append([antilog, x])

            previous_poly_list = terms

        # Need to sort by the exponent on the x value
        sorted_poly_list = sorted(previous_poly_list, key=lambda x: x[1], reverse=True)

        string_count = 1
        # adding number of codewords to make sure leading exponent isnt too small
        exponent_equalizer = lead_exponent - int(sorted_poly_list[0][1])
        new_poly_list = []
        for item in sorted_poly_list:
            new_poly_list.append([item[0], int(item[1]) + exponent_equalizer]) #new_poly_list + f'{item[0]}x^{int(item[1]) + exponent_equalizer}'  # not actually going to add anything until i know exactly what to add +(ec_codewords_per_block-1)
            string_count += 1

        return new_poly_list

    def get_generator_polynomial_string(self, ec_codewords_per_block, lead_exponent):
        'This will be set up solely to print out a string version of the generator polynomial'

        previous_poly_string = 'a^0x^1+a^0x^0'
        for step in range(ec_codewords_per_block - 1):
            step = step + 1
            poly_string = f'{previous_poly_string}*a^0x^1+a^{step}x^0'
            items_1, items_2 = self.poly_split(poly_string)
            grouping = []
            index_2 = 0
            for i in items_1:
                for a in items_2:
                    grouping.append((i, a))

            terms = []
            for item in grouping:
                a, x = item
                a1 = int(a[0])
                a2 = int(a[1])
                x1 = int(x[0])
                x2 = int(x[1])

                a1 = (a1 % 256) + math.floor(a1 / 256) if a1 > 255 else a1
                a2 = (a2 % 256) + math.floor(a2 / 256) if a2 > 255 else a2
                x1 = (x1 % 256) + math.floor(x1 / 256) if x1 > 255 else x1
                x2 = (x2 % 256) + math.floor(x2 / 256) if x2 > 255 else x2

                #a1 = (a1 % 255) if a1 > 255 else a1
                #a2 = (a2 % 255) if a2 > 255 else a2
                #x1 = (x1 % 255) if x1 > 255 else x1
                #x2 = (x2 % 255) if x2 > 255 else x2

                exp1 = int(a1) + int(x1)
                exp2 = int(a2) + int(x2)
                terms.append((f'{exp1}', f'{exp2}'))

            # combine terms if multiple x^n factors
            single_terms = list(set([i[1] for i in terms]))
            combine_list = []
            for item in single_terms:
                dups = len([i[0] for i in terms if i[1] == item])
                if dups > 1:
                    combine_list.append(item)

            for item in combine_list:
                items_to_combine = [i for i in terms if i[1] == item]
                xor_items = []
                for term in items_to_combine:
                    terms.remove(term)
                    a, x = term
                    #a = (int(a) % 256) + math.floor(int(a) / 256) if int(a) > 255 else int(a)
                    a = (int(a) % 255) if int(a) > 255 else int(a)
                    tolog = self.get_log(a)
                    xor_items.append(tolog)

                item_no = 0
                last_item = 0
                for item in xor_items:
                    if item_no == 0:
                        last_item = item
                    else:
                        last_item = last_item ^ item
                    item_no += 1
                antilog = self.get_antilog(last_item)
                terms.append((str(antilog), str(x)))

            previous_poly_string = self.poly_join(terms)

        # Need to sort by the exponent on the x value
        sorted_poly = sorted([i.split('x^') for i in previous_poly_string.split('+')], key=lambda x: int(x[1]),
                             reverse=True)
        new_poly_string = ''
        string_count = 1
        # adding number of codewords to make sure leading exponent isnt too small
        exponent_equalizer = lead_exponent - int(sorted_poly[0][1])
        for item in sorted_poly:
            if string_count == len(sorted_poly):
                new_poly_string = new_poly_string + f'{item[0]}x^{int(item[1])+exponent_equalizer}'  # not actually going to add anything until i know exactly what to add +(ec_codewords_per_block-1)
            else:
                new_poly_string = new_poly_string + f'{item[0]}x^{int(item[1])+exponent_equalizer}+'
            string_count += 1
        return new_poly_string

    def get_ecc(self, ec_codewords_per_block, input_text, verbose=False):
        verbose = False
        print(input_text) if verbose else ''
        message_polynomial = self.get_message_polynomial(input_text, ec_codewords_per_block)
        print(ec_codewords_per_block, [i[0] for i in message_polynomial]) if verbose else ''
        # Verify that the lead term of the generator polynomial has the same exponent as the lead of the message polynomial
        lead_exponent = int(message_polynomial[0][1])
        generator_polynomial = self.get_generator_polynomial(ec_codewords_per_block, lead_exponent)

        # Step 1a: Multiply the Generator Polynomial by the Lead Term of the Message Polynomial
        lead_term = message_polynomial[0]
        lead_alpha_exponent = self.get_antilog(int(lead_term[0]))

        int_notations = []
        for a_term, x_term in generator_polynomial:
            a_var = a_term + int(lead_alpha_exponent)
            #a_var = (a_var % 256) + math.floor(a_var / 256) if a_var > 255 else a_var
            a_var = (a_var % 255) if a_var > 255 else a_var
            a_var = self.get_log(a_var)
            int_notations.append([a_var, x_term])

        print('Step 1a', int_notations) if verbose else ''
        total_loops = len(message_polynomial) # get total number of loops before making lists the same length

        # Step 1b: XOR the result with the message polynomial
        int_notations, split_message = self.make_even(int_notations, message_polynomial)
        step_1b = []
        var_index = 0
        for i in range(len(int_notations)):
            item = split_message[i] if split_message[i] != 0 else [0, 0]
            item_2 = int_notations[i] if int_notations[i] != 0 else [0, 0]

            a_var = int(item[0])
            x_var = int(item_2[0])
            if var_index < len(int_notations):
                output = a_var ^ x_var
            else:
                output = a_var ^ 0


            step_1b.append(output)
            var_index += 1
        print('Step 1b', step_1b) if verbose else ''
        # discard the lead zero
        step_1b.remove(0)

        current_loop = 2
        lead_term = step_1b[0]
        last_list = step_1b

        while current_loop <= total_loops:
            # Multiply the Generator Polynomial by the Lead Term of the previous loop
            multiplied_list = self.multiply_generator_xor(lead_term, generator_polynomial)
            print(f'Step {current_loop}a', multiplied_list) if verbose else ''
            # make the two lists the same length by adding zeros to the lesser
            last_list, multiplied_list = self.make_even(last_list, multiplied_list)
            # XOR the result with the result from previous loop
            last_list = self.xor_results(multiplied_list, last_list)
            print(f'Step {current_loop}b', last_list) if verbose else ''

            if last_list[0] == 0:
                # Discard lead term if lead term is still zero
                # this counts as a divistion step
                last_list.pop(0)
                current_loop += 1
                print(f'Step {current_loop}', last_list) if verbose else ''

            #elif last_list[0] == 1:
                #last_list.pop(0)
                #current_loop += 1
                #print(f'Step {current_loop}', last_list) if verbose else ''

            lead_term = last_list[0]

            current_loop += 1

        #print(lead_exponent)
        #print(len(last_list))
        #print(current_loop)
        #print(lead_exponent - len(last_list) - (current_loop-1))
        if len(last_list) < ec_codewords_per_block:
            if lead_exponent - len(last_list) - (current_loop - 1) == 0:
                last_list.append(0)
            elif lead_exponent - len(last_list) - (current_loop - 1) == -1:
                last_list.insert(0, 0)
            #print(input_text, '\n', ec_codewords_per_block, '\n', last_list)

        #print('Total Steps', current_loop) if verbose else ''

        print('Final Output:', last_list) if verbose else ''

        #print('#######################################################################################################')
        return last_list

    def get_ecc2(self, ec_codewords_per_block, input_text):
        print('Required Number of Codewords', ec_codewords_per_block)
        message_polynomial = self.get_message_polynomial_string(input_text, ec_codewords_per_block)
        # Verify that the lead term of the generator polynomial has the same exponent as the lead of the message polynomial
        lead_exponent = int(message_polynomial.split('+')[0].split('^')[1])
        generator_polynomial = self.get_generator_polynomial_string(ec_codewords_per_block, lead_exponent)
        #print(message_polynomial)
        #print(generator_polynomial)

        # Step 1a: Multiply the Generator Polynomial by the Lead Term of the Message Polynomial
        lead_term = message_polynomial.split('+')[0]
        lead_alpha_exponent = self.get_antilog(int(int(lead_term.split('x')[0])))
        int_notations = []
        for a_term, _ in [i.split('x^') for i in generator_polynomial.split('+')]:
            a_var = int(a_term.split('^')[1]) + int(lead_alpha_exponent)
            #a_var = (a_var % 256) + math.floor(a_var / 256) if a_var > 255 else a_var
            a_var = (a_var % 255) if a_var > 255 else a_var
            a_var = self.get_log(a_var)
            int_notations.append([str(a_var), _])

        #print('int_notations', int_notations)

        # Step 1b: XOR the result with the message polynomial
        int_notations, split_message = self.make_even(int_notations, [x.split('x^') for x in message_polynomial.split('+')])
        step_1b = []
        var_index = 0
        for i in range(len(int_notations)):
            item = split_message[i] if split_message[i] != 0 else [0, 0]
            item_2 = int_notations[i] if int_notations[i] != 0 else [0, 0]


            a_var = int(item[0])
            x_var = int(item_2[0])
            if var_index < len(int_notations):
                output = a_var ^ x_var
            else:
                output = a_var ^ 0


            step_1b.append(output)
            var_index += 1
        # discard the lead zero
        #print(step_1b)
        step_1b.remove(0)


        total_loops = len([i.split('x^') for i in message_polynomial.split('+')])
        print('total_loops', total_loops)
        current_loop = 2
        lead_term = step_1b[0]
        last_list = step_1b
        #for i in range(total_loops):
        while current_loop <= total_loops:
            # Multiply the Generator Polynomial by the Lead Term of the previous loop
            multiplied_list = self.multiply_generator_xor2(lead_term, generator_polynomial)
            #print('multiplied_list', multiplied_list)
            # make the two lists the same length by adding zeros to the lesser
            last_list, multiplied_list = self.make_even(last_list, multiplied_list)

            # XOR the result with the result from previous loop
            last_list = self.xor_results(multiplied_list, last_list)

            # Discard lead term if lead term is zero
            while last_list[0] == 0:
                last_list.remove(0)
                current_loop += 1

            #print(last_list)
            lead_term = last_list[0]
            current_loop += 1

        print('Output ECC Codewords', len(last_list))
        return last_list

    def get_final_string(self):
        final_string_list = [
            ('L', 0, '111011111000100'),
            ('L', 1, '111001011110011'),
            ('L', 2, '111110110101010'),
            ('L', 3, '111100010011101'),
            ('L', 4, '110011000101111'),
            ('L', 5, '110001100011000'),
            ('L', 6, '110110001000001'),
            ('L', 7, '110100101110110'),
            ('M', 0, '101010000010010'),
            ('M', 1, '101000100100101'),
            ('M', 2, '101111001111100'),
            ('M', 3, '101101101001011'),
            ('M', 4, '100010111111001'),
            ('M', 5, '100000011001110'),
            ('M', 6, '100111110010111'),
            ('M', 7, '100101010100000'),
            ('Q', 0, '011010101011111'),
            ('Q', 1, '011000001101000'),
            ('Q', 2, '011111100110001'),
            ('Q', 3, '011101000000110'),
            ('Q', 4, '010010010110100'),
            ('Q', 5, '010000110000011'),
            ('Q', 6, '010111011011010'),
            ('Q', 7, '010101111101101'),
            ('H', 0, '001011010001001'),
            ('H', 1, '001001110111110'),
            ('H', 2, '001110011100111'),
            ('H', 3, '001100111010000'),
            ('H', 4, '000011101100010'),
            ('H', 5, '000001001010101'),
            ('H', 6, '000110100001100'),
            ('H', 7, '000100000111011'),
        ]

    def get_format_ecc(self, ec_codewords_per_block, input_text):
        binary_version = '10100110111' # this is the defined and set binary version of the generator polynomial
        # make input text binary length equal to 15
        while len(input_text) != 15:
            input_text = input_text + '0'
        # then remove any leading zeroes

        for i in input_text:
            if i == '1':
                break
            else:
                input_text = input_text[1:]

        # set generator polynomial bits to same length as current text input
        padded_generator = binary_version
        while len(padded_generator) < len(input_text):
            padded_generator = padded_generator + '0'

        xord = ''
        bit_index = 0
        for bit in input_text:
            xor_result = int(bit) ^ int(padded_generator[bit_index])
            bit_index += 1
            xord = xord + str(xor_result)

        for i in xord:
            if i == '1':
                break
            else:
                xord = xord[1:]



        while len(xord) > 10:
            # remove leading zeroes from the result
            for i in xord:
                if i == '1':
                    break
                else:
                    xord = xord[1:]
            input_text = xord
            if len(xord) > ec_codewords_per_block:
                # its still too long, add padding to generator polynomial again+
                padded_generator = binary_version
                while len(padded_generator) < len(xord):
                    padded_generator = padded_generator + '0'
                # now xor the two strings
                bit_index = 0
                updated_xord = ''
                for bit in xord:
                    xor_result = int(bit) ^ int(padded_generator[bit_index])
                    bit_index += 1
                    updated_xord = updated_xord + str(xor_result)

                xord = updated_xord

        xord = xord.zfill(10)
        return xord

    def get_version_ecc(self, ec_codewords_per_block, input_text):
        binary_version = '1111100100101'  # this is the defined and set binary version of the generator polynomial
        # make input text binary length equal to 15
        while len(input_text) != 18:
            input_text = input_text + '0'
        # then remove any leading zeroes

        for i in input_text:
            if i == '1':
                break
            else:
                input_text = input_text[1:]

        # set generator polynomial bits to same length as current text input
        padded_generator = binary_version
        while len(padded_generator) < len(input_text):
            padded_generator = padded_generator + '0'

        xord = ''
        bit_index = 0
        for bit in input_text:
            xor_result = int(bit) ^ int(padded_generator[bit_index])
            bit_index += 1
            xord = xord + str(xor_result)

        for i in xord:
            if i == '1':
                break
            else:
                xord = xord[1:]

        while len(xord) > ec_codewords_per_block:
            # remove leading zeroes from the result
            for i in xord:
                if i == '1':
                    break
                else:
                    xord = xord[1:]
            input_text = xord
            if len(xord) > ec_codewords_per_block:
                # its still too long, add padding to generator polynomial again+
                padded_generator = binary_version
                while len(padded_generator) < len(xord):
                    padded_generator = padded_generator + '0'
                # now xor the two strings
                bit_index = 0
                updated_xord = ''
                for bit in xord:
                    xor_result = int(bit) ^ int(padded_generator[bit_index])
                    bit_index += 1
                    updated_xord = updated_xord + str(xor_result)

                xord = updated_xord

        xord = xord.zfill(ec_codewords_per_block)
        return xord



#input_text = '0100000000101100111001011110010101000101100001101001010010110100100101011010010110010100100001110111010011010110100101110110011011000011011001100100011000110111001001110000010101110100111101001000010110100010010101110101001100000110011100111001010010000111101000110001001110010101100001100111011101010100110001100111010011100011011101101011011100000011001100101010011011000110011001010101001001010101001101010100001001010110000101000000001110010011011000110001001010000101101001101011011100000100001101101111010000010111010101111001011101000011000001011001011101010010100001110111010001100110111001111010001010010011010101000000010000100100110001000011010010100010101000110101011011110100010100110011010001010100010101010110001000110110010001010001001110010110111100101001010000010101011101000010010101000111100001010110010001110011011001010101011100000100001101110111010101000110110100100001011001100010'
#ec_codewords_per_block = 28

#count = 0
#for item in text_list:
    #input_text = item
    #ec_codewords_per_block = number_list[count]
    #print(get_ecc(ec_codewords_per_block, input_text))
    #count += 1





x = ErrorCorrection()
#28
#α^0x^28+α^168x^27+α^223x^26+α^200x^25+α^104x^24+α^224x^23+α^234x^22+α^108x^21+α^180x^20+α^110x^19+α^190x^18+α^195x^17+α^147x^16+α^205x^15+α^27x^14+α^232x^13+α^201x^12+α^21x^11+α43x10 + α245x9 + α87x8 + α42x7 + α195x6 + α212x5 + α119x4 + α242x3 + α37x2 + α9x + α123
#a^0x^140+a^168x^139+a^223x^138+a^200x^137+a^104x^136+a^224x^135+a^234x^134+a^108x^133+a^180x^132+a^110x^131+a^190x^130+a^195x^129+a^147x^128+a^205x^127+a^27x^126+a^232x^125+a^201x^124+a^21x^123+a^43x^122+a^245x^121+a^87x^120+a^42x^119+a^195x^118+a^212x^117+a^119x^116+a^242x^115+a^37x^114+a^9x^113+a^123x^112
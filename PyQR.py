import math
from qr_shapes import *
from ErrorCorrection import ErrorCorrection
import numpy as np
from qr_masks import *
from qr_penalty import *
from qr_imager import *
from qr_ps import *
from qr_coords import *
from DataAnalysis import DataAnalysis

# Resource Links i used to build this
# full qr creation Tutorial
# https://www.thonky.com/qr-code-tutorial/introduction
# General Resource QR Wiki
# https://en.wikipedia.org/wiki/QR_code
# QR Creation Tool with Steps
# https://www.nayuki.io/page/creating-a-qr-code-step-by-step

class QR():
    def __init__(self):
        self.Data = DataAnalysis()
        self.ECC = ErrorCorrection()

    def generate_qr(self, data_string, correction_level='Low', mask=None, PrintData=False):
        if mask is not None:
            if mask not in [0, 1, 2, 3, 4, 5, 6, 7]:
                raise Exception('Invalid Mask Number - Please Select a Number Between 0 - 7')
                return

        if correction_level not in ['Low', 'Medium', 'Quartile', 'High']:
            raise Exception('Invalid Correction Level - Please Select from (Low, Medium, Quartile, High)')
            return

        self.Mask = mask

        self.PrintData = PrintData
        # Correction Level Options: Low, Medium, Quartile, High
        (version, capacity, ecc_code, mode, character_count, ec_codewords_per_block, group_1_blocks,
         data_codewords_per_block_1, group_2_blocks, data_codewords_per_block_2, total_blocks, binary_values,
         total_codewords) = self.Data.analyze(data_string, correction_level)
        self.printer(f'Total Group 1 Blocks: {group_1_blocks}')
        self.printer(f'Total Blocks per Group 1 Blocks: {data_codewords_per_block_1}')
        self.printer(f'Total Group 2 Blocks: {group_2_blocks}')
        self.printer(f'Total Blocks per Group 2 Blocks: {data_codewords_per_block_2}')


        total_data_bits = total_codewords * 8
        base_message = "".join(binary_values)
        self.printer(f'Total Data Bits Required: {total_data_bits}')
        self.printer(f'Requird Codewords Per Block: {ec_codewords_per_block}')
        self.printer(f'Version: {version}')
        self.printer(f'Mode String: {mode}')
        self.printer(f'Character String: {character_count}')
        self.printer(f'Initial Data String: {base_message}')

        binary = ''
        binary += mode
        binary += character_count
        binary += base_message

        terminator = '0000' if len(binary) + 4 < total_data_bits else (
            '0'.zfill(total_data_bits - len(binary)) if len(binary) < total_data_bits else '')
        self.printer(f'Terminator String: {terminator}')

        #for i in terminator:
            #binary = binary + i

        binary += terminator

        while len(binary) % 8 != 0:  # the length has to be a multiple of 8
            binary += '0'

        pad_bits = int((total_data_bits - len(binary)) / 8)
        self.printer(f'Total Pad Bits Required: {pad_bits}')
        pad_bit_1 = '11101100'  # qr spec pad bit #1
        pad_bit_2 = '00010001'  # qr spec pad bit #2
        pad_string = ''
        while pad_bits > 0:
            binary = binary + pad_bit_1
            pad_string = pad_string + pad_bit_1
            pad_bits -= 1
            if pad_bits == 0:
                pass
            else:
                binary = binary + pad_bit_2
                pad_string = pad_string + pad_bit_2
                pad_bits -= 1
        self.printer(f'Pad String: {pad_string}')
        self.printer(f'Data String: {binary}')
        if total_blocks > 1:
            # split binary string into segments of length 8
            x = 8
            input_text_list = [binary[y - x:y] for y in range(x, len(binary) + x, x)]
            block_ecc_codewords = []
            block_codewords = self.Data.get_block_data(group_1_blocks, data_codewords_per_block_1, group_2_blocks,
                                                       data_codewords_per_block_2, input_text_list)
            print(block_codewords)
            for block in block_codewords:
                block_ecc_codewords.append(self.ECC.get_ecc(ec_codewords_per_block, "".join(block)))

            interlaced_binary_data = self.Data.interlace_data(block_ecc_codewords, block_codewords)
            binary = "".join(["".join(i) for i in interlaced_binary_data])
        else:

            ecc_code_words = self.ECC.get_ecc(ec_codewords_per_block, binary)
            binary += "".join([format(int(item), 'b').zfill(8) for item in ecc_code_words])

        remainder_bits = ''.zfill(self.Data.get_remainder_bits(version))
        binary += remainder_bits
        self.printer(f'Full Binary Data: {binary}')

        reserve_pixels = []
        module_size = 1
        qr_size = (((int(version) - 1) * 4) + 21)
        self.printer(f'QR Size: {qr_size} x {qr_size}')
        finder_dim = 8

        # first set the grid locations of the first 3 reserve patters
        reserve1x, reserve1y = finder_dim, 0
        [reserve_pixels.append(i) for i in get_coords(reserve1x, reserve1y, get_reserve_1_shape())]

        reserve2x, reserve2y = 0, (qr_size - (finder_dim * 2)) + finder_dim - 1
        [reserve_pixels.append(i) for i in get_coords(reserve2x, reserve2y, get_reserve_2_shape())]

        reserve3x, reserve3y = (qr_size - (finder_dim * 2)) + finder_dim, (qr_size - (finder_dim * 2)) + finder_dim - 1
        [reserve_pixels.append(i) for i in get_coords(reserve3x, reserve3y, get_reserve_3_shape())]

        # now the three finders can be placed
        finder1x, finder1y = 0, qr_size - finder_dim  # the top left finder
        [reserve_pixels.append(i) for i in get_coords(finder1x, finder1y, get_finder_1_shape()) if
         i[0] not in [i[0] for i in reserve_pixels]]

        finder2x, finder2y = qr_size - finder_dim, qr_size - finder_dim  # the top right finder
        [reserve_pixels.append(i) for i in get_coords(finder2x, finder2y, get_finder_2_shape()) if
         i[0] not in [i[0] for i in reserve_pixels]]

        finder3x, finder3y = 0, 0  # the bottom left finder
        [reserve_pixels.append(i) for i in get_coords(finder3x, finder3y, get_finder_3_shape()) if
         i[0] not in [i[0] for i in reserve_pixels]]

        v_reserver_dim = 3
        v_reserve1x, v_reserve1y = ((qr_size - (finder_dim * 2)) + finder_dim) - v_reserver_dim, (
                    (qr_size - (finder_dim * 2)) + finder_dim) + 2
        v_reserve2x, v_reserve2y = 0, finder_dim
        if version >= 7:
            [reserve_pixels.append(i) for i in get_coords(v_reserve1x, v_reserve1y, get_v_reserve_1_shape()) if
             i[0] not in [i[0] for i in reserve_pixels]]
            [reserve_pixels.append(i) for i in get_coords(v_reserve2x, v_reserve2y, get_v_reserve_2_shape()) if
             i[0] not in [i[0] for i in reserve_pixels]]

        # Mark the dark module location
        dark_module_coord = ((4 * version) + 9, finder_dim)
        dark_x, dark_y = (qr_size) - ((dark_module_coord[0])), (dark_module_coord[1]) - 1
        reserve_pixels.append(((dark_x, dark_y), 1))

        # alignment pattern only added if the version is greater than 1
        if version > 1:
            alignment_patterns = get_alignment_placements(version, reserve_pixels, qr_size)

        reserve_pixels = get_timing_coords(qr_size, reserve_pixels)

        data_pixels = self.Data.place_data_codewords(qr_size, binary, reserve_pixels)

        masks = [
            (0, mask_0),
            (1, mask_1),
            (2, mask_2),
            (3, mask_3),
            (4, mask_4),
            (5, mask_5),
            (6, mask_6),
            (7, mask_7)
        ]

        if self.Mask is None:
            #masked_data_0 = mask_0(data_pixels, qr_size)
            #mask_0_penalty = get_penalty(masked_data_0, reserve_pixels, qr_size)
            #masked_data_1 = mask_1(data_pixels, qr_size)
            #mask_1_penalty = get_penalty(masked_data_1, reserve_pixels, qr_size)
            #masked_data_2 = mask_2(data_pixels, qr_size)
            #mask_2_penalty = get_penalty(masked_data_2, reserve_pixels, qr_size)
            #masked_data_3 = mask_3(data_pixels, qr_size)
            #mask_3_penalty = get_penalty(masked_data_3, reserve_pixels, qr_size)
            #masked_data_4 = mask_4(data_pixels, qr_size)
            #mask_4_penalty = get_penalty(masked_data_4, reserve_pixels, qr_size)
            #masked_data_5 = mask_5(data_pixels, qr_size)
            #mask_5_penalty = get_penalty(masked_data_5, reserve_pixels, qr_size)
            #masked_data_6 = mask_6(data_pixels, qr_size)
            #mask_6_penalty = get_penalty(masked_data_6, reserve_pixels, qr_size)
            #masked_data_7 = mask_7(data_pixels, qr_size)
            #mask_7_penalty = get_penalty(masked_data_7, reserve_pixels, qr_size)
            #penalty_list = [
                #(masked_data_0, mask_0_penalty, 0),
                #(masked_data_1, mask_1_penalty, 1),
                #(masked_data_2, mask_2_penalty, 2),
                #(masked_data_3, mask_3_penalty, 3),
                #(masked_data_4, mask_4_penalty, 4),
                #(masked_data_5, mask_5_penalty, 5),
                #(masked_data_6, mask_6_penalty, 6),
                #(masked_data_7, mask_7_penalty, 7)
            #]
            penalty_list = []
            for mask_int, mask_function in masks:
                masked_data = mask_function(data_pixels, qr_size)
                mask_penalty = get_penalty(masked_data, reserve_pixels, qr_size)
                penalty_list.append((masked_data, mask_penalty, mask_int))

            min_penalty = min([i[1] for i in penalty_list])
            self.printer(f'Selected Mask: {[x[2] for x in penalty_list if x[1] == min_penalty][0]}')
            mask_number = format([x[2] for x in penalty_list if x[1] == min_penalty][0], 'b').zfill(3)
            qr_data = [x[0] for x in penalty_list if x[1] == min_penalty][0]
        else:
            selected_mask = [i[1] for i in masks if i[0] == self.Mask][0]
            self.printer(f'Selected Mask: {self.Mask}')
            qr_data = selected_mask(data_pixels, qr_size)
            [qr_data.append(i) for i in reserve_pixels]
            mask_number = format(self.Mask, 'b').zfill(3)

        # Calculate the binary for the format version string or use the list in the ECC script to get it
        error_correction_bits = [('Low', '01', 1), ('Medium', '00', 0), ('Quartile', '11', 3), ('High', '10', 2)]
        format_version = [i[1] for i in error_correction_bits if i[0] == correction_level][0] + mask_number

        ecc_bits = self.ECC.get_format_ecc(10, format_version)
        ecc_format_version = format_version + ecc_bits

        set_xor_string = '101010000010010'  # qr spec xor string for all qr types
        final_string = ''
        bit_index = 0
        for bit in ecc_format_version:
            xor_result = int(bit) ^ int(set_xor_string[bit_index])
            bit_index += 1
            final_string = final_string + str(xor_result)

        updated_reserve = []

        reserve_1_shape = get_reserve_1_shape(binary=final_string[0:6])
        reserve_2_shape = get_reserve_2_shape(binary=final_string)
        reserve_3_shape = get_reserve_3_shape(binary=final_string[7:])

        [updated_reserve.append(i) for i in get_coords(reserve1x, reserve1y, reserve_1_shape)]
        [updated_reserve.append(i) for i in get_coords(reserve2x, reserve2y, reserve_2_shape)]
        [updated_reserve.append(i) for i in get_coords(reserve3x, reserve3y, reserve_3_shape)]

        # generate a version error correction if the version is greater than 7
        if version >= 7:
            version_string = format(int(version), 'b').zfill(6)
            ecc_bits = self.ECC.get_version_ecc(12, version_string)
            ecc_version_string = version_string.zfill(6) + ecc_bits
            r1 = [2, 1, 0,
                  5, 4, 3,
                  8, 7, 6,
                  11, 10, 9,
                  14, 13, 12,
                  17, 16, 15]

            v_reserve_1_shape = get_v_reserve_1_shape(binary=[ecc_version_string[i] for i in r1])
            r2 = [17, 14, 11, 8, 5, 2,
                  16, 13, 10, 7, 4, 1,
                  15, 12, 9, 6, 3, 0]

            v_reserve_2_shape = get_v_reserve_2_shape(binary=[ecc_version_string[i] for i in r2])

            [updated_reserve.append(i) for i in get_coords(v_reserve1x, v_reserve1y, v_reserve_1_shape)]
            [updated_reserve.append(i) for i in get_coords(v_reserve2x, v_reserve2y, v_reserve_2_shape)]

        # update to current coords list with new data
        for coord, state in updated_reserve:
            reserve_coords = [i[0] for i in qr_data]
            if coord in reserve_coords:
                data_index = reserve_coords.index(coord)
                qr_data[data_index] = (coord, state)

        return [qr_data, module_size]

    def write_ps(self, data, file_dir=None):
        qr_data, module_size = data
        write_qr(qr_data, module_size, file_dir)

    def return_ps(self, data, mod_size=False):
        qr_data, module_size = data
        if not mod_size:
            pass
        else:
            module_size = mod_size
        ps_data = return_ps(qr_data, module_size)
        return ps_data

    def make_png(self, data, file_dir):
        qr_data, module_size = data
        create_qr_png(qr_data, file_dir)

    def show_png(self, data):
        qr_data, module_size = data
        display_qr_image(qr_data)

    def printer(self, message):
        if self.PrintData:
            print(message)
        else:
            pass




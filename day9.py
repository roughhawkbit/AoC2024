with open('input.txt', 'r') as f:
    input = f.read().strip()

def disk_map_to_blocks(disk_map):
    blocks = []
    is_block = True
    block_id = 0
    for i, c_char in enumerate(disk_map):
        c_int = int(c_char)
        to_insert = block_id if is_block else None
        for j in range(c_int):
            blocks.append(to_insert)
        if is_block:
            block_id += 1
        is_block = not is_block
    return blocks

def rearrange_blocks(blocks):
    i = 0
    j = len(blocks) - 1
    i = blocks.index(None)
    while (0 <= i < j):
        if blocks[j] is not None:
            blocks[i] = blocks[j]
            blocks[j] = None
            i = blocks.index(None, i + 1)
        j -= 1
    return(blocks)

blocks = disk_map_to_blocks(input)
blocks = rearrange_blocks(blocks)
checksum = sum([i*c for i,c in enumerate(blocks) if c is not None])
print(checksum)

def disk_map_as_blox(input):
    blox = []
    is_block = True
    block_id = 0
    start = 0
    for c in input:
        block_length = int(c)
        blox.append((
            start,
            block_length,
            block_id if is_block else None
        ))
        start += block_length
        if is_block:
            block_id += 1
        is_block = not is_block
    return blox

def rearrange_files(blox):
    n_skipped = 0
    while True:
        # Find the rightmost file that hasn't yet been considered
        file_idxs = [i for i,b in enumerate(blox) if (b[2] is not None) and (i < len(blox)-n_skipped)]
        if len(file_idxs) == 0:
            break
        rm_idx = max(file_idxs)
        # Find the lestmost gap that is long enough
        gap_idxs = [i for i,b in enumerate(blox) if (b[2] is None) and (b[1] >= blox[rm_idx][1]) and (i<rm_idx)]
        # If none exists, move onto the next file
        if len(gap_idxs) == 0:
            n_skipped += 1
            continue
        # If a suitable gap does exist, move the file into it
        lm_idx = min(gap_idxs)
        diff = blox[lm_idx][1] - blox[rm_idx][1]
        blox[lm_idx] = (
            blox[lm_idx][0],
            blox[rm_idx][1],
            blox[rm_idx][2]
        )
        # Add a new, shorter gap if it wasn't a perfect fit
        if diff > 0:
            blox.insert(lm_idx + 1,
                        (blox[lm_idx][0] + blox[rm_idx][1],
                         diff,
                         None)
                         )
            rm_idx += 1
        # Move the gap to where the file was, combining it with any gaps left and/or right (if existing)
        join_left = blox[rm_idx-1][2] is None
        join_right = False if (rm_idx == len(blox)-1) else (blox[rm_idx+1][2] is None)
        new_start = blox[rm_idx-1][0] if join_left else blox[rm_idx][0]
        new_length = blox[rm_idx][1] + (blox[rm_idx-1][1] if join_left else 0) + (blox[rm_idx+1][1] if join_right else 0)
        blox[rm_idx] = (new_start, new_length, None)
        if join_left:
            del blox[rm_idx-1]
            rm_idx -= 1
        if join_right:
            del blox[rm_idx+1]
    return blox

def blok_checksum(blok):
    checksum = 0
    if blok[2] is None:
        return checksum
    for i in range(blok[0], blok[0]+blok[1]):
        checksum += i * blok[2]
    return checksum

blox = disk_map_as_blox(input)
blocks = rearrange_files(blox)
checksum = sum([blok_checksum(blok) for blok in blox])
print(checksum)


# def find_free_space(blocks, start, end=None):
#     if end is None:
#         end = len(blocks)
#     if not None in blocks[start:end]:
#         return -1, -1
#     i0 = blocks.index(None, start, end)
#     i1 = i0
#     while (blocks[i1] is None) and (0 <= i1 <= end):
#         i1 += 1
#     return i0, i1

# def find_file_start(blocks, end):
#     j0 = end - 1
#     while (j0 >= 0) and (blocks[j0] == blocks[end]):
#         j0 -= 1
#     return j0

# def rearrange_files(blocks):
#     # Setup
#     i0, i1 = find_free_space(blocks, 0)
#     j1 = len(blocks) - 1
#     while (blocks[j1] is None) and (j1 >= 0):
#         j1 -= 1
#     j0 = find_file_start(blocks, j1)
#     # Main process
#     while (0 <= i1 < j0):
#         file_length = j1 - j0
#         while (file_length > i1 - i0) and (0 < i1 <= j0):
#             i0, i1 = find_free_space(blocks, i1, end=j0+1)
#         if (file_length <= i1 - i0) and (i0 > 0):
#             for k in range(file_length):
#                 blocks[i0 + k] = blocks[j1 - k]
#                 blocks[j1 - k] = None
#         i0, i1 = find_free_space(blocks, 0)
#         j1 = j0
#         j0 = find_file_start(blocks, j1)
#     return(blocks)


### Part 2


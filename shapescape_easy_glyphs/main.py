from pathlib import Path
from PIL import Image
import json
import os
import sys
import re


def generate_texture():
    glyph = Image.new('RGBA', (tile_scale * col, tile_scale * row))
    glyph.save(font_path / glyph_name)
    return glyph


def load_categories():
    categories = next(os.walk('data/shapescape_easy_glyphs'))[1]
    categories.sort()
    return categories


def paste_icons():
    cur_row = 0
    cur_col = 0
    icon_code_out = {}

    glyph = generate_texture()

    for e in load_categories():
        unicode_list = {}
        # Sort files using numeric prefix from the filename (e.g. "01_", "02_", etc.)
        for file in sorted(Path(texture_directory + '/' + e).glob('**/*.png'),
                           key=lambda f: int(re.match(r'^(\d+)_', f.stem).group(1)) if re.match(r'^(\d+)_', f.stem) else float('inf')):
            cord_x = cur_col * tile_scale
            cord_y = cur_row * tile_scale
            temp_icon = Image.open(str(file))
            if temp_icon.height > tile_scale:
                temp_icon = temp_icon.resize((tile_scale, tile_scale), resample=0)
            if temp_icon.height < tile_scale:
                cord_y += int(tile_scale / 2) - int(temp_icon.height / 2)
            glyph.paste(temp_icon, (cord_x, cord_y))

            unicode_list.update({file.stem: get_uni_code(cur_row, cur_col)})

            if cur_col + 1 != 16:
                cur_col = cur_col + 1
            else:
                cur_row = cur_row + 1
                cur_col = 0
        icon_code_out.update({e[2:]: unicode_list})
        cur_col = 0
        cur_row += 1
    with open('data/shapescape_easy_glyphs/unicodes.json', 'w', encoding='utf8') as f:
        json.dump(icon_code_out, f, indent=4, ensure_ascii=False)
    glyph.save(font_path / glyph_name)


def get_uni_code(cur_row, cur_col):
    uni_x = hex(cur_row).lstrip('0x').rstrip('L')
    uni_y = hex(cur_col).lstrip('0x').rstrip('L')
    if uni_x == '':
        uni_x = 0
    if uni_y == '':
        uni_y = 0
    unicode = '0x' + config["glyph_hex"] + str(uni_x) + str(uni_y)
    unicode = chr(int(unicode, 16))
    return unicode


if __name__ == "__main__":
    # Default config values
    config = {
        "scale": 4,
        "glyph_hex": "E1"
    }
    # User config values
    try:
        config = config | json.loads(sys.argv[1])
    except Exception:
        pass
    # Fixed config values
    config |= {
        "rp_path": Path("RP")
    }
    if "source_file" in config:
        del config["source_file"]

    # non editable variables
    row = 16
    col = 16
    tile_scale = 31 * config["scale"]

    texture_directory = 'data/shapescape_easy_glyphs'

    rp_path = config["rp_path"]
    font_path = rp_path / 'font/'
    glyph_name = 'glyph_' + config["glyph_hex"] + '.png'
    # creating /font directory if it does not exist yet.
    font_path.mkdir(parents=True, exist_ok=True)
    paste_icons()

import colorsys
import os
import shutil

colors = {
    "gruvbox-red-bright": "fb4934",
    "gruvbox-green-bright": "b8bb26",
    "gruvbox-yellow-bright": "fabd2f",
    "gruvbox-blue-bright": "83a598",
    "gruvbox-purple-bright": "d3869b",
    "gruvbox-aqua-bright": "8ec07c",
    "gruvbox-orange-bright": "fe8019",
    "gruvbox-red-neutral": "cc241d",
    "gruvbox-green-neutral": "98971a",
    "gruvbox-yellow-neutral": "d79921",
    "gruvbox-blue-neutral": "458588",
    "gruvbox-purple-neutral": "b16286",
    "gruvbox-aqua-neutral": "689d6a",
    "gruvbox-orange-neutral": "d65d0e",
    "gruvbox-red-faded": "9d0006",
    "gruvbox-green-faded": "79740e",
    "gruvbox-yellow-faded": "b57614",
    "gruvbox-blue-faded": "076678",
    "gruvbox-purple-faded": "8f3f71",
    "gruvbox-aqua-faded": "427b58",
    "gruvbox-orange-faded": "af3a03",
}

for c in colors:
    lightness_reduction = 0.1
    r_hex = int(colors[c][0:2], 16)
    g_hex = int(colors[c][2:4], 16)
    b_hex = int(colors[c][4:6], 16)
    r_norm, g_norm, b_norm = r_hex / 255.0, g_hex / 255.0, b_hex / 255.0
    h, l, s = colorsys.rgb_to_hls(r_norm, g_norm, b_norm)
    new_l = max(0.0, l - lightness_reduction)
    new_r_norm, new_g_norm, new_b_norm = colorsys.hls_to_rgb(h, new_l, s)
    new_r = int(new_r_norm * 255)
    new_g = int(new_g_norm * 255)
    new_b = int(new_b_norm * 255)
    new_hex = f"{new_r:02X}{new_g:02X}{new_b:02X}"

    print(f"Original Hex: {colors[c]}")
    print(f"New Hex (lightness reduced by {lightness_reduction*100}%): {new_hex}")

    color_dir = f"Adwaita-{c}"

    shutil.copytree("Adwaita", color_dir, dirs_exist_ok=True)
    shutil.copy("index.theme", f"{color_dir}/index.theme")

    os.system(f'sed -i "s/Name=Adwaita/Name=Adwaita-{c}/" "{color_dir}/index.theme"')
    os.system(f'sed -i "s/Hidden=true/Hidden=false/" "{color_dir}/index.theme"')

    os.system(f'sed -i "s/#62a0ea/#{colors[c]}/g" {color_dir}/scalable/places/folder*.svg')
    os.system(f'sed -i "s/#afd4ff/#{colors[c]}/g" {color_dir}/scalable/places/folder*.svg')
    os.system(f'sed -i "s/#c0d5ea/#{colors[c]}/g" {color_dir}/scalable/places/folder*.svg')
    os.system(f'sed -i "s/#a4caee/#{colors[c]}/g" {color_dir}/scalable/places/folder*.svg')
    os.system(f'sed -i "s/#438de6/#{new_hex}/g" {color_dir}/scalable/places/folder*.svg')
    os.system(f'sed -i "s/#62a0ea/#{colors[c]}/g" {color_dir}/scalable/places/user*.svg')
    os.system(f'sed -i "s/#afd4ff/#{colors[c]}/g" {color_dir}/scalable/places/user*.svg')
    os.system(f'sed -i "s/#c0d5ea/#{colors[c]}/g" {color_dir}/scalable/places/user*.svg')
    os.system(f'sed -i "s/#a4caee/#{colors[c]}/g" {color_dir}/scalable/places/user*.svg')
    os.system(f'sed -i "s/#438de6/#{new_hex}/g" {color_dir}/scalable/places/user*.svg')

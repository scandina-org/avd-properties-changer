import json

with open('./presets/api_preset.json', 'r') as f:
    preset_list = json.load(f)

converted_list = []

for preset in preset_list:
    converted_preset = {}
    converted_preset['PRESET_NAME'] = preset['PRESET_NAME']
    # converted_preset['ro.product.cpu.abi'] = preset['ABI']
    # converted_preset['ro.product.cpu.abilist'] = preset['ABI']
    # converted_preset['ro.product.cpu.abilist32'] = preset['ABI']
    # converted_preset['ro.product.cpu.abilist64'] = preset['ABI']

    converted_preset['ro.bootloader'] = preset['bootloader']

    converted_preset['ro.product.brand'] = preset['brand']
    converted_preset['ro.product.vendor.brand'] = preset['brand']

    # Not working
    converted_preset['ro.product.board'] = preset['board']

    converted_preset['ro.product.bootimage.device'] = preset['device']
    converted_preset['ro.product.odm.device'] = preset['device']
    converted_preset['ro.product.product.device'] = preset['device']
    converted_preset['ro.product.system_ext.device'] = preset['device']
    converted_preset['ro.product.vendor.device'] = preset['device']
    converted_preset['ro.product.device'] = preset['device']
    converted_preset['ro.product.vendor.device'] = preset['device']
    converted_preset['ro.build.product'] = preset['device']
    converted_preset['ro.product.vendor_dlkm.device'] = preset['device']

    converted_preset['ro.build.display.id'] = preset['display']

    converted_preset['ro.bootimage.build.fingerprint'] = preset['fingerprint']
    converted_preset['ro.build.fingerprint'] = preset['fingerprint']
    converted_preset['ro.system.build.fingerprint'] = preset['fingerprint']
    converted_preset['ro.product.build.fingerprint'] = preset['fingerprint']
    converted_preset['ro.odm.build.fingerprint'] = preset['fingerprint']
    converted_preset['ro.system_ext.build.fingerprint'] = preset['fingerprint']
    converted_preset['ro.vendor.build.fingerprint'] = preset['fingerprint']

    converted_preset['ro.bootimage.build.tags'] = preset['tags']
    converted_preset['ro.build.tags'] = preset['tags']
    converted_preset['ro.system.build.tags'] = preset['tags']
    converted_preset['ro.product.build.tags'] = preset['tags']
    converted_preset['ro.system_ext.build.tags'] = preset['tags']
    converted_preset['ro.vendor.build.tags'] = preset['tags']
    converted_preset['ro.vendor_dlkm.build.tags'] = preset['tags']

    converted_preset['ro.bootimage.build.type'] = preset['type']
    converted_preset['ro.build.type'] = preset['type']
    converted_preset['ro.system.build.type'] = preset['type']
    converted_preset['ro.product.build.type'] = preset['type']
    converted_preset['ro.system_ext.build.type'] = preset['type']
    converted_preset['ro.vendor.build.type'] = preset['type']
    converted_preset['ro.vendor_dlkm.build.type'] = preset['type']

    converted_preset['ro.product.model'] = preset['model']
    converted_preset['ro.product.odm.model'] = preset['model']
    converted_preset['ro.product.product.model'] = preset['model']
    converted_preset['ro.product.system_ext.model'] = preset['model']
    converted_preset['ro.product.vendor.model'] = preset['model']
    converted_preset['ro.product.vendor_dlkm.model'] = preset['model']

    converted_preset['ro.product.name'] = preset['product']
    converted_preset['ro.product.odm.name'] = preset['product']
    converted_preset['ro.product.product.name'] = preset['product']
    converted_preset['ro.product.system_ext.name'] = preset['product']
    converted_preset['ro.product.vendor.name'] = preset['product']
    converted_preset['ro.product.vendor_dlkm.name'] = preset['product']

    converted_preset['ro.boot.hardware'] = preset['hardware']
    converted_preset['ro.hardware'] = preset['hardware']
    converted_preset['ro.hardware.power'] = preset['hardware']
    converted_preset['ro.kernel.androidboot.hardware'] = preset['hardware']
    converted_preset['ro.soc.model'] = preset['hardware']

    converted_preset['ro.kernel.qemu'] = 0

    converted_list.append(converted_preset)

with open('./presets/system_preset.json', 'w') as f:
    json.dump(converted_list, f, indent='\t')
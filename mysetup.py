# build_windows.py
from py2exe import freeze

freeze(
    console=['screen_alive.py'],           # or windows=['your_gui_script.py']
    data_files=None,                       # to include extra files
    zipfile=None,                          # embed the library.zip
    options={'py2exe': {'bundle_files': 1, 'compressed': True}},
    version_info={'version': '1.0.0', 'product_name': 'MyApp'},
)

# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['envi.py'],
             pathex=['C:\\Users\\Hieu\\Desktop\\MyWorkPlace\\Ultimate\\translate'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries + [('envi.ico', 'C:\\Users\\Hieu\\Desktop\\MyWorkPlace\\Ultimate\\translate\\envi.ico', 'DATA')],
          a.zipfiles,
          a.datas,
          [],
          name='envi',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='favicon.ico')

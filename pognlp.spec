# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['pognlp/pognlp.py'],
             pathex=['/home/evan/git/reddit-nlp'],
             binaries=[],
             datas=[],
             hiddenimports=[
                    'srsly.msgpack.util',
                    'cymem.cymem',
                    'murmurhash.mrmr',
                    'cytoolz.utils',
                    'cytoolz._signatures',
                    'spacy.strings',
                    'spacy.morphology',
                    'spacy.lexeme',
                    'spacy.tokens.underscore',
                    'preshed.maps',
                    'thinc.backends.linalg',
                    'blis',
             ],
             hookspath=['pyinstaller-hooks/'],
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
          [],
          exclude_binaries=True,
          name='pognlp',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='pognlp')

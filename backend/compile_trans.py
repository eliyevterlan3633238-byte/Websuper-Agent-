import polib
import os

ru_po_path = r'c:\Users\Terlan\OneDrive\Desktop\sayt2\backend\locale\ru\LC_MESSAGES\django.po'
ru_mo_path = r'c:\Users\Terlan\OneDrive\Desktop\sayt2\backend\locale\ru\LC_MESSAGES\django.mo'

en_po_path = r'c:\Users\Terlan\OneDrive\Desktop\sayt2\backend\locale\en\LC_MESSAGES\django.po'
en_mo_path = r'c:\Users\Terlan\OneDrive\Desktop\sayt2\backend\locale\en\LC_MESSAGES\django.mo'

def compile_po(po_path, mo_path):
    if os.path.exists(po_path):
        po = polib.pofile(po_path)
        po.save_as_mofile(mo_path)
        print(f"Compiled {po_path} to {mo_path}")

compile_po(ru_po_path, ru_mo_path)
compile_po(en_po_path, en_mo_path)

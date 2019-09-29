from cx_Freeze import setup, Executable

setup(
    name="LabyrintheAuto",
    version="1.0",
    description="génération de labyrinthe aléatoire de taille variable",
    executables=[Executable("Labyrinthe.py")],
    options={'build_exe': {'include_files': ["Case.py", "Traducteur.py"]}},
)

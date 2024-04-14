import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from model.SpecialTokenManipulator import SpecialTokenManipulator
from model.StringReader import StringReader


print(SpecialTokenManipulator.show_answers((StringReader.clean_text(open("./text_files/teste.txt", "r", encoding="utf8")))))
from argparse import Namespace
import main
from mock import patch
import unittest


class Tre(unittest.TestCase):
    @patch.object(main, 'parse_args')
    def test_validFiles(self,test_combineFiles):
        test_combineFiles.return_value = Namespace(name=['/csvfiles/accessories_test.csv', '/csvfiles/clothing_test.csv'])
        tmp = main.CombineCSV()
        tmp.combineFiles()

    @patch.object(main, 'parse_args')
    def test_filenotfound(self,test_combineFilesfnf):
        test_combineFilesfnf.return_value = Namespace(name=['/csvfiles/access.csv', '/csvfiles/clothing.csv'])
        tmp = main.CombineCSV()
        with self.assertRaises(Exception): tmp.combineFiles()

    @patch.object(main, 'parse_args')
    def test_notvalidformat(self,test_combineFilesnotcsv):
        test_combineFilesnotcsv.return_value = Namespace(name=['/csvfiles/sample.txt', '/csvfiles/clothing.csv'])
        tmp = main.CombineCSV()
        with self.assertRaises(Exception): tmp.combineFiles()

    @patch.object(main, 'parse_args')
    def test_notsamecolumns(self,test_combineFilesdifcols):
        test_combineFilesdifcols.return_value = Namespace(name=['/csvfiles/acc.csv', '/csvfiles/clothing.csv'])
        tmp = main.CombineCSV()
        with self.assertRaises(Exception): tmp.combineFiles()


if __name__ == "__main__":
    unittest.main()





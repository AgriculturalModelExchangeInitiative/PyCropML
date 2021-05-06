# Generated from javalib\gram\CSharpParser.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\u00c7")
        buf.write("\u0a50\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\tL\4M\t")
        buf.write("M\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\tU\4V\t")
        buf.write("V\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4^\t^\4")
        buf.write("_\t_\4`\t`\4a\ta\4b\tb\4c\tc\4d\td\4e\te\4f\tf\4g\tg\4")
        buf.write("h\th\4i\ti\4j\tj\4k\tk\4l\tl\4m\tm\4n\tn\4o\to\4p\tp\4")
        buf.write("q\tq\4r\tr\4s\ts\4t\tt\4u\tu\4v\tv\4w\tw\4x\tx\4y\ty\4")
        buf.write("z\tz\4{\t{\4|\t|\4}\t}\4~\t~\4\177\t\177\4\u0080\t\u0080")
        buf.write("\4\u0081\t\u0081\4\u0082\t\u0082\4\u0083\t\u0083\4\u0084")
        buf.write("\t\u0084\4\u0085\t\u0085\4\u0086\t\u0086\4\u0087\t\u0087")
        buf.write("\4\u0088\t\u0088\4\u0089\t\u0089\4\u008a\t\u008a\4\u008b")
        buf.write("\t\u008b\4\u008c\t\u008c\4\u008d\t\u008d\4\u008e\t\u008e")
        buf.write("\4\u008f\t\u008f\4\u0090\t\u0090\4\u0091\t\u0091\4\u0092")
        buf.write("\t\u0092\4\u0093\t\u0093\4\u0094\t\u0094\4\u0095\t\u0095")
        buf.write("\4\u0096\t\u0096\4\u0097\t\u0097\4\u0098\t\u0098\4\u0099")
        buf.write("\t\u0099\4\u009a\t\u009a\4\u009b\t\u009b\4\u009c\t\u009c")
        buf.write("\4\u009d\t\u009d\4\u009e\t\u009e\4\u009f\t\u009f\4\u00a0")
        buf.write("\t\u00a0\4\u00a1\t\u00a1\4\u00a2\t\u00a2\4\u00a3\t\u00a3")
        buf.write("\4\u00a4\t\u00a4\4\u00a5\t\u00a5\4\u00a6\t\u00a6\4\u00a7")
        buf.write("\t\u00a7\4\u00a8\t\u00a8\4\u00a9\t\u00a9\4\u00aa\t\u00aa")
        buf.write("\4\u00ab\t\u00ab\4\u00ac\t\u00ac\4\u00ad\t\u00ad\4\u00ae")
        buf.write("\t\u00ae\4\u00af\t\u00af\4\u00b0\t\u00b0\4\u00b1\t\u00b1")
        buf.write("\4\u00b2\t\u00b2\4\u00b3\t\u00b3\4\u00b4\t\u00b4\4\u00b5")
        buf.write("\t\u00b5\4\u00b6\t\u00b6\4\u00b7\t\u00b7\4\u00b8\t\u00b8")
        buf.write("\4\u00b9\t\u00b9\4\u00ba\t\u00ba\4\u00bb\t\u00bb\4\u00bc")
        buf.write("\t\u00bc\4\u00bd\t\u00bd\4\u00be\t\u00be\4\u00bf\t\u00bf")
        buf.write("\4\u00c0\t\u00c0\4\u00c1\t\u00c1\4\u00c2\t\u00c2\4\u00c3")
        buf.write("\t\u00c3\4\u00c4\t\u00c4\4\u00c5\t\u00c5\4\u00c6\t\u00c6")
        buf.write("\4\u00c7\t\u00c7\4\u00c8\t\u00c8\4\u00c9\t\u00c9\4\u00ca")
        buf.write("\t\u00ca\4\u00cb\t\u00cb\4\u00cc\t\u00cc\4\u00cd\t\u00cd")
        buf.write("\4\u00ce\t\u00ce\4\u00cf\t\u00cf\4\u00d0\t\u00d0\4\u00d1")
        buf.write("\t\u00d1\4\u00d2\t\u00d2\4\u00d3\t\u00d3\4\u00d4\t\u00d4")
        buf.write("\4\u00d5\t\u00d5\4\u00d6\t\u00d6\4\u00d7\t\u00d7\4\u00d8")
        buf.write("\t\u00d8\4\u00d9\t\u00d9\4\u00da\t\u00da\4\u00db\t\u00db")
        buf.write("\3\2\5\2\u01b8\n\2\3\2\5\2\u01bb\n\2\3\2\5\2\u01be\n\2")
        buf.write("\3\2\7\2\u01c1\n\2\f\2\16\2\u01c4\13\2\3\2\5\2\u01c7\n")
        buf.write("\2\3\2\3\2\3\3\3\3\5\3\u01cd\n\3\3\3\5\3\u01d0\n\3\3\3")
        buf.write("\3\3\3\3\5\3\u01d5\n\3\7\3\u01d7\n\3\f\3\16\3\u01da\13")
        buf.write("\3\3\4\3\4\3\4\3\4\7\4\u01e0\n\4\f\4\16\4\u01e3\13\4\3")
        buf.write("\5\3\5\3\5\3\5\3\5\5\5\u01ea\n\5\3\6\3\6\3\6\3\6\6\6\u01f0")
        buf.write("\n\6\r\6\16\6\u01f1\3\6\3\6\3\7\3\7\5\7\u01f8\n\7\3\b")
        buf.write("\3\b\5\b\u01fc\n\b\3\t\3\t\3\t\5\t\u0201\n\t\3\n\3\n\3")
        buf.write("\13\3\13\3\f\3\f\3\f\3\f\5\f\u020b\n\f\3\r\3\r\3\r\3\r")
        buf.write("\7\r\u0211\n\r\f\r\16\r\u0214\13\r\3\r\3\r\3\16\3\16\3")
        buf.write("\16\7\16\u021b\n\16\f\16\16\16\u021e\13\16\3\17\3\17\3")
        buf.write("\17\5\17\u0223\n\17\3\17\5\17\u0226\n\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\5\20\u022e\n\20\3\21\3\21\3\21\5\21\u0233")
        buf.write("\n\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u023d")
        buf.write("\n\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\5\23\u024a\n\23\3\24\3\24\3\24\3\24\3\24\3\24\5")
        buf.write("\24\u0252\n\24\3\25\3\25\3\25\3\25\5\25\u0258\n\25\5\25")
        buf.write("\u025a\n\25\3\26\3\26\3\26\7\26\u025f\n\26\f\26\16\26")
        buf.write("\u0262\13\26\3\27\3\27\3\27\7\27\u0267\n\27\f\27\16\27")
        buf.write("\u026a\13\27\3\30\3\30\3\30\7\30\u026f\n\30\f\30\16\30")
        buf.write("\u0272\13\30\3\31\3\31\3\31\7\31\u0277\n\31\f\31\16\31")
        buf.write("\u027a\13\31\3\32\3\32\3\32\7\32\u027f\n\32\f\32\16\32")
        buf.write("\u0282\13\32\3\33\3\33\3\33\7\33\u0287\n\33\f\33\16\33")
        buf.write("\u028a\13\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\7\34\u0293")
        buf.write("\n\34\f\34\16\34\u0296\13\34\3\35\3\35\3\35\5\35\u029b")
        buf.write("\n\35\3\35\7\35\u029e\n\35\f\35\16\35\u02a1\13\35\3\36")
        buf.write("\3\36\3\36\7\36\u02a6\n\36\f\36\16\36\u02a9\13\36\3\37")
        buf.write("\3\37\3\37\7\37\u02ae\n\37\f\37\16\37\u02b1\13\37\3 \3")
        buf.write(" \3 \3 \3 \5 \u02b8\n \5 \u02ba\n \3 \5 \u02bd\n \3!\3")
        buf.write("!\3!\7!\u02c2\n!\f!\16!\u02c5\13!\3\"\3\"\5\"\u02c9\n")
        buf.write("\"\3\"\3\"\3\"\3#\3#\5#\u02d0\n#\3#\3#\5#\u02d4\n#\5#")
        buf.write("\u02d6\n#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3")
        buf.write("$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\5$\u02f2\n$\3%\3%\5")
        buf.write("%\u02f6\n%\3%\7%\u02f9\n%\f%\16%\u02fc\13%\3%\5%\u02ff")
        buf.write("\n%\3%\3%\3%\3%\3%\3%\5%\u0307\n%\3%\5%\u030a\n%\3%\7")
        buf.write("%\u030d\n%\f%\16%\u0310\13%\3%\5%\u0313\n%\7%\u0315\n")
        buf.write("%\f%\16%\u0318\13%\3&\3&\3&\5&\u031d\n&\3&\3&\3&\3&\3")
        buf.write("&\3&\3&\3&\3&\3&\3&\3&\5&\u032b\n&\3&\3&\3&\3&\5&\u0331")
        buf.write("\n&\3&\3&\3&\3&\3&\3&\3&\3&\7&\u033b\n&\f&\16&\u033e\13")
        buf.write("&\3&\5&\u0341\n&\3&\6&\u0344\n&\r&\16&\u0345\3&\3&\5&")
        buf.write("\u034a\n&\3&\3&\3&\3&\5&\u0350\n&\3&\3&\3&\3&\6&\u0356")
        buf.write("\n&\r&\16&\u0357\3&\3&\3&\3&\3&\3&\3&\5&\u0361\n&\3&\3")
        buf.write("&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\5&\u0373\n")
        buf.write("&\3&\5&\u0376\n&\3&\3&\3&\5&\u037b\n&\3&\5&\u037e\n&\3")
        buf.write("&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\7&\u038b\n&\f&\16&\u038e")
        buf.write("\13&\3&\3&\3&\5&\u0393\n&\3\'\3\'\5\'\u0397\n\'\3(\3(")
        buf.write("\3(\3)\5)\u039d\n)\3)\3)\3)\5)\u03a2\n)\3*\5*\u03a5\n")
        buf.write("*\3*\3*\3*\3*\7*\u03ab\n*\f*\16*\u03ae\13*\3*\3*\3+\3")
        buf.write("+\3+\5+\u03b5\n+\3+\3+\3,\3,\3-\3-\3-\7-\u03be\n-\f-\16")
        buf.write("-\u03c1\13-\3.\3.\5.\u03c5\n.\3/\3/\3/\5/\u03ca\n/\5/")
        buf.write("\u03cc\n/\3/\3/\3\60\3\60\3\60\7\60\u03d3\n\60\f\60\16")
        buf.write("\60\u03d6\13\60\3\61\3\61\3\61\3\61\3\61\5\61\u03dd\n")
        buf.write("\61\3\61\3\61\3\61\3\62\3\62\5\62\u03e4\n\62\3\63\3\63")
        buf.write("\3\63\3\63\7\63\u03ea\n\63\f\63\16\63\u03ed\13\63\3\63")
        buf.write("\5\63\u03f0\n\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\5")
        buf.write("\64\u03f9\n\64\3\65\3\65\3\65\5\65\u03fe\n\65\5\65\u0400")
        buf.write("\n\65\3\65\3\65\3\66\3\66\3\66\7\66\u0407\n\66\f\66\16")
        buf.write("\66\u040a\13\66\3\67\3\67\3\67\3\67\3\67\5\67\u0411\n")
        buf.write("\67\38\38\58\u0415\n8\38\38\38\58\u041a\n8\58\u041c\n")
        buf.write("8\38\38\38\58\u0421\n8\78\u0423\n8\f8\168\u0426\138\3")
        buf.write("9\39\79\u042a\n9\f9\169\u042d\139\39\39\3:\3:\3:\7:\u0434")
        buf.write("\n:\f:\16:\u0437\13:\3:\5:\u043a\n:\3:\5:\u043d\n:\3:")
        buf.write("\5:\u0440\n:\3;\3;\3;\3;\7;\u0446\n;\f;\16;\u0449\13;")
        buf.write("\3;\3;\3<\3<\3<\3<\3=\5=\u0452\n=\3=\3=\3=\3=\3>\3>\3")
        buf.write(">\3>\3>\3>\3>\3>\3>\3>\3>\5>\u0463\n>\3?\3?\3?\7?\u0468")
        buf.write("\n?\f?\16?\u046b\13?\3@\5@\u046e\n@\3@\3@\3@\3A\3A\3A")
        buf.write("\7A\u0476\nA\fA\16A\u0479\13A\3B\3B\5B\u047d\nB\3C\3C")
        buf.write("\3C\3D\3D\5D\u0484\nD\3D\3D\3D\3D\3E\7E\u048b\nE\fE\16")
        buf.write("E\u048e\13E\3E\3E\5E\u0492\nE\3F\3F\3F\3F\3F\5F\u0499")
        buf.write("\nF\3G\3G\3G\3G\3G\3H\3H\3H\3I\3I\5I\u04a5\nI\3I\3I\3")
        buf.write("I\3I\3I\3I\3I\3I\3I\5I\u04b0\nI\3J\3J\3J\3J\7J\u04b6\n")
        buf.write("J\fJ\16J\u04b9\13J\3K\3K\5K\u04bd\nK\3L\3L\3L\3L\3L\3")
        buf.write("L\3L\5L\u04c6\nL\3M\3M\3M\3M\3N\3N\3N\5N\u04cf\nN\3O\3")
        buf.write("O\3O\3O\3O\3O\3O\5O\u04d8\nO\3P\3P\3P\3Q\5Q\u04de\nQ\3")
        buf.write("Q\3Q\3Q\5Q\u04e3\nQ\3Q\3Q\5Q\u04e7\nQ\3Q\3Q\5Q\u04eb\n")
        buf.write("Q\3R\3R\5R\u04ef\nR\3R\3R\5R\u04f3\nR\3S\3S\3S\3S\3S\5")
        buf.write("S\u04fa\nS\3T\3T\3T\3T\3U\3U\5U\u0502\nU\3V\3V\3V\3V\3")
        buf.write("V\3V\3V\3V\3V\3V\3V\5V\u050f\nV\3V\3V\3V\3V\3V\3V\7V\u0517")
        buf.write("\nV\fV\16V\u051a\13V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V")
        buf.write("\3V\3V\3V\3V\3V\3V\3V\3V\5V\u052f\nV\3V\3V\5V\u0533\n")
        buf.write("V\3V\3V\5V\u0537\nV\3V\3V\3V\5V\u053c\nV\3V\3V\3V\3V\3")
        buf.write("V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\5V\u0550\nV\3")
        buf.write("V\3V\3V\5V\u0555\nV\3V\3V\3V\5V\u055a\nV\3V\3V\3V\3V\3")
        buf.write("V\5V\u0561\nV\3V\5V\u0564\nV\3V\3V\3V\3V\3V\3V\3V\3V\3")
        buf.write("V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\5V\u057a\nV\3V\3V\3")
        buf.write("V\3V\3V\3V\3V\3V\3V\3V\5V\u0586\nV\3W\3W\5W\u058a\nW\3")
        buf.write("W\3W\3X\3X\3X\3X\5X\u0592\nX\3X\3X\3X\3X\7X\u0598\nX\f")
        buf.write("X\16X\u059b\13X\3X\3X\3X\3X\5X\u05a1\nX\3Y\3Y\5Y\u05a5")
        buf.write("\nY\3Z\3Z\3Z\5Z\u05aa\nZ\3Z\5Z\u05ad\nZ\3[\3[\3[\5[\u05b2")
        buf.write("\n[\3\\\3\\\3\\\3\\\3]\3]\5]\u05ba\n]\3^\6^\u05bd\n^\r")
        buf.write("^\16^\u05be\3^\3^\3_\3_\3_\5_\u05c6\n_\3_\3_\3_\3_\5_")
        buf.write("\u05cc\n_\3`\3`\3`\3a\6a\u05d2\na\ra\16a\u05d3\3b\3b\3")
        buf.write("b\3b\7b\u05da\nb\fb\16b\u05dd\13b\5b\u05df\nb\3c\3c\3")
        buf.write("c\7c\u05e4\nc\fc\16c\u05e7\13c\3d\3d\7d\u05eb\nd\fd\16")
        buf.write("d\u05ee\13d\3d\5d\u05f1\nd\3d\5d\u05f4\nd\3e\3e\3e\3e")
        buf.write("\5e\u05fa\ne\3e\3e\5e\u05fe\ne\3e\3e\3f\3f\5f\u0604\n")
        buf.write("f\3f\3f\3g\3g\3g\3g\3g\3h\3h\3h\3i\3i\5i\u0612\ni\3j\3")
        buf.write("j\3j\3j\5j\u0618\nj\3k\3k\3k\7k\u061d\nk\fk\16k\u0620")
        buf.write("\13k\3l\3l\5l\u0624\nl\3l\5l\u0627\nl\3l\5l\u062a\nl\3")
        buf.write("l\3l\3m\6m\u062f\nm\rm\16m\u0630\3n\3n\3n\3n\3n\3o\6o")
        buf.write("\u0639\no\ro\16o\u063a\3p\3p\3p\3p\3p\3p\3p\3p\3p\3p\3")
        buf.write("p\3p\3p\3p\3p\5p\u064c\np\3q\6q\u064f\nq\rq\16q\u0650")
        buf.write("\3r\3r\5r\u0655\nr\3s\5s\u0658\ns\3s\5s\u065b\ns\3s\3")
        buf.write("s\3s\3s\3s\5s\u0662\ns\3t\3t\3t\3t\5t\u0668\nt\3u\3u\3")
        buf.write("u\3u\7u\u066e\nu\fu\16u\u0671\13u\3u\3u\3v\5v\u0676\n")
        buf.write("v\3v\3v\3w\3w\3w\3w\7w\u067e\nw\fw\16w\u0681\13w\3x\3")
        buf.write("x\3x\7x\u0686\nx\fx\16x\u0689\13x\3y\6y\u068c\ny\ry\16")
        buf.write("y\u068d\3z\3z\3z\3z\3z\3{\3{\3{\3{\5{\u0699\n{\3{\3{\5")
        buf.write("{\u069d\n{\5{\u069f\n{\3|\3|\3|\5|\u06a4\n|\3|\3|\5|\u06a8")
        buf.write("\n|\3}\3}\3}\7}\u06ad\n}\f}\16}\u06b0\13}\3~\3~\3~\3~")
        buf.write("\3\177\3\177\5\177\u06b8\n\177\3\177\3\177\3\u0080\6\u0080")
        buf.write("\u06bd\n\u0080\r\u0080\16\u0080\u06be\3\u0081\5\u0081")
        buf.write("\u06c2\n\u0081\3\u0081\5\u0081\u06c5\n\u0081\3\u0081\3")
        buf.write("\u0081\5\u0081\u06c9\n\u0081\3\u0082\6\u0082\u06cc\n\u0082")
        buf.write("\r\u0082\16\u0082\u06cd\3\u0083\3\u0083\3\u0084\3\u0084")
        buf.write("\3\u0084\3\u0084\3\u0084\3\u0084\3\u0084\3\u0084\3\u0084")
        buf.write("\5\u0084\u06db\n\u0084\3\u0084\3\u0084\3\u0084\3\u0084")
        buf.write("\3\u0084\3\u0084\3\u0084\3\u0084\5\u0084\u06e5\n\u0084")
        buf.write("\3\u0085\3\u0085\3\u0085\3\u0085\3\u0085\5\u0085\u06ec")
        buf.write("\n\u0085\3\u0085\3\u0085\3\u0085\3\u0085\3\u0085\3\u0085")
        buf.write("\3\u0085\3\u0085\3\u0085\3\u0085\5\u0085\u06f8\n\u0085")
        buf.write("\3\u0086\3\u0086\3\u0086\7\u0086\u06fd\n\u0086\f\u0086")
        buf.write("\16\u0086\u0700\13\u0086\3\u0087\3\u0087\3\u0087\3\u0087")
        buf.write("\3\u0088\3\u0088\3\u0088\7\u0088\u0709\n\u0088\f\u0088")
        buf.write("\16\u0088\u070c\13\u0088\3\u0089\3\u0089\3\u0089\5\u0089")
        buf.write("\u0711\n\u0089\3\u008a\3\u008a\5\u008a\u0715\n\u008a\3")
        buf.write("\u008b\3\u008b\5\u008b\u0719\n\u008b\3\u008c\3\u008c\3")
        buf.write("\u008d\3\u008d\5\u008d\u071f\n\u008d\3\u008e\3\u008e\3")
        buf.write("\u008e\3\u008e\5\u008e\u0725\n\u008e\5\u008e\u0727\n\u008e")
        buf.write("\3\u008f\3\u008f\3\u008f\7\u008f\u072c\n\u008f\f\u008f")
        buf.write("\16\u008f\u072f\13\u008f\3\u0090\5\u0090\u0732\n\u0090")
        buf.write("\3\u0090\5\u0090\u0735\n\u0090\3\u0090\3\u0090\5\u0090")
        buf.write("\u0739\n\u0090\3\u0091\3\u0091\3\u0091\3\u0091\3\u0091")
        buf.write("\3\u0091\3\u0091\3\u0091\5\u0091\u0743\n\u0091\3\u0092")
        buf.write("\5\u0092\u0746\n\u0092\3\u0092\3\u0092\3\u0092\3\u0092")
        buf.write("\3\u0093\5\u0093\u074d\n\u0093\3\u0093\5\u0093\u0750\n")
        buf.write("\u0093\3\u0093\3\u0093\3\u0093\5\u0093\u0755\n\u0093\3")
        buf.write("\u0093\3\u0093\3\u0093\5\u0093\u075a\n\u0093\5\u0093\u075c")
        buf.write("\n\u0093\3\u0094\5\u0094\u075f\n\u0094\3\u0094\5\u0094")
        buf.write("\u0762\n\u0094\3\u0094\3\u0094\3\u0094\3\u0095\5\u0095")
        buf.write("\u0768\n\u0095\3\u0095\5\u0095\u076b\n\u0095\3\u0095\3")
        buf.write("\u0095\3\u0095\3\u0096\3\u0096\3\u0096\3\u0096\3\u0096")
        buf.write("\3\u0096\3\u0096\5\u0096\u0777\n\u0096\3\u0097\3\u0097")
        buf.write("\5\u0097\u077b\n\u0097\3\u0098\5\u0098\u077e\n\u0098\3")
        buf.write("\u0098\3\u0098\3\u0098\3\u0098\3\u0098\3\u0098\3\u0098")
        buf.write("\3\u0098\5\u0098\u0788\n\u0098\3\u0099\5\u0099\u078b\n")
        buf.write("\u0099\3\u0099\3\u0099\3\u0099\3\u009a\5\u009a\u0791\n")
        buf.write("\u009a\3\u009a\3\u009a\3\u009a\3\u009b\3\u009b\3\u009b")
        buf.write("\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b")
        buf.write("\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b")
        buf.write("\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b\5\u009b\u07ac")
        buf.write("\n\u009b\3\u009c\3\u009c\3\u009c\3\u009c\3\u009c\3\u009c")
        buf.write("\3\u009c\3\u009d\3\u009d\3\u009d\3\u009d\5\u009d\u07b9")
        buf.write("\n\u009d\3\u009d\3\u009d\3\u009e\3\u009e\5\u009e\u07bf")
        buf.write("\n\u009e\3\u009f\3\u009f\3\u009f\3\u00a0\3\u00a0\7\u00a0")
        buf.write("\u07c6\n\u00a0\f\u00a0\16\u00a0\u07c9\13\u00a0\3\u00a0")
        buf.write("\3\u00a0\3\u00a1\5\u00a1\u07ce\n\u00a1\3\u00a1\5\u00a1")
        buf.write("\u07d1\n\u00a1\3\u00a1\3\u00a1\3\u00a1\3\u00a1\6\u00a1")
        buf.write("\u07d7\n\u00a1\r\u00a1\16\u00a1\u07d8\3\u00a1\3\u00a1")
        buf.write("\5\u00a1\u07dd\n\u00a1\3\u00a2\3\u00a2\7\u00a2\u07e1\n")
        buf.write("\u00a2\f\u00a2\16\u00a2\u07e4\13\u00a2\3\u00a2\6\u00a2")
        buf.write("\u07e7\n\u00a2\r\u00a2\16\u00a2\u07e8\3\u00a3\3\u00a3")
        buf.write("\7\u00a3\u07ed\n\u00a3\f\u00a3\16\u00a3\u07f0\13\u00a3")
        buf.write("\3\u00a3\3\u00a3\3\u00a4\3\u00a4\3\u00a4\3\u00a4\7\u00a4")
        buf.write("\u07f8\n\u00a4\f\u00a4\16\u00a4\u07fb\13\u00a4\3\u00a4")
        buf.write("\5\u00a4\u07fe\n\u00a4\5\u00a4\u0800\n\u00a4\3\u00a4\3")
        buf.write("\u00a4\3\u00a5\3\u00a5\3\u00a5\3\u00a5\7\u00a5\u0808\n")
        buf.write("\u00a5\f\u00a5\16\u00a5\u080b\13\u00a5\3\u00a5\3\u00a5")
        buf.write("\3\u00a6\5\u00a6\u0810\n\u00a6\3\u00a6\5\u00a6\u0813\n")
        buf.write("\u00a6\3\u00a6\3\u00a6\3\u00a7\3\u00a7\3\u00a8\3\u00a8")
        buf.write("\3\u00a8\3\u00a9\3\u00a9\7\u00a9\u081e\n\u00a9\f\u00a9")
        buf.write("\16\u00a9\u0821\13\u00a9\3\u00a9\3\u00a9\3\u00aa\5\u00aa")
        buf.write("\u0826\n\u00aa\3\u00aa\5\u00aa\u0829\n\u00aa\3\u00aa\5")
        buf.write("\u00aa\u082c\n\u00aa\3\u00aa\3\u00aa\3\u00aa\3\u00aa\3")
        buf.write("\u00aa\5\u00aa\u0833\n\u00aa\3\u00aa\3\u00aa\3\u00aa\5")
        buf.write("\u00aa\u0838\n\u00aa\3\u00aa\3\u00aa\5\u00aa\u083c\n\u00aa")
        buf.write("\3\u00aa\3\u00aa\5\u00aa\u0840\n\u00aa\3\u00aa\3\u00aa")
        buf.write("\3\u00aa\3\u00aa\3\u00aa\3\u00aa\3\u00aa\3\u00aa\3\u00aa")
        buf.write("\3\u00aa\3\u00aa\3\u00aa\3\u00aa\3\u00aa\3\u00aa\5\u00aa")
        buf.write("\u0851\n\u00aa\3\u00aa\5\u00aa\u0854\n\u00aa\3\u00aa\3")
        buf.write("\u00aa\3\u00aa\5\u00aa\u0859\n\u00aa\3\u00aa\3\u00aa\5")
        buf.write("\u00aa\u085d\n\u00aa\3\u00aa\3\u00aa\5\u00aa\u0861\n\u00aa")
        buf.write("\3\u00aa\3\u00aa\3\u00aa\3\u00aa\3\u00aa\3\u00aa\3\u00aa")
        buf.write("\5\u00aa\u086a\n\u00aa\3\u00ab\5\u00ab\u086d\n\u00ab\3")
        buf.write("\u00ab\3\u00ab\3\u00ab\5\u00ab\u0872\n\u00ab\3\u00ab\3")
        buf.write("\u00ab\5\u00ab\u0876\n\u00ab\3\u00ab\3\u00ab\3\u00ab\5")
        buf.write("\u00ab\u087b\n\u00ab\3\u00ab\3\u00ab\5\u00ab\u087f\n\u00ab")
        buf.write("\5\u00ab\u0881\n\u00ab\3\u00ac\3\u00ac\3\u00ac\3\u00ad")
        buf.write("\3\u00ad\3\u00ad\3\u00ad\7\u00ad\u088a\n\u00ad\f\u00ad")
        buf.write("\16\u00ad\u088d\13\u00ad\3\u00ad\5\u00ad\u0890\n\u00ad")
        buf.write("\5\u00ad\u0892\n\u00ad\3\u00ad\3\u00ad\3\u00ae\5\u00ae")
        buf.write("\u0897\n\u00ae\3\u00ae\3\u00ae\3\u00ae\5\u00ae\u089c\n")
        buf.write("\u00ae\3\u00af\3\u00af\3\u00af\3\u00af\3\u00af\5\u00af")
        buf.write("\u08a3\n\u00af\3\u00af\3\u00af\3\u00b0\3\u00b0\5\u00b0")
        buf.write("\u08a9\n\u00b0\3\u00b1\6\u00b1\u08ac\n\u00b1\r\u00b1\16")
        buf.write("\u00b1\u08ad\3\u00b2\3\u00b2\3\u00b2\3\u00b2\5\u00b2\u08b4")
        buf.write("\n\u00b2\3\u00b2\3\u00b2\5\u00b2\u08b8\n\u00b2\3\u00b2")
        buf.write("\3\u00b2\3\u00b3\3\u00b3\5\u00b3\u08be\n\u00b3\3\u00b4")
        buf.write("\3\u00b4\3\u00b4\7\u00b4\u08c3\n\u00b4\f\u00b4\16\u00b4")
        buf.write("\u08c6\13\u00b4\3\u00b5\3\u00b5\3\u00b5\3\u00b5\3\u00b5")
        buf.write("\7\u00b5\u08cd\n\u00b5\f\u00b5\16\u00b5\u08d0\13\u00b5")
        buf.write("\5\u00b5\u08d2\n\u00b5\3\u00b5\5\u00b5\u08d5\n\u00b5\3")
        buf.write("\u00b6\3\u00b6\3\u00b6\5\u00b6\u08da\n\u00b6\3\u00b6\3")
        buf.write("\u00b6\3\u00b7\3\u00b7\5\u00b7\u08e0\n\u00b7\3\u00b7\3")
        buf.write("\u00b7\7\u00b7\u08e4\n\u00b7\f\u00b7\16\u00b7\u08e7\13")
        buf.write("\u00b7\3\u00b7\3\u00b7\3\u00b7\3\u00b7\5\u00b7\u08ed\n")
        buf.write("\u00b7\3\u00b8\3\u00b8\3\u00b8\7\u00b8\u08f2\n\u00b8\f")
        buf.write("\u00b8\16\u00b8\u08f5\13\u00b8\3\u00b9\3\u00b9\3\u00b9")
        buf.write("\3\u00b9\3\u00ba\5\u00ba\u08fc\n\u00ba\3\u00ba\3\u00ba")
        buf.write("\5\u00ba\u0900\n\u00ba\3\u00bb\3\u00bb\3\u00bb\3\u00bb")
        buf.write("\3\u00bb\3\u00bc\3\u00bc\3\u00bc\3\u00bc\3\u00bc\3\u00bc")
        buf.write("\3\u00bc\3\u00bc\5\u00bc\u090f\n\u00bc\3\u00bc\3\u00bc")
        buf.write("\5\u00bc\u0913\n\u00bc\3\u00bc\3\u00bc\3\u00bc\3\u00bc")
        buf.write("\3\u00bc\7\u00bc\u091a\n\u00bc\f\u00bc\16\u00bc\u091d")
        buf.write("\13\u00bc\3\u00bc\5\u00bc\u0920\n\u00bc\3\u00bc\3\u00bc")
        buf.write("\5\u00bc\u0924\n\u00bc\3\u00bd\3\u00bd\3\u00bd\3\u00bd")
        buf.write("\3\u00be\3\u00be\3\u00be\3\u00be\3\u00bf\3\u00bf\3\u00bf")
        buf.write("\3\u00bf\3\u00c0\3\u00c0\3\u00c0\3\u00c0\3\u00c0\3\u00c0")
        buf.write("\3\u00c0\3\u00c0\5\u00c0\u093a\n\u00c0\3\u00c1\3\u00c1")
        buf.write("\3\u00c2\3\u00c2\3\u00c2\3\u00c2\5\u00c2\u0942\n\u00c2")
        buf.write("\3\u00c3\3\u00c3\7\u00c3\u0946\n\u00c3\f\u00c3\16\u00c3")
        buf.write("\u0949\13\u00c3\3\u00c3\3\u00c3\3\u00c4\3\u00c4\7\u00c4")
        buf.write("\u094f\n\u00c4\f\u00c4\16\u00c4\u0952\13\u00c4\3\u00c4")
        buf.write("\3\u00c4\3\u00c5\3\u00c5\3\u00c5\3\u00c5\5\u00c5\u095a")
        buf.write("\n\u00c5\3\u00c6\3\u00c6\3\u00c6\3\u00c6\5\u00c6\u0960")
        buf.write("\n\u00c6\3\u00c7\3\u00c7\3\u00c7\7\u00c7\u0965\n\u00c7")
        buf.write("\f\u00c7\16\u00c7\u0968\13\u00c7\3\u00c7\3\u00c7\6\u00c7")
        buf.write("\u096c\n\u00c7\r\u00c7\16\u00c7\u096d\5\u00c7\u0970\n")
        buf.write("\u00c7\3\u00c8\3\u00c8\3\u00c9\3\u00c9\3\u00c9\5\u00c9")
        buf.write("\u0977\n\u00c9\3\u00c9\5\u00c9\u097a\n\u00c9\3\u00c9\5")
        buf.write("\u00c9\u097d\n\u00c9\3\u00c9\3\u00c9\5\u00c9\u0981\n\u00c9")
        buf.write("\3\u00ca\5\u00ca\u0984\n\u00ca\3\u00ca\3\u00ca\3\u00ca")
        buf.write("\5\u00ca\u0989\n\u00ca\3\u00ca\5\u00ca\u098c\n\u00ca\3")
        buf.write("\u00ca\5\u00ca\u098f\n\u00ca\3\u00ca\3\u00ca\5\u00ca\u0993")
        buf.write("\n\u00ca\3\u00cb\3\u00cb\3\u00cb\5\u00cb\u0998\n\u00cb")
        buf.write("\3\u00cb\5\u00cb\u099b\n\u00cb\3\u00cb\5\u00cb\u099e\n")
        buf.write("\u00cb\3\u00cb\3\u00cb\5\u00cb\u09a2\n\u00cb\3\u00cc\3")
        buf.write("\u00cc\3\u00cc\5\u00cc\u09a7\n\u00cc\3\u00cc\3\u00cc\5")
        buf.write("\u00cc\u09ab\n\u00cc\3\u00cd\3\u00cd\3\u00cd\3\u00cd\5")
        buf.write("\u00cd\u09b1\n\u00cd\3\u00cd\3\u00cd\5\u00cd\u09b5\n\u00cd")
        buf.write("\3\u00cd\3\u00cd\5\u00cd\u09b9\n\u00cd\3\u00cd\3\u00cd")
        buf.write("\3\u00ce\3\u00ce\3\u00ce\3\u00ce\3\u00ce\3\u00ce\3\u00ce")
        buf.write("\3\u00ce\3\u00ce\3\u00ce\5\u00ce\u09c7\n\u00ce\3\u00cf")
        buf.write("\3\u00cf\3\u00cf\3\u00d0\3\u00d0\3\u00d0\3\u00d0\3\u00d0")
        buf.write("\3\u00d0\3\u00d0\3\u00d0\5\u00d0\u09d4\n\u00d0\3\u00d0")
        buf.write("\3\u00d0\3\u00d0\3\u00d0\5\u00d0\u09da\n\u00d0\3\u00d1")
        buf.write("\3\u00d1\3\u00d1\3\u00d1\3\u00d1\3\u00d2\3\u00d2\3\u00d2")
        buf.write("\3\u00d2\3\u00d2\3\u00d2\3\u00d2\3\u00d2\3\u00d2\3\u00d2")
        buf.write("\3\u00d2\3\u00d2\5\u00d2\u09ed\n\u00d2\3\u00d3\3\u00d3")
        buf.write("\3\u00d3\3\u00d3\3\u00d3\3\u00d3\3\u00d4\3\u00d4\3\u00d4")
        buf.write("\5\u00d4\u09f8\n\u00d4\3\u00d4\3\u00d4\5\u00d4\u09fc\n")
        buf.write("\u00d4\3\u00d4\3\u00d4\3\u00d5\3\u00d5\5\u00d5\u0a02\n")
        buf.write("\u00d5\3\u00d5\3\u00d5\5\u00d5\u0a06\n\u00d5\3\u00d5\3")
        buf.write("\u00d5\5\u00d5\u0a0a\n\u00d5\3\u00d5\3\u00d5\3\u00d5\3")
        buf.write("\u00d5\3\u00d5\5\u00d5\u0a11\n\u00d5\3\u00d6\3\u00d6\3")
        buf.write("\u00d6\3\u00d6\3\u00d6\5\u00d6\u0a18\n\u00d6\3\u00d6\5")
        buf.write("\u00d6\u0a1b\n\u00d6\3\u00d6\3\u00d6\7\u00d6\u0a1f\n\u00d6")
        buf.write("\f\u00d6\16\u00d6\u0a22\13\u00d6\3\u00d7\3\u00d7\3\u00d7")
        buf.write("\3\u00d7\5\u00d7\u0a28\n\u00d7\3\u00d7\3\u00d7\3\u00d7")
        buf.write("\5\u00d7\u0a2d\n\u00d7\3\u00d7\5\u00d7\u0a30\n\u00d7\3")
        buf.write("\u00d7\3\u00d7\3\u00d7\3\u00d7\3\u00d7\3\u00d7\5\u00d7")
        buf.write("\u0a38\n\u00d7\3\u00d8\3\u00d8\3\u00d8\3\u00d8\5\u00d8")
        buf.write("\u0a3e\n\u00d8\3\u00d9\3\u00d9\5\u00d9\u0a42\n\u00d9\3")
        buf.write("\u00d9\3\u00d9\3\u00da\3\u00da\5\u00da\u0a48\n\u00da\3")
        buf.write("\u00da\3\u00da\5\u00da\u0a4c\n\u00da\3\u00db\3\u00db\3")
        buf.write("\u00db\2\2\u00dc\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36")
        buf.write(" \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprt")
        buf.write("vxz|~\u0080\u0082\u0084\u0086\u0088\u008a\u008c\u008e")
        buf.write("\u0090\u0092\u0094\u0096\u0098\u009a\u009c\u009e\u00a0")
        buf.write("\u00a2\u00a4\u00a6\u00a8\u00aa\u00ac\u00ae\u00b0\u00b2")
        buf.write("\u00b4\u00b6\u00b8\u00ba\u00bc\u00be\u00c0\u00c2\u00c4")
        buf.write("\u00c6\u00c8\u00ca\u00cc\u00ce\u00d0\u00d2\u00d4\u00d6")
        buf.write("\u00d8\u00da\u00dc\u00de\u00e0\u00e2\u00e4\u00e6\u00e8")
        buf.write("\u00ea\u00ec\u00ee\u00f0\u00f2\u00f4\u00f6\u00f8\u00fa")
        buf.write("\u00fc\u00fe\u0100\u0102\u0104\u0106\u0108\u010a\u010c")
        buf.write("\u010e\u0110\u0112\u0114\u0116\u0118\u011a\u011c\u011e")
        buf.write("\u0120\u0122\u0124\u0126\u0128\u012a\u012c\u012e\u0130")
        buf.write("\u0132\u0134\u0136\u0138\u013a\u013c\u013e\u0140\u0142")
        buf.write("\u0144\u0146\u0148\u014a\u014c\u014e\u0150\u0152\u0154")
        buf.write("\u0156\u0158\u015a\u015c\u015e\u0160\u0162\u0164\u0166")
        buf.write("\u0168\u016a\u016c\u016e\u0170\u0172\u0174\u0176\u0178")
        buf.write("\u017a\u017c\u017e\u0180\u0182\u0184\u0186\u0188\u018a")
        buf.write("\u018c\u018e\u0190\u0192\u0194\u0196\u0198\u019a\u019c")
        buf.write("\u019e\u01a0\u01a2\u01a4\u01a6\u01a8\u01aa\u01ac\u01ae")
        buf.write("\u01b0\u01b2\u01b4\2\25\n\2\26\26\31\3188@@TTXXdeii\4")
        buf.write("\2##..\5\2\67\67IIQQ\3\2\u009d\u009e\4\2\u0093\u0094\u009f")
        buf.write("\u00a0\3\2\u0088\u0089\3\2\u008a\u008c\20\2\23\23\26\26")
        buf.write("\31\31\36\36##..88@@EETTXX\\\\deii\4\2\17\17!!\4\2\20")
        buf.write("\20hh\16\2\n\n\20\20**::CCJJLPUU[[hhllnn\4\2))\66\66\4")
        buf.write("\2\22\22__\4\2\u008a\u008a\u0095\u0095\4\2\67\67II\4\2")
        buf.write("++aa\25\2\n\n\16\16\22\24\26 \"#%&(\60\63\63\65:<<?@B")
        buf.write("EGGIKMQSUXjlnqq\3\2PQ\26\2\13\r\17\21\25\25!!$$\'\'\61")
        buf.write("\62\64\64;;=>AAFFHHLLRRVWggkkoprs\2\u0b5c\2\u01b7\3\2")
        buf.write("\2\2\4\u01cf\3\2\2\2\6\u01db\3\2\2\2\b\u01e9\3\2\2\2\n")
        buf.write("\u01eb\3\2\2\2\f\u01f5\3\2\2\2\16\u01fb\3\2\2\2\20\u0200")
        buf.write("\3\2\2\2\22\u0202\3\2\2\2\24\u0204\3\2\2\2\26\u020a\3")
        buf.write("\2\2\2\30\u020c\3\2\2\2\32\u0217\3\2\2\2\34\u0222\3\2")
        buf.write("\2\2\36\u022d\3\2\2\2 \u0232\3\2\2\2\"\u023c\3\2\2\2$")
        buf.write("\u0249\3\2\2\2&\u024b\3\2\2\2(\u0253\3\2\2\2*\u025b\3")
        buf.write("\2\2\2,\u0263\3\2\2\2.\u026b\3\2\2\2\60\u0273\3\2\2\2")
        buf.write("\62\u027b\3\2\2\2\64\u0283\3\2\2\2\66\u028b\3\2\2\28\u0297")
        buf.write("\3\2\2\2:\u02a2\3\2\2\2<\u02aa\3\2\2\2>\u02b2\3\2\2\2")
        buf.write("@\u02be\3\2\2\2B\u02c6\3\2\2\2D\u02d5\3\2\2\2F\u02f1\3")
        buf.write("\2\2\2H\u02f3\3\2\2\2J\u0392\3\2\2\2L\u0396\3\2\2\2N\u0398")
        buf.write("\3\2\2\2P\u039c\3\2\2\2R\u03a4\3\2\2\2T\u03b4\3\2\2\2")
        buf.write("V\u03b8\3\2\2\2X\u03ba\3\2\2\2Z\u03c4\3\2\2\2\\\u03c6")
        buf.write("\3\2\2\2^\u03cf\3\2\2\2`\u03dc\3\2\2\2b\u03e3\3\2\2\2")
        buf.write("d\u03e5\3\2\2\2f\u03f8\3\2\2\2h\u03fa\3\2\2\2j\u0403\3")
        buf.write("\2\2\2l\u0410\3\2\2\2n\u0412\3\2\2\2p\u0427\3\2\2\2r\u0430")
        buf.write("\3\2\2\2t\u0441\3\2\2\2v\u044c\3\2\2\2x\u0451\3\2\2\2")
        buf.write("z\u0462\3\2\2\2|\u0464\3\2\2\2~\u046d\3\2\2\2\u0080\u0472")
        buf.write("\3\2\2\2\u0082\u047c\3\2\2\2\u0084\u047e\3\2\2\2\u0086")
        buf.write("\u0481\3\2\2\2\u0088\u048c\3\2\2\2\u008a\u0498\3\2\2\2")
        buf.write("\u008c\u049a\3\2\2\2\u008e\u049f\3\2\2\2\u0090\u04a2\3")
        buf.write("\2\2\2\u0092\u04b1\3\2\2\2\u0094\u04ba\3\2\2\2\u0096\u04c5")
        buf.write("\3\2\2\2\u0098\u04c7\3\2\2\2\u009a\u04ce\3\2\2\2\u009c")
        buf.write("\u04d7\3\2\2\2\u009e\u04d9\3\2\2\2\u00a0\u04dd\3\2\2\2")
        buf.write("\u00a2\u04f2\3\2\2\2\u00a4\u04f9\3\2\2\2\u00a6\u04fb\3")
        buf.write("\2\2\2\u00a8\u0501\3\2\2\2\u00aa\u0585\3\2\2\2\u00ac\u0587")
        buf.write("\3\2\2\2\u00ae\u05a0\3\2\2\2\u00b0\u05a4\3\2\2\2\u00b2")
        buf.write("\u05a6\3\2\2\2\u00b4\u05b1\3\2\2\2\u00b6\u05b3\3\2\2\2")
        buf.write("\u00b8\u05b9\3\2\2\2\u00ba\u05bc\3\2\2\2\u00bc\u05cb\3")
        buf.write("\2\2\2\u00be\u05cd\3\2\2\2\u00c0\u05d1\3\2\2\2\u00c2\u05de")
        buf.write("\3\2\2\2\u00c4\u05e0\3\2\2\2\u00c6\u05f3\3\2\2\2\u00c8")
        buf.write("\u05f5\3\2\2\2\u00ca\u0601\3\2\2\2\u00cc\u0607\3\2\2\2")
        buf.write("\u00ce\u060c\3\2\2\2\u00d0\u0611\3\2\2\2\u00d2\u0613\3")
        buf.write("\2\2\2\u00d4\u0619\3\2\2\2\u00d6\u0621\3\2\2\2\u00d8\u062e")
        buf.write("\3\2\2\2\u00da\u0632\3\2\2\2\u00dc\u0638\3\2\2\2\u00de")
        buf.write("\u064b\3\2\2\2\u00e0\u064e\3\2\2\2\u00e2\u0654\3\2\2\2")
        buf.write("\u00e4\u0657\3\2\2\2\u00e6\u0663\3\2\2\2\u00e8\u0669\3")
        buf.write("\2\2\2\u00ea\u0675\3\2\2\2\u00ec\u0679\3\2\2\2\u00ee\u0682")
        buf.write("\3\2\2\2\u00f0\u068b\3\2\2\2\u00f2\u068f\3\2\2\2\u00f4")
        buf.write("\u069e\3\2\2\2\u00f6\u06a7\3\2\2\2\u00f8\u06a9\3\2\2\2")
        buf.write("\u00fa\u06b1\3\2\2\2\u00fc\u06b5\3\2\2\2\u00fe\u06bc\3")
        buf.write("\2\2\2\u0100\u06c1\3\2\2\2\u0102\u06cb\3\2\2\2\u0104\u06cf")
        buf.write("\3\2\2\2\u0106\u06e4\3\2\2\2\u0108\u06eb\3\2\2\2\u010a")
        buf.write("\u06f9\3\2\2\2\u010c\u0701\3\2\2\2\u010e\u0705\3\2\2\2")
        buf.write("\u0110\u070d\3\2\2\2\u0112\u0714\3\2\2\2\u0114\u0718\3")
        buf.write("\2\2\2\u0116\u071a\3\2\2\2\u0118\u071e\3\2\2\2\u011a\u0726")
        buf.write("\3\2\2\2\u011c\u0728\3\2\2\2\u011e\u0738\3\2\2\2\u0120")
        buf.write("\u0742\3\2\2\2\u0122\u0745\3\2\2\2\u0124\u074c\3\2\2\2")
        buf.write("\u0126\u075e\3\2\2\2\u0128\u0767\3\2\2\2\u012a\u0776\3")
        buf.write("\2\2\2\u012c\u077a\3\2\2\2\u012e\u077d\3\2\2\2\u0130\u078a")
        buf.write("\3\2\2\2\u0132\u0790\3\2\2\2\u0134\u07ab\3\2\2\2\u0136")
        buf.write("\u07ad\3\2\2\2\u0138\u07b4\3\2\2\2\u013a\u07be\3\2\2\2")
        buf.write("\u013c\u07c0\3\2\2\2\u013e\u07c3\3\2\2\2\u0140\u07cd\3")
        buf.write("\2\2\2\u0142\u07de\3\2\2\2\u0144\u07ea\3\2\2\2\u0146\u07f3")
        buf.write("\3\2\2\2\u0148\u0803\3\2\2\2\u014a\u080f\3\2\2\2\u014c")
        buf.write("\u0816\3\2\2\2\u014e\u0818\3\2\2\2\u0150\u081b\3\2\2\2")
        buf.write("\u0152\u0825\3\2\2\2\u0154\u086c\3\2\2\2\u0156\u0882\3")
        buf.write("\2\2\2\u0158\u0885\3\2\2\2\u015a\u0896\3\2\2\2\u015c\u089d")
        buf.write("\3\2\2\2\u015e\u08a8\3\2\2\2\u0160\u08ab\3\2\2\2\u0162")
        buf.write("\u08af\3\2\2\2\u0164\u08bd\3\2\2\2\u0166\u08bf\3\2\2\2")
        buf.write("\u0168\u08c7\3\2\2\2\u016a\u08d9\3\2\2\2\u016c\u08ec\3")
        buf.write("\2\2\2\u016e\u08ee\3\2\2\2\u0170\u08f6\3\2\2\2\u0172\u08ff")
        buf.write("\3\2\2\2\u0174\u0901\3\2\2\2\u0176\u0923\3\2\2\2\u0178")
        buf.write("\u0925\3\2\2\2\u017a\u0929\3\2\2\2\u017c\u092d\3\2\2\2")
        buf.write("\u017e\u0939\3\2\2\2\u0180\u093b\3\2\2\2\u0182\u0941\3")
        buf.write("\2\2\2\u0184\u0943\3\2\2\2\u0186\u094c\3\2\2\2\u0188\u0959")
        buf.write("\3\2\2\2\u018a\u095f\3\2\2\2\u018c\u0961\3\2\2\2\u018e")
        buf.write("\u0971\3\2\2\2\u0190\u0973\3\2\2\2\u0192\u0983\3\2\2\2")
        buf.write("\u0194\u0994\3\2\2\2\u0196\u09a3\3\2\2\2\u0198\u09ac\3")
        buf.write("\2\2\2\u019a\u09bc\3\2\2\2\u019c\u09c8\3\2\2\2\u019e\u09cb")
        buf.write("\3\2\2\2\u01a0\u09db\3\2\2\2\u01a2\u09e0\3\2\2\2\u01a4")
        buf.write("\u09ee\3\2\2\2\u01a6\u09f4\3\2\2\2\u01a8\u09ff\3\2\2\2")
        buf.write("\u01aa\u0a17\3\2\2\2\u01ac\u0a23\3\2\2\2\u01ae\u0a39\3")
        buf.write("\2\2\2\u01b0\u0a3f\3\2\2\2\u01b2\u0a45\3\2\2\2\u01b4\u0a4d")
        buf.write("\3\2\2\2\u01b6\u01b8\7\3\2\2\u01b7\u01b6\3\2\2\2\u01b7")
        buf.write("\u01b8\3\2\2\2\u01b8\u01ba\3\2\2\2\u01b9\u01bb\5\u00d8")
        buf.write("m\2\u01ba\u01b9\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb\u01bd")
        buf.write("\3\2\2\2\u01bc\u01be\5\u00dco\2\u01bd\u01bc\3\2\2\2\u01bd")
        buf.write("\u01be\3\2\2\2\u01be\u01c2\3\2\2\2\u01bf\u01c1\5\u015c")
        buf.write("\u00af\2\u01c0\u01bf\3\2\2\2\u01c1\u01c4\3\2\2\2\u01c2")
        buf.write("\u01c0\3\2\2\2\u01c2\u01c3\3\2\2\2\u01c3\u01c6\3\2\2\2")
        buf.write("\u01c4\u01c2\3\2\2\2\u01c5\u01c7\5\u00e0q\2\u01c6\u01c5")
        buf.write("\3\2\2\2\u01c6\u01c7\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8")
        buf.write("\u01c9\7\2\2\3\u01c9\3\3\2\2\2\u01ca\u01cc\5\u01b4\u00db")
        buf.write("\2\u01cb\u01cd\5\30\r\2\u01cc\u01cb\3\2\2\2\u01cc\u01cd")
        buf.write("\3\2\2\2\u01cd\u01d0\3\2\2\2\u01ce\u01d0\5\u00e6t\2\u01cf")
        buf.write("\u01ca\3\2\2\2\u01cf\u01ce\3\2\2\2\u01d0\u01d8\3\2\2\2")
        buf.write("\u01d1\u01d2\7\u0084\2\2\u01d2\u01d4\5\u01b4\u00db\2\u01d3")
        buf.write("\u01d5\5\30\r\2\u01d4\u01d3\3\2\2\2\u01d4\u01d5\3\2\2")
        buf.write("\2\u01d5\u01d7\3\2\2\2\u01d6\u01d1\3\2\2\2\u01d7\u01da")
        buf.write("\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9")
        buf.write("\5\3\2\2\2\u01da\u01d8\3\2\2\2\u01db\u01e1\5\b\5\2\u01dc")
        buf.write("\u01e0\7\u0095\2\2\u01dd\u01e0\5\u0144\u00a3\2\u01de\u01e0")
        buf.write("\7\u008a\2\2\u01df\u01dc\3\2\2\2\u01df\u01dd\3\2\2\2\u01df")
        buf.write("\u01de\3\2\2\2\u01e0\u01e3\3\2\2\2\u01e1\u01df\3\2\2\2")
        buf.write("\u01e1\u01e2\3\2\2\2\u01e2\7\3\2\2\2\u01e3\u01e1\3\2\2")
        buf.write("\2\u01e4\u01ea\5\16\b\2\u01e5\u01ea\5\26\f\2\u01e6\u01e7")
        buf.write("\7m\2\2\u01e7\u01ea\7\u008a\2\2\u01e8\u01ea\5\n\6\2\u01e9")
        buf.write("\u01e4\3\2\2\2\u01e9\u01e5\3\2\2\2\u01e9\u01e6\3\2\2\2")
        buf.write("\u01e9\u01e8\3\2\2\2\u01ea\t\3\2\2\2\u01eb\u01ec\7\u0082")
        buf.write("\2\2\u01ec\u01ef\5\f\7\2\u01ed\u01ee\7\u0085\2\2\u01ee")
        buf.write("\u01f0\5\f\7\2\u01ef\u01ed\3\2\2\2\u01f0\u01f1\3\2\2\2")
        buf.write("\u01f1\u01ef\3\2\2\2\u01f1\u01f2\3\2\2\2\u01f2\u01f3\3")
        buf.write("\2\2\2\u01f3\u01f4\7\u0083\2\2\u01f4\13\3\2\2\2\u01f5")
        buf.write("\u01f7\5\6\4\2\u01f6\u01f8\5\u01b4\u00db\2\u01f7\u01f6")
        buf.write("\3\2\2\2\u01f7\u01f8\3\2\2\2\u01f8\r\3\2\2\2\u01f9\u01fc")
        buf.write("\5\20\t\2\u01fa\u01fc\7\23\2\2\u01fb\u01f9\3\2\2\2\u01fb")
        buf.write("\u01fa\3\2\2\2\u01fc\17\3\2\2\2\u01fd\u0201\5\22\n\2\u01fe")
        buf.write("\u0201\5\24\13\2\u01ff\u0201\7\36\2\2\u0200\u01fd\3\2")
        buf.write("\2\2\u0200\u01fe\3\2\2\2\u0200\u01ff\3\2\2\2\u0201\21")
        buf.write("\3\2\2\2\u0202\u0203\t\2\2\2\u0203\23\3\2\2\2\u0204\u0205")
        buf.write("\t\3\2\2\u0205\25\3\2\2\2\u0206\u020b\5\4\3\2\u0207\u020b")
        buf.write("\7E\2\2\u0208\u020b\7$\2\2\u0209\u020b\7\\\2\2\u020a\u0206")
        buf.write("\3\2\2\2\u020a\u0207\3\2\2\2\u020a\u0208\3\2\2\2\u020a")
        buf.write("\u0209\3\2\2\2\u020b\27\3\2\2\2\u020c\u020d\7\u0093\2")
        buf.write("\2\u020d\u0212\5\6\4\2\u020e\u020f\7\u0085\2\2\u020f\u0211")
        buf.write("\5\6\4\2\u0210\u020e\3\2\2\2\u0211\u0214\3\2\2\2\u0212")
        buf.write("\u0210\3\2\2\2\u0212\u0213\3\2\2\2\u0213\u0215\3\2\2\2")
        buf.write("\u0214\u0212\3\2\2\2\u0215\u0216\7\u0094\2\2\u0216\31")
        buf.write("\3\2\2\2\u0217\u021c\5\34\17\2\u0218\u0219\7\u0085\2\2")
        buf.write("\u0219\u021b\5\34\17\2\u021a\u0218\3\2\2\2\u021b\u021e")
        buf.write("\3\2\2\2\u021c\u021a\3\2\2\2\u021c\u021d\3\2\2\2\u021d")
        buf.write("\33\3\2\2\2\u021e\u021c\3\2\2\2\u021f\u0220\5\u01b4\u00db")
        buf.write("\2\u0220\u0221\7\u0086\2\2\u0221\u0223\3\2\2\2\u0222\u021f")
        buf.write("\3\2\2\2\u0222\u0223\3\2\2\2\u0223\u0225\3\2\2\2\u0224")
        buf.write("\u0226\t\4\2\2\u0225\u0224\3\2\2\2\u0225\u0226\3\2\2\2")
        buf.write("\u0226\u0227\3\2\2\2\u0227\u0228\5\36\20\2\u0228\35\3")
        buf.write("\2\2\2\u0229\u022e\5\"\22\2\u022a\u022e\5 \21\2\u022b")
        buf.write("\u022c\7Q\2\2\u022c\u022e\5 \21\2\u022d\u0229\3\2\2\2")
        buf.write("\u022d\u022a\3\2\2\2\u022d\u022b\3\2\2\2\u022e\37\3\2")
        buf.write("\2\2\u022f\u0233\5x=\2\u0230\u0233\5\u0084C\2\u0231\u0233")
        buf.write("\5&\24\2\u0232\u022f\3\2\2\2\u0232\u0230\3\2\2\2\u0232")
        buf.write("\u0231\3\2\2\2\u0233!\3\2\2\2\u0234\u0235\5F$\2\u0235")
        buf.write("\u0236\5$\23\2\u0236\u0237\5\36\20\2\u0237\u023d\3\2\2")
        buf.write("\2\u0238\u0239\5F$\2\u0239\u023a\7\u00ab\2\2\u023a\u023b")
        buf.write("\5L\'\2\u023b\u023d\3\2\2\2\u023c\u0234\3\2\2\2\u023c")
        buf.write("\u0238\3\2\2\2\u023d#\3\2\2\2\u023e\u024a\7\u0092\2\2")
        buf.write("\u023f\u024a\7\u00a1\2\2\u0240\u024a\7\u00a2\2\2\u0241")
        buf.write("\u024a\7\u00a3\2\2\u0242\u024a\7\u00a4\2\2\u0243\u024a")
        buf.write("\7\u00a5\2\2\u0244\u024a\7\u00a6\2\2\u0245\u024a\7\u00a7")
        buf.write("\2\2\u0246\u024a\7\u00a8\2\2\u0247\u024a\7\u00aa\2\2\u0248")
        buf.write("\u024a\5\u017c\u00bf\2\u0249\u023e\3\2\2\2\u0249\u023f")
        buf.write("\3\2\2\2\u0249\u0240\3\2\2\2\u0249\u0241\3\2\2\2\u0249")
        buf.write("\u0242\3\2\2\2\u0249\u0243\3\2\2\2\u0249\u0244\3\2\2\2")
        buf.write("\u0249\u0245\3\2\2\2\u0249\u0246\3\2\2\2\u0249\u0247\3")
        buf.write("\2\2\2\u0249\u0248\3\2\2\2\u024a%\3\2\2\2\u024b\u0251")
        buf.write("\5(\25\2\u024c\u024d\7\u0095\2\2\u024d\u024e\5L\'\2\u024e")
        buf.write("\u024f\7\u0086\2\2\u024f\u0250\5L\'\2\u0250\u0252\3\2")
        buf.write("\2\2\u0251\u024c\3\2\2\2\u0251\u0252\3\2\2\2\u0252\'\3")
        buf.write("\2\2\2\u0253\u0259\5*\26\2\u0254\u0257\7\u0097\2\2\u0255")
        buf.write("\u0258\5(\25\2\u0256\u0258\5N(\2\u0257\u0255\3\2\2\2\u0257")
        buf.write("\u0256\3\2\2\2\u0258\u025a\3\2\2\2\u0259\u0254\3\2\2\2")
        buf.write("\u0259\u025a\3\2\2\2\u025a)\3\2\2\2\u025b\u0260\5,\27")
        buf.write("\2\u025c\u025d\7\u009b\2\2\u025d\u025f\5,\27\2\u025e\u025c")
        buf.write("\3\2\2\2\u025f\u0262\3\2\2\2\u0260\u025e\3\2\2\2\u0260")
        buf.write("\u0261\3\2\2\2\u0261+\3\2\2\2\u0262\u0260\3\2\2\2\u0263")
        buf.write("\u0268\5.\30\2\u0264\u0265\7\u009a\2\2\u0265\u0267\5.")
        buf.write("\30\2\u0266\u0264\3\2\2\2\u0267\u026a\3\2\2\2\u0268\u0266")
        buf.write("\3\2\2\2\u0268\u0269\3\2\2\2\u0269-\3\2\2\2\u026a\u0268")
        buf.write("\3\2\2\2\u026b\u0270\5\60\31\2\u026c\u026d\7\u008e\2\2")
        buf.write("\u026d\u026f\5\60\31\2\u026e\u026c\3\2\2\2\u026f\u0272")
        buf.write("\3\2\2\2\u0270\u026e\3\2\2\2\u0270\u0271\3\2\2\2\u0271")
        buf.write("/\3\2\2\2\u0272\u0270\3\2\2\2\u0273\u0278\5\62\32\2\u0274")
        buf.write("\u0275\7\u008f\2\2\u0275\u0277\5\62\32\2\u0276\u0274\3")
        buf.write("\2\2\2\u0277\u027a\3\2\2\2\u0278\u0276\3\2\2\2\u0278\u0279")
        buf.write("\3\2\2\2\u0279\61\3\2\2\2\u027a\u0278\3\2\2\2\u027b\u0280")
        buf.write("\5\64\33\2\u027c\u027d\7\u008d\2\2\u027d\u027f\5\64\33")
        buf.write("\2\u027e\u027c\3\2\2\2\u027f\u0282\3\2\2\2\u0280\u027e")
        buf.write("\3\2\2\2\u0280\u0281\3\2\2\2\u0281\63\3\2\2\2\u0282\u0280")
        buf.write("\3\2\2\2\u0283\u0288\5\66\34\2\u0284\u0285\t\5\2\2\u0285")
        buf.write("\u0287\5\66\34\2\u0286\u0284\3\2\2\2\u0287\u028a\3\2\2")
        buf.write("\2\u0288\u0286\3\2\2\2\u0288\u0289\3\2\2\2\u0289\65\3")
        buf.write("\2\2\2\u028a\u0288\3\2\2\2\u028b\u0294\58\35\2\u028c\u028d")
        buf.write("\t\6\2\2\u028d\u0293\58\35\2\u028e\u028f\7<\2\2\u028f")
        buf.write("\u0293\5r:\2\u0290\u0291\7\16\2\2\u0291\u0293\5\6\4\2")
        buf.write("\u0292\u028c\3\2\2\2\u0292\u028e\3\2\2\2\u0292\u0290\3")
        buf.write("\2\2\2\u0293\u0296\3\2\2\2\u0294\u0292\3\2\2\2\u0294\u0295")
        buf.write("\3\2\2\2\u0295\67\3\2\2\2\u0296\u0294\3\2\2\2\u0297\u029f")
        buf.write("\5:\36\2\u0298\u029b\7\u00a9\2\2\u0299\u029b\5\u017a\u00be")
        buf.write("\2\u029a\u0298\3\2\2\2\u029a\u0299\3\2\2\2\u029b\u029c")
        buf.write("\3\2\2\2\u029c\u029e\5:\36\2\u029d\u029a\3\2\2\2\u029e")
        buf.write("\u02a1\3\2\2\2\u029f\u029d\3\2\2\2\u029f\u02a0\3\2\2\2")
        buf.write("\u02a09\3\2\2\2\u02a1\u029f\3\2\2\2\u02a2\u02a7\5<\37")
        buf.write("\2\u02a3\u02a4\t\7\2\2\u02a4\u02a6\5<\37\2\u02a5\u02a3")
        buf.write("\3\2\2\2\u02a6\u02a9\3\2\2\2\u02a7\u02a5\3\2\2\2\u02a7")
        buf.write("\u02a8\3\2\2\2\u02a8;\3\2\2\2\u02a9\u02a7\3\2\2\2\u02aa")
        buf.write("\u02af\5> \2\u02ab\u02ac\t\b\2\2\u02ac\u02ae\5> \2\u02ad")
        buf.write("\u02ab\3\2\2\2\u02ae\u02b1\3\2\2\2\u02af\u02ad\3\2\2\2")
        buf.write("\u02af\u02b0\3\2\2\2\u02b0=\3\2\2\2\u02b1\u02af\3\2\2")
        buf.write("\2\u02b2\u02bc\5D#\2\u02b3\u02b4\7^\2\2\u02b4\u02b9\7")
        buf.write("~\2\2\u02b5\u02b7\5@!\2\u02b6\u02b8\7\u0085\2\2\u02b7")
        buf.write("\u02b6\3\2\2\2\u02b7\u02b8\3\2\2\2\u02b8\u02ba\3\2\2\2")
        buf.write("\u02b9\u02b5\3\2\2\2\u02b9\u02ba\3\2\2\2\u02ba\u02bb\3")
        buf.write("\2\2\2\u02bb\u02bd\7\177\2\2\u02bc\u02b3\3\2\2\2\u02bc")
        buf.write("\u02bd\3\2\2\2\u02bd?\3\2\2\2\u02be\u02c3\5B\"\2\u02bf")
        buf.write("\u02c0\7\u0085\2\2\u02c0\u02c2\5B\"\2\u02c1\u02bf\3\2")
        buf.write("\2\2\u02c2\u02c5\3\2\2\2\u02c3\u02c1\3\2\2\2\u02c3\u02c4")
        buf.write("\3\2\2\2\u02c4A\3\2\2\2\u02c5\u02c3\3\2\2\2\u02c6\u02c8")
        buf.write("\5\36\20\2\u02c7\u02c9\5\u00be`\2\u02c8\u02c7\3\2\2\2")
        buf.write("\u02c8\u02c9\3\2\2\2\u02c9\u02ca\3\2\2\2\u02ca\u02cb\5")
        buf.write("\u0178\u00bd\2\u02cb\u02cc\5L\'\2\u02ccC\3\2\2\2\u02cd")
        buf.write("\u02d6\5F$\2\u02ce\u02d0\5F$\2\u02cf\u02ce\3\2\2\2\u02cf")
        buf.write("\u02d0\3\2\2\2\u02d0\u02d1\3\2\2\2\u02d1\u02d3\7\u00ac")
        buf.write("\2\2\u02d2\u02d4\5F$\2\u02d3\u02d2\3\2\2\2\u02d3\u02d4")
        buf.write("\3\2\2\2\u02d4\u02d6\3\2\2\2\u02d5\u02cd\3\2\2\2\u02d5")
        buf.write("\u02cf\3\2\2\2\u02d6E\3\2\2\2\u02d7\u02f2\5H%\2\u02d8")
        buf.write("\u02d9\7\u0088\2\2\u02d9\u02f2\5F$\2\u02da\u02db\7\u0089")
        buf.write("\2\2\u02db\u02f2\5F$\2\u02dc\u02dd\7\u0090\2\2\u02dd\u02f2")
        buf.write("\5F$\2\u02de\u02df\7\u0091\2\2\u02df\u02f2\5F$\2\u02e0")
        buf.write("\u02e1\7\u0098\2\2\u02e1\u02f2\5F$\2\u02e2\u02e3\7\u0099")
        buf.write("\2\2\u02e3\u02f2\5F$\2\u02e4\u02e5\7\u0082\2\2\u02e5\u02e6")
        buf.write("\5\6\4\2\u02e6\u02e7\7\u0083\2\2\u02e7\u02e8\5F$\2\u02e8")
        buf.write("\u02f2\3\2\2\2\u02e9\u02ea\7\21\2\2\u02ea\u02f2\5F$\2")
        buf.write("\u02eb\u02ec\7\u008d\2\2\u02ec\u02f2\5F$\2\u02ed\u02ee")
        buf.write("\7\u008a\2\2\u02ee\u02f2\5F$\2\u02ef\u02f0\7\u008f\2\2")
        buf.write("\u02f0\u02f2\5F$\2\u02f1\u02d7\3\2\2\2\u02f1\u02d8\3\2")
        buf.write("\2\2\u02f1\u02da\3\2\2\2\u02f1\u02dc\3\2\2\2\u02f1\u02de")
        buf.write("\3\2\2\2\u02f1\u02e0\3\2\2\2\u02f1\u02e2\3\2\2\2\u02f1")
        buf.write("\u02e4\3\2\2\2\u02f1\u02e9\3\2\2\2\u02f1\u02eb\3\2\2\2")
        buf.write("\u02f1\u02ed\3\2\2\2\u02f1\u02ef\3\2\2\2\u02f2G\3\2\2")
        buf.write("\2\u02f3\u02f5\5J&\2\u02f4\u02f6\7\u0090\2\2\u02f5\u02f4")
        buf.write("\3\2\2\2\u02f5\u02f6\3\2\2\2\u02f6\u02fa\3\2\2\2\u02f7")
        buf.write("\u02f9\5R*\2\u02f8\u02f7\3\2\2\2\u02f9\u02fc\3\2\2\2\u02fa")
        buf.write("\u02f8\3\2\2\2\u02fa\u02fb\3\2\2\2\u02fb\u02fe\3\2\2\2")
        buf.write("\u02fc\u02fa\3\2\2\2\u02fd\u02ff\7\u0090\2\2\u02fe\u02fd")
        buf.write("\3\2\2\2\u02fe\u02ff\3\2\2\2\u02ff\u0316\3\2\2\2\u0300")
        buf.write("\u0307\5P)\2\u0301\u0307\5\u01b0\u00d9\2\u0302\u0307\7")
        buf.write("\u0098\2\2\u0303\u0307\7\u0099\2\2\u0304\u0305\7\u009c")
        buf.write("\2\2\u0305\u0307\5\u01b4\u00db\2\u0306\u0300\3\2\2\2\u0306")
        buf.write("\u0301\3\2\2\2\u0306\u0302\3\2\2\2\u0306\u0303\3\2\2\2")
        buf.write("\u0306\u0304\3\2\2\2\u0307\u0309\3\2\2\2\u0308\u030a\7")
        buf.write("\u0090\2\2\u0309\u0308\3\2\2\2\u0309\u030a\3\2\2\2\u030a")
        buf.write("\u030e\3\2\2\2\u030b\u030d\5R*\2\u030c\u030b\3\2\2\2\u030d")
        buf.write("\u0310\3\2\2\2\u030e\u030c\3\2\2\2\u030e\u030f\3\2\2\2")
        buf.write("\u030f\u0312\3\2\2\2\u0310\u030e\3\2\2\2\u0311\u0313\7")
        buf.write("\u0090\2\2\u0312\u0311\3\2\2\2\u0312\u0313\3\2\2\2\u0313")
        buf.write("\u0315\3\2\2\2\u0314\u0306\3\2\2\2\u0315\u0318\3\2\2\2")
        buf.write("\u0316\u0314\3\2\2\2\u0316\u0317\3\2\2\2\u0317I\3\2\2")
        buf.write("\2\u0318\u0316\3\2\2\2\u0319\u0393\5\u017e\u00c0\2\u031a")
        buf.write("\u031c\5\u01b4\u00db\2\u031b\u031d\5\30\r\2\u031c\u031b")
        buf.write("\3\2\2\2\u031c\u031d\3\2\2\2\u031d\u0393\3\2\2\2\u031e")
        buf.write("\u031f\7\u0082\2\2\u031f\u0320\5\36\20\2\u0320\u0321\7")
        buf.write("\u0083\2\2\u0321\u0393\3\2\2\2\u0322\u0393\5V,\2\u0323")
        buf.write("\u0393\5\u00e6t\2\u0324\u0393\7t\2\2\u0325\u0393\7_\2")
        buf.write("\2\u0326\u0330\7\22\2\2\u0327\u0328\7\u0084\2\2\u0328")
        buf.write("\u032a\5\u01b4\u00db\2\u0329\u032b\5\30\r\2\u032a\u0329")
        buf.write("\3\2\2\2\u032a\u032b\3\2\2\2\u032b\u0331\3\2\2\2\u032c")
        buf.write("\u032d\7\u0080\2\2\u032d\u032e\5X-\2\u032e\u032f\7\u0081")
        buf.write("\2\2\u032f\u0331\3\2\2\2\u0330\u0327\3\2\2\2\u0330\u032c")
        buf.write("\3\2\2\2\u0331\u0393\3\2\2\2\u0332\u034f\7C\2\2\u0333")
        buf.write("\u0349\5\6\4\2\u0334\u034a\5\u01b2\u00da\2\u0335\u034a")
        buf.write("\5Z.\2\u0336\u0337\7\u0080\2\2\u0337\u0338\5X-\2\u0338")
        buf.write("\u033c\7\u0081\2\2\u0339\u033b\5\u0144\u00a3\2\u033a\u0339")
        buf.write("\3\2\2\2\u033b\u033e\3\2\2\2\u033c\u033a\3\2\2\2\u033c")
        buf.write("\u033d\3\2\2\2\u033d\u0340\3\2\2\2\u033e\u033c\3\2\2\2")
        buf.write("\u033f\u0341\5\u0146\u00a4\2\u0340\u033f\3\2\2\2\u0340")
        buf.write("\u0341\3\2\2\2\u0341\u034a\3\2\2\2\u0342\u0344\5\u0144")
        buf.write("\u00a3\2\u0343\u0342\3\2\2\2\u0344\u0345\3\2\2\2\u0345")
        buf.write("\u0343\3\2\2\2\u0345\u0346\3\2\2\2\u0346\u0347\3\2\2\2")
        buf.write("\u0347\u0348\5\u0146\u00a4\2\u0348\u034a\3\2\2\2\u0349")
        buf.write("\u0334\3\2\2\2\u0349\u0335\3\2\2\2\u0349\u0336\3\2\2\2")
        buf.write("\u0349\u0343\3\2\2\2\u034a\u0350\3\2\2\2\u034b\u0350\5")
        buf.write("h\65\2\u034c\u034d\5\u0144\u00a3\2\u034d\u034e\5\u0146")
        buf.write("\u00a4\2\u034e\u0350\3\2\2\2\u034f\u0333\3\2\2\2\u034f")
        buf.write("\u034b\3\2\2\2\u034f\u034c\3\2\2\2\u0350\u0393\3\2\2\2")
        buf.write("\u0351\u0352\7\u0082\2\2\u0352\u0355\5\34\17\2\u0353\u0354")
        buf.write("\7\u0085\2\2\u0354\u0356\5\34\17\2\u0355\u0353\3\2\2\2")
        buf.write("\u0356\u0357\3\2\2\2\u0357\u0355\3\2\2\2\u0357\u0358\3")
        buf.write("\2\2\2\u0358\u0359\3\2\2\2\u0359\u035a\7\u0083\2\2\u035a")
        buf.write("\u0393\3\2\2\2\u035b\u035c\7c\2\2\u035c\u0360\7\u0082")
        buf.write("\2\2\u035d\u0361\5n8\2\u035e\u0361\5\6\4\2\u035f\u0361")
        buf.write("\7m\2\2\u0360\u035d\3\2\2\2\u0360\u035e\3\2\2\2\u0360")
        buf.write("\u035f\3\2\2\2\u0361\u0362\3\2\2\2\u0362\u0393\7\u0083")
        buf.write("\2\2\u0363\u0364\7\32\2\2\u0364\u0365\7\u0082\2\2\u0365")
        buf.write("\u0366\5\36\20\2\u0366\u0367\7\u0083\2\2\u0367\u0393\3")
        buf.write("\2\2\2\u0368\u0369\7f\2\2\u0369\u036a\7\u0082\2\2\u036a")
        buf.write("\u036b\5\36\20\2\u036b\u036c\7\u0083\2\2\u036c\u0393\3")
        buf.write("\2\2\2\u036d\u0372\7\37\2\2\u036e\u036f\7\u0082\2\2\u036f")
        buf.write("\u0370\5\6\4\2\u0370\u0371\7\u0083\2\2\u0371\u0373\3\2")
        buf.write("\2\2\u0372\u036e\3\2\2\2\u0372\u0373\3\2\2\2\u0373\u0393")
        buf.write("\3\2\2\2\u0374\u0376\7\20\2\2\u0375\u0374\3\2\2\2\u0375")
        buf.write("\u0376\3\2\2\2\u0376\u0377\3\2\2\2\u0377\u037d\7 \2\2")
        buf.write("\u0378\u037a\7\u0082\2\2\u0379\u037b\5|?\2\u037a\u0379")
        buf.write("\3\2\2\2\u037a\u037b\3\2\2\2\u037b\u037c\3\2\2\2\u037c")
        buf.write("\u037e\7\u0083\2\2\u037d\u0378\3\2\2\2\u037d\u037e\3\2")
        buf.write("\2\2\u037e\u037f\3\2\2\2\u037f\u0393\5\u00acW\2\u0380")
        buf.write("\u0381\7Y\2\2\u0381\u0382\7\u0082\2\2\u0382\u0383\5\6")
        buf.write("\4\2\u0383\u0384\7\u0083\2\2\u0384\u0393\3\2\2\2\u0385")
        buf.write("\u0386\7A\2\2\u0386\u038c\7\u0082\2\2\u0387\u0388\5\u01b4")
        buf.write("\u00db\2\u0388\u0389\7\u0084\2\2\u0389\u038b\3\2\2\2\u038a")
        buf.write("\u0387\3\2\2\2\u038b\u038e\3\2\2\2\u038c\u038a\3\2\2\2")
        buf.write("\u038c\u038d\3\2\2\2\u038d\u038f\3\2\2\2\u038e\u038c\3")
        buf.write("\2\2\2\u038f\u0390\5\u01b4\u00db\2\u0390\u0391\7\u0083")
        buf.write("\2\2\u0391\u0393\3\2\2\2\u0392\u0319\3\2\2\2\u0392\u031a")
        buf.write("\3\2\2\2\u0392\u031e\3\2\2\2\u0392\u0322\3\2\2\2\u0392")
        buf.write("\u0323\3\2\2\2\u0392\u0324\3\2\2\2\u0392\u0325\3\2\2\2")
        buf.write("\u0392\u0326\3\2\2\2\u0392\u0332\3\2\2\2\u0392\u0351\3")
        buf.write("\2\2\2\u0392\u035b\3\2\2\2\u0392\u0363\3\2\2\2\u0392\u0368")
        buf.write("\3\2\2\2\u0392\u036d\3\2\2\2\u0392\u0375\3\2\2\2\u0392")
        buf.write("\u0380\3\2\2\2\u0392\u0385\3\2\2\2\u0393K\3\2\2\2\u0394")
        buf.write("\u0397\5\36\20\2\u0395\u0397\5N(\2\u0396\u0394\3\2\2\2")
        buf.write("\u0396\u0395\3\2\2\2\u0397M\3\2\2\2\u0398\u0399\7`\2\2")
        buf.write("\u0399\u039a\5\36\20\2\u039aO\3\2\2\2\u039b\u039d\7\u0095")
        buf.write("\2\2\u039c\u039b\3\2\2\2\u039c\u039d\3\2\2\2\u039d\u039e")
        buf.write("\3\2\2\2\u039e\u039f\7\u0084\2\2\u039f\u03a1\5\u01b4\u00db")
        buf.write("\2\u03a0\u03a2\5\30\r\2\u03a1\u03a0\3\2\2\2\u03a1\u03a2")
        buf.write("\3\2\2\2\u03a2Q\3\2\2\2\u03a3\u03a5\7\u0095\2\2\u03a4")
        buf.write("\u03a3\3\2\2\2\u03a4\u03a5\3\2\2\2\u03a5\u03a6\3\2\2\2")
        buf.write("\u03a6\u03a7\7\u0080\2\2\u03a7\u03ac\5T+\2\u03a8\u03a9")
        buf.write("\7\u0085\2\2\u03a9\u03ab\5T+\2\u03aa\u03a8\3\2\2\2\u03ab")
        buf.write("\u03ae\3\2\2\2\u03ac\u03aa\3\2\2\2\u03ac\u03ad\3\2\2\2")
        buf.write("\u03ad\u03af\3\2\2\2\u03ae\u03ac\3\2\2\2\u03af\u03b0\7")
        buf.write("\u0081\2\2\u03b0S\3\2\2\2\u03b1\u03b2\5\u01b4\u00db\2")
        buf.write("\u03b2\u03b3\7\u0086\2\2\u03b3\u03b5\3\2\2\2\u03b4\u03b1")
        buf.write("\3\2\2\2\u03b4\u03b5\3\2\2\2\u03b5\u03b6\3\2\2\2\u03b6")
        buf.write("\u03b7\5\36\20\2\u03b7U\3\2\2\2\u03b8\u03b9\t\t\2\2\u03b9")
        buf.write("W\3\2\2\2\u03ba\u03bf\5\36\20\2\u03bb\u03bc\7\u0085\2")
        buf.write("\2\u03bc\u03be\5\36\20\2\u03bd\u03bb\3\2\2\2\u03be\u03c1")
        buf.write("\3\2\2\2\u03bf\u03bd\3\2\2\2\u03bf\u03c0\3\2\2\2\u03c0")
        buf.write("Y\3\2\2\2\u03c1\u03bf\3\2\2\2\u03c2\u03c5\5\\/\2\u03c3")
        buf.write("\u03c5\5d\63\2\u03c4\u03c2\3\2\2\2\u03c4\u03c3\3\2\2\2")
        buf.write("\u03c5[\3\2\2\2\u03c6\u03cb\7~\2\2\u03c7\u03c9\5^\60\2")
        buf.write("\u03c8\u03ca\7\u0085\2\2\u03c9\u03c8\3\2\2\2\u03c9\u03ca")
        buf.write("\3\2\2\2\u03ca\u03cc\3\2\2\2\u03cb\u03c7\3\2\2\2\u03cb")
        buf.write("\u03cc\3\2\2\2\u03cc\u03cd\3\2\2\2\u03cd\u03ce\7\177\2")
        buf.write("\2\u03ce]\3\2\2\2\u03cf\u03d4\5`\61\2\u03d0\u03d1\7\u0085")
        buf.write("\2\2\u03d1\u03d3\5`\61\2\u03d2\u03d0\3\2\2\2\u03d3\u03d6")
        buf.write("\3\2\2\2\u03d4\u03d2\3\2\2\2\u03d4\u03d5\3\2\2\2\u03d5")
        buf.write("_\3\2\2\2\u03d6\u03d4\3\2\2\2\u03d7\u03dd\5\u01b4\u00db")
        buf.write("\2\u03d8\u03d9\7\u0080\2\2\u03d9\u03da\5\36\20\2\u03da")
        buf.write("\u03db\7\u0081\2\2\u03db\u03dd\3\2\2\2\u03dc\u03d7\3\2")
        buf.write("\2\2\u03dc\u03d8\3\2\2\2\u03dd\u03de\3\2\2\2\u03de\u03df")
        buf.write("\7\u0092\2\2\u03df\u03e0\5b\62\2\u03e0a\3\2\2\2\u03e1")
        buf.write("\u03e4\5\36\20\2\u03e2\u03e4\5Z.\2\u03e3\u03e1\3\2\2\2")
        buf.write("\u03e3\u03e2\3\2\2\2\u03e4c\3\2\2\2\u03e5\u03e6\7~\2\2")
        buf.write("\u03e6\u03eb\5f\64\2\u03e7\u03e8\7\u0085\2\2\u03e8\u03ea")
        buf.write("\5f\64\2\u03e9\u03e7\3\2\2\2\u03ea\u03ed\3\2\2\2\u03eb")
        buf.write("\u03e9\3\2\2\2\u03eb\u03ec\3\2\2\2\u03ec\u03ef\3\2\2\2")
        buf.write("\u03ed\u03eb\3\2\2\2\u03ee\u03f0\7\u0085\2\2\u03ef\u03ee")
        buf.write("\3\2\2\2\u03ef\u03f0\3\2\2\2\u03f0\u03f1\3\2\2\2\u03f1")
        buf.write("\u03f2\7\177\2\2\u03f2e\3\2\2\2\u03f3\u03f9\5 \21\2\u03f4")
        buf.write("\u03f5\7~\2\2\u03f5\u03f6\5X-\2\u03f6\u03f7\7\177\2\2")
        buf.write("\u03f7\u03f9\3\2\2\2\u03f8\u03f3\3\2\2\2\u03f8\u03f4\3")
        buf.write("\2\2\2\u03f9g\3\2\2\2\u03fa\u03ff\7~\2\2\u03fb\u03fd\5")
        buf.write("j\66\2\u03fc\u03fe\7\u0085\2\2\u03fd\u03fc\3\2\2\2\u03fd")
        buf.write("\u03fe\3\2\2\2\u03fe\u0400\3\2\2\2\u03ff\u03fb\3\2\2\2")
        buf.write("\u03ff\u0400\3\2\2\2\u0400\u0401\3\2\2\2\u0401\u0402\7")
        buf.write("\177\2\2\u0402i\3\2\2\2\u0403\u0408\5l\67\2\u0404\u0405")
        buf.write("\7\u0085\2\2\u0405\u0407\5l\67\2\u0406\u0404\3\2\2\2\u0407")
        buf.write("\u040a\3\2\2\2\u0408\u0406\3\2\2\2\u0408\u0409\3\2\2\2")
        buf.write("\u0409k\3\2\2\2\u040a\u0408\3\2\2\2\u040b\u0411\5H%\2")
        buf.write("\u040c\u040d\5\u01b4\u00db\2\u040d\u040e\7\u0092\2\2\u040e")
        buf.write("\u040f\5\36\20\2\u040f\u0411\3\2\2\2\u0410\u040b\3\2\2")
        buf.write("\2\u0410\u040c\3\2\2\2\u0411m\3\2\2\2\u0412\u041b\5\u01b4")
        buf.write("\u00db\2\u0413\u0415\5p9\2\u0414\u0413\3\2\2\2\u0414\u0415")
        buf.write("\3\2\2\2\u0415\u041c\3\2\2\2\u0416\u0417\7\u0096\2\2\u0417")
        buf.write("\u0419\5\u01b4\u00db\2\u0418\u041a\5p9\2\u0419\u0418\3")
        buf.write("\2\2\2\u0419\u041a\3\2\2\2\u041a\u041c\3\2\2\2\u041b\u0414")
        buf.write("\3\2\2\2\u041b\u0416\3\2\2\2\u041c\u0424\3\2\2\2\u041d")
        buf.write("\u041e\7\u0084\2\2\u041e\u0420\5\u01b4\u00db\2\u041f\u0421")
        buf.write("\5p9\2\u0420\u041f\3\2\2\2\u0420\u0421\3\2\2\2\u0421\u0423")
        buf.write("\3\2\2\2\u0422\u041d\3\2\2\2\u0423\u0426\3\2\2\2\u0424")
        buf.write("\u0422\3\2\2\2\u0424\u0425\3\2\2\2\u0425o\3\2\2\2\u0426")
        buf.write("\u0424\3\2\2\2\u0427\u042b\7\u0093\2\2\u0428\u042a\7\u0085")
        buf.write("\2\2\u0429\u0428\3\2\2\2\u042a\u042d\3\2\2\2\u042b\u0429")
        buf.write("\3\2\2\2\u042b\u042c\3\2\2\2\u042c\u042e\3\2\2\2\u042d")
        buf.write("\u042b\3\2\2\2\u042e\u042f\7\u0094\2\2\u042fq\3\2\2\2")
        buf.write("\u0430\u0435\5\b\5\2\u0431\u0434\5\u0144\u00a3\2\u0432")
        buf.write("\u0434\7\u008a\2\2\u0433\u0431\3\2\2\2\u0433\u0432\3\2")
        buf.write("\2\2\u0434\u0437\3\2\2\2\u0435\u0433\3\2\2\2\u0435\u0436")
        buf.write("\3\2\2\2\u0436\u0439\3\2\2\2\u0437\u0435\3\2\2\2\u0438")
        buf.write("\u043a\7\u0095\2\2\u0439\u0438\3\2\2\2\u0439\u043a\3\2")
        buf.write("\2\2\u043a\u043c\3\2\2\2\u043b\u043d\5t;\2\u043c\u043b")
        buf.write("\3\2\2\2\u043c\u043d\3\2\2\2\u043d\u043f\3\2\2\2\u043e")
        buf.write("\u0440\5\u01b4\u00db\2\u043f\u043e\3\2\2\2\u043f\u0440")
        buf.write("\3\2\2\2\u0440s\3\2\2\2\u0441\u0442\7~\2\2\u0442\u0447")
        buf.write("\5v<\2\u0443\u0444\7\u0085\2\2\u0444\u0446\5v<\2\u0445")
        buf.write("\u0443\3\2\2\2\u0446\u0449\3\2\2\2\u0447\u0445\3\2\2\2")
        buf.write("\u0447\u0448\3\2\2\2\u0448\u044a\3\2\2\2\u0449\u0447\3")
        buf.write("\2\2\2\u044a\u044b\7\177\2\2\u044bu\3\2\2\2\u044c\u044d")
        buf.write("\5\u01b4\u00db\2\u044d\u044e\7\u0086\2\2\u044e\u044f\5")
        buf.write("\36\20\2\u044fw\3\2\2\2\u0450\u0452\7\20\2\2\u0451\u0450")
        buf.write("\3\2\2\2\u0451\u0452\3\2\2\2\u0452\u0453\3\2\2\2\u0453")
        buf.write("\u0454\5z>\2\u0454\u0455\5\u0178\u00bd\2\u0455\u0456\5")
        buf.write("\u0082B\2\u0456y\3\2\2\2\u0457\u0458\7\u0082\2\2\u0458")
        buf.write("\u0463\7\u0083\2\2\u0459\u045a\7\u0082\2\2\u045a\u045b")
        buf.write("\5|?\2\u045b\u045c\7\u0083\2\2\u045c\u0463\3\2\2\2\u045d")
        buf.write("\u045e\7\u0082\2\2\u045e\u045f\5\u0080A\2\u045f\u0460")
        buf.write("\7\u0083\2\2\u0460\u0463\3\2\2\2\u0461\u0463\5\u01b4\u00db")
        buf.write("\2\u0462\u0457\3\2\2\2\u0462\u0459\3\2\2\2\u0462\u045d")
        buf.write("\3\2\2\2\u0462\u0461\3\2\2\2\u0463{\3\2\2\2\u0464\u0469")
        buf.write("\5~@\2\u0465\u0466\7\u0085\2\2\u0466\u0468\5~@\2\u0467")
        buf.write("\u0465\3\2\2\2\u0468\u046b\3\2\2\2\u0469\u0467\3\2\2\2")
        buf.write("\u0469\u046a\3\2\2\2\u046a}\3\2\2\2\u046b\u0469\3\2\2")
        buf.write("\2\u046c\u046e\t\4\2\2\u046d\u046c\3\2\2\2\u046d\u046e")
        buf.write("\3\2\2\2\u046e\u046f\3\2\2\2\u046f\u0470\5\6\4\2\u0470")
        buf.write("\u0471\5\u01b4\u00db\2\u0471\177\3\2\2\2\u0472\u0477\5")
        buf.write("\u01b4\u00db\2\u0473\u0474\7\u0085\2\2\u0474\u0476\5\u01b4")
        buf.write("\u00db\2\u0475\u0473\3\2\2\2\u0476\u0479\3\2\2\2\u0477")
        buf.write("\u0475\3\2\2\2\u0477\u0478\3\2\2\2\u0478\u0081\3\2\2\2")
        buf.write("\u0479\u0477\3\2\2\2\u047a\u047d\5L\'\2\u047b\u047d\5")
        buf.write("\u00acW\2\u047c\u047a\3\2\2\2\u047c\u047b\3\2\2\2\u047d")
        buf.write("\u0083\3\2\2\2\u047e\u047f\5\u0086D\2\u047f\u0480\5\u0088")
        buf.write("E\2\u0480\u0085\3\2\2\2\u0481\u0483\7\61\2\2\u0482\u0484")
        buf.write("\5\6\4\2\u0483\u0482\3\2\2\2\u0483\u0484\3\2\2\2\u0484")
        buf.write("\u0485\3\2\2\2\u0485\u0486\5\u01b4\u00db\2\u0486\u0487")
        buf.write("\7\67\2\2\u0487\u0488\5\36\20\2\u0488\u0087\3\2\2\2\u0489")
        buf.write("\u048b\5\u008aF\2\u048a\u0489\3\2\2\2\u048b\u048e\3\2")
        buf.write("\2\2\u048c\u048a\3\2\2\2\u048c\u048d\3\2\2\2\u048d\u048f")
        buf.write("\3\2\2\2\u048e\u048c\3\2\2\2\u048f\u0491\5\u0096L\2\u0490")
        buf.write("\u0492\5\u0098M\2\u0491\u0490\3\2\2\2\u0491\u0492\3\2")
        buf.write("\2\2\u0492\u0089\3\2\2\2\u0493\u0499\5\u0086D\2\u0494")
        buf.write("\u0499\5\u008cG\2\u0495\u0499\5\u008eH\2\u0496\u0499\5")
        buf.write("\u0090I\2\u0497\u0499\5\u0092J\2\u0498\u0493\3\2\2\2\u0498")
        buf.write("\u0494\3\2\2\2\u0498\u0495\3\2\2\2\u0498\u0496\3\2\2\2")
        buf.write("\u0498\u0497\3\2\2\2\u0499\u008b\3\2\2\2\u049a\u049b\7")
        buf.write(">\2\2\u049b\u049c\5\u01b4\u00db\2\u049c\u049d\7\u0092")
        buf.write("\2\2\u049d\u049e\5\36\20\2\u049e\u008d\3\2\2\2\u049f\u04a0")
        buf.write("\7p\2\2\u04a0\u04a1\5\36\20\2\u04a1\u008f\3\2\2\2\u04a2")
        buf.write("\u04a4\7=\2\2\u04a3\u04a5\5\6\4\2\u04a4\u04a3\3\2\2\2")
        buf.write("\u04a4\u04a5\3\2\2\2\u04a5\u04a6\3\2\2\2\u04a6\u04a7\5")
        buf.write("\u01b4\u00db\2\u04a7\u04a8\7\67\2\2\u04a8\u04a9\5\36\20")
        buf.write("\2\u04a9\u04aa\7F\2\2\u04aa\u04ab\5\36\20\2\u04ab\u04ac")
        buf.write("\7\'\2\2\u04ac\u04af\5\36\20\2\u04ad\u04ae\7;\2\2\u04ae")
        buf.write("\u04b0\5\u01b4\u00db\2\u04af\u04ad\3\2\2\2\u04af\u04b0")
        buf.write("\3\2\2\2\u04b0\u0091\3\2\2\2\u04b1\u04b2\7H\2\2\u04b2")
        buf.write("\u04b7\5\u0094K\2\u04b3\u04b4\7\u0085\2\2\u04b4\u04b6")
        buf.write("\5\u0094K\2\u04b5\u04b3\3\2\2\2\u04b6\u04b9\3\2\2\2\u04b7")
        buf.write("\u04b5\3\2\2\2\u04b7\u04b8\3\2\2\2\u04b8\u0093\3\2\2\2")
        buf.write("\u04b9\u04b7\3\2\2\2\u04ba\u04bc\5\36\20\2\u04bb\u04bd")
        buf.write("\t\n\2\2\u04bc\u04bb\3\2\2\2\u04bc\u04bd\3\2\2\2\u04bd")
        buf.write("\u0095\3\2\2\2\u04be\u04bf\7V\2\2\u04bf\u04c6\5\36\20")
        buf.write("\2\u04c0\u04c1\7\64\2\2\u04c1\u04c2\5\36\20\2\u04c2\u04c3")
        buf.write("\7\25\2\2\u04c3\u04c4\5\36\20\2\u04c4\u04c6\3\2\2\2\u04c5")
        buf.write("\u04be\3\2\2\2\u04c5\u04c0\3\2\2\2\u04c6\u0097\3\2\2\2")
        buf.write("\u04c7\u04c8\7;\2\2\u04c8\u04c9\5\u01b4\u00db\2\u04c9")
        buf.write("\u04ca\5\u0088E\2\u04ca\u0099\3\2\2\2\u04cb\u04cf\5\u00a6")
        buf.write("T\2\u04cc\u04cf\5\u009cO\2\u04cd\u04cf\5\u00a8U\2\u04ce")
        buf.write("\u04cb\3\2\2\2\u04ce\u04cc\3\2\2\2\u04ce\u04cd\3\2\2\2")
        buf.write("\u04cf\u009b\3\2\2\2\u04d0\u04d1\5\u00aeX\2\u04d1\u04d2")
        buf.write("\7\u0087\2\2\u04d2\u04d8\3\2\2\2\u04d3\u04d4\5\u00b6\\")
        buf.write("\2\u04d4\u04d5\7\u0087\2\2\u04d5\u04d8\3\2\2\2\u04d6\u04d8")
        buf.write("\5\u009eP\2\u04d7\u04d0\3\2\2\2\u04d7\u04d3\3\2\2\2\u04d7")
        buf.write("\u04d6\3\2\2\2\u04d8\u009d\3\2\2\2\u04d9\u04da\5\u00a0")
        buf.write("Q\2\u04da\u04db\5\u00a4S\2\u04db\u009f\3\2\2\2\u04dc\u04de")
        buf.write("\5\u00a2R\2\u04dd\u04dc\3\2\2\2\u04dd\u04de\3\2\2\2\u04de")
        buf.write("\u04df\3\2\2\2\u04df\u04e0\5\u0114\u008b\2\u04e0\u04e2")
        buf.write("\5\u01b4\u00db\2\u04e1\u04e3\5\u00e8u\2\u04e2\u04e1\3")
        buf.write("\2\2\2\u04e2\u04e3\3\2\2\2\u04e3\u04e4\3\2\2\2\u04e4\u04e6")
        buf.write("\7\u0082\2\2\u04e5\u04e7\5\u011a\u008e\2\u04e6\u04e5\3")
        buf.write("\2\2\2\u04e6\u04e7\3\2\2\2\u04e7\u04e8\3\2\2\2\u04e8\u04ea")
        buf.write("\7\u0083\2\2\u04e9\u04eb\5\u00f0y\2\u04ea\u04e9\3\2\2")
        buf.write("\2\u04ea\u04eb\3\2\2\2\u04eb\u00a1\3\2\2\2\u04ec\u04ee")
        buf.write("\t\13\2\2\u04ed\u04ef\7[\2\2\u04ee\u04ed\3\2\2\2\u04ee")
        buf.write("\u04ef\3\2\2\2\u04ef\u04f3\3\2\2\2\u04f0\u04f1\7[\2\2")
        buf.write("\u04f1\u04f3\t\13\2\2\u04f2\u04ec\3\2\2\2\u04f2\u04f0")
        buf.write("\3\2\2\2\u04f3\u00a3\3\2\2\2\u04f4\u04fa\5\u00acW\2\u04f5")
        buf.write("\u04f6\5\u0178\u00bd\2\u04f6\u04f7\5L\'\2\u04f7\u04f8")
        buf.write("\7\u0087\2\2\u04f8\u04fa\3\2\2\2\u04f9\u04f4\3\2\2\2\u04f9")
        buf.write("\u04f5\3\2\2\2\u04fa\u00a5\3\2\2\2\u04fb\u04fc\5\u01b4")
        buf.write("\u00db\2\u04fc\u04fd\7\u0086\2\2\u04fd\u04fe\5\u009aN")
        buf.write("\2\u04fe\u00a7\3\2\2\2\u04ff\u0502\5\u00acW\2\u0500\u0502")
        buf.write("\5\u00aaV\2\u0501\u04ff\3\2\2\2\u0501\u0500\3\2\2\2\u0502")
        buf.write("\u00a9\3\2\2\2\u0503\u0586\7\u0087\2\2\u0504\u0505\5\36")
        buf.write("\20\2\u0505\u0506\7\u0087\2\2\u0506\u0586\3\2\2\2\u0507")
        buf.write("\u0508\7\65\2\2\u0508\u0509\7\u0082\2\2\u0509\u050a\5")
        buf.write("\36\20\2\u050a\u050b\7\u0083\2\2\u050b\u050e\5\u00b8]")
        buf.write("\2\u050c\u050d\7%\2\2\u050d\u050f\5\u00b8]\2\u050e\u050c")
        buf.write("\3\2\2\2\u050e\u050f\3\2\2\2\u050f\u0586\3\2\2\2\u0510")
        buf.write("\u0511\7^\2\2\u0511\u0512\7\u0082\2\2\u0512\u0513\5\36")
        buf.write("\20\2\u0513\u0514\7\u0083\2\2\u0514\u0518\7~\2\2\u0515")
        buf.write("\u0517\5\u00ba^\2\u0516\u0515\3\2\2\2\u0517\u051a\3\2")
        buf.write("\2\2\u0518\u0516\3\2\2\2\u0518\u0519\3\2\2\2\u0519\u051b")
        buf.write("\3\2\2\2\u051a\u0518\3\2\2\2\u051b\u051c\7\177\2\2\u051c")
        buf.write("\u0586\3\2\2\2\u051d\u051e\7q\2\2\u051e\u051f\7\u0082")
        buf.write("\2\2\u051f\u0520\5\36\20\2\u0520\u0521\7\u0083\2\2\u0521")
        buf.write("\u0522\5\u00a8U\2\u0522\u0586\3\2\2\2\u0523\u0524\7\"")
        buf.write("\2\2\u0524\u0525\5\u00a8U\2\u0525\u0526\7q\2\2\u0526\u0527")
        buf.write("\7\u0082\2\2\u0527\u0528\5\36\20\2\u0528\u0529\7\u0083")
        buf.write("\2\2\u0529\u052a\7\u0087\2\2\u052a\u0586\3\2\2\2\u052b")
        buf.write("\u052c\7/\2\2\u052c\u052e\7\u0082\2\2\u052d\u052f\5\u00c2")
        buf.write("b\2\u052e\u052d\3\2\2\2\u052e\u052f\3\2\2\2\u052f\u0530")
        buf.write("\3\2\2\2\u0530\u0532\7\u0087\2\2\u0531\u0533\5\36\20\2")
        buf.write("\u0532\u0531\3\2\2\2\u0532\u0533\3\2\2\2\u0533\u0534\3")
        buf.write("\2\2\2\u0534\u0536\7\u0087\2\2\u0535\u0537\5\u00c4c\2")
        buf.write("\u0536\u0535\3\2\2\2\u0536\u0537\3\2\2\2\u0537\u0538\3")
        buf.write("\2\2\2\u0538\u0539\7\u0083\2\2\u0539\u0586\5\u00a8U\2")
        buf.write("\u053a\u053c\7\21\2\2\u053b\u053a\3\2\2\2\u053b\u053c")
        buf.write("\3\2\2\2\u053c\u053d\3\2\2\2\u053d\u053e\7\60\2\2\u053e")
        buf.write("\u053f\7\u0082\2\2\u053f\u0540\5\u00b0Y\2\u0540\u0541")
        buf.write("\5\u01b4\u00db\2\u0541\u0542\7\67\2\2\u0542\u0543\5\36")
        buf.write("\20\2\u0543\u0544\7\u0083\2\2\u0544\u0545\5\u00a8U\2\u0545")
        buf.write("\u0586\3\2\2\2\u0546\u0547\7\24\2\2\u0547\u0586\7\u0087")
        buf.write("\2\2\u0548\u0549\7\35\2\2\u0549\u0586\7\u0087\2\2\u054a")
        buf.write("\u054f\7\63\2\2\u054b\u0550\5\u01b4\u00db\2\u054c\u054d")
        buf.write("\7\27\2\2\u054d\u0550\5\36\20\2\u054e\u0550\7\37\2\2\u054f")
        buf.write("\u054b\3\2\2\2\u054f\u054c\3\2\2\2\u054f\u054e\3\2\2\2")
        buf.write("\u0550\u0551\3\2\2\2\u0551\u0586\7\u0087\2\2\u0552\u0554")
        buf.write("\7S\2\2\u0553\u0555\5\36\20\2\u0554\u0553\3\2\2\2\u0554")
        buf.write("\u0555\3\2\2\2\u0555\u0556\3\2\2\2\u0556\u0586\7\u0087")
        buf.write("\2\2\u0557\u0559\7`\2\2\u0558\u055a\5\36\20\2\u0559\u0558")
        buf.write("\3\2\2\2\u0559\u055a\3\2\2\2\u055a\u055b\3\2\2\2\u055b")
        buf.write("\u0586\7\u0087\2\2\u055c\u055d\7b\2\2\u055d\u0563\5\u00ac")
        buf.write("W\2\u055e\u0560\5\u00c6d\2\u055f\u0561\5\u00ceh\2\u0560")
        buf.write("\u055f\3\2\2\2\u0560\u0561\3\2\2\2\u0561\u0564\3\2\2\2")
        buf.write("\u0562\u0564\5\u00ceh\2\u0563\u055e\3\2\2\2\u0563\u0562")
        buf.write("\3\2\2\2\u0564\u0586\3\2\2\2\u0565\u0566\7\32\2\2\u0566")
        buf.write("\u0586\5\u00acW\2\u0567\u0568\7f\2\2\u0568\u0586\5\u00ac")
        buf.write("W\2\u0569\u056a\7?\2\2\u056a\u056b\7\u0082\2\2\u056b\u056c")
        buf.write("\5\36\20\2\u056c\u056d\7\u0083\2\2\u056d\u056e\5\u00a8")
        buf.write("U\2\u056e\u0586\3\2\2\2\u056f\u0570\7j\2\2\u0570\u0571")
        buf.write("\7\u0082\2\2\u0571\u0572\5\u00d0i\2\u0572\u0573\7\u0083")
        buf.write("\2\2\u0573\u0574\5\u00a8U\2\u0574\u0586\3\2\2\2\u0575")
        buf.write("\u0579\7r\2\2\u0576\u0577\7S\2\2\u0577\u057a\5\36\20\2")
        buf.write("\u0578\u057a\7\24\2\2\u0579\u0576\3\2\2\2\u0579\u0578")
        buf.write("\3\2\2\2\u057a\u057b\3\2\2\2\u057b\u0586\7\u0087\2\2\u057c")
        buf.write("\u057d\7h\2\2\u057d\u0586\5\u00acW\2\u057e\u057f\7-\2")
        buf.write("\2\u057f\u0580\7\u0082\2\2\u0580\u0581\5\u016c\u00b7\2")
        buf.write("\u0581\u0582\5\u016e\u00b8\2\u0582\u0583\7\u0083\2\2\u0583")
        buf.write("\u0584\5\u00a8U\2\u0584\u0586\3\2\2\2\u0585\u0503\3\2")
        buf.write("\2\2\u0585\u0504\3\2\2\2\u0585\u0507\3\2\2\2\u0585\u0510")
        buf.write("\3\2\2\2\u0585\u051d\3\2\2\2\u0585\u0523\3\2\2\2\u0585")
        buf.write("\u052b\3\2\2\2\u0585\u053b\3\2\2\2\u0585\u0546\3\2\2\2")
        buf.write("\u0585\u0548\3\2\2\2\u0585\u054a\3\2\2\2\u0585\u0552\3")
        buf.write("\2\2\2\u0585\u0557\3\2\2\2\u0585\u055c\3\2\2\2\u0585\u0565")
        buf.write("\3\2\2\2\u0585\u0567\3\2\2\2\u0585\u0569\3\2\2\2\u0585")
        buf.write("\u056f\3\2\2\2\u0585\u0575\3\2\2\2\u0585\u057c\3\2\2\2")
        buf.write("\u0585\u057e\3\2\2\2\u0586\u00ab\3\2\2\2\u0587\u0589\7")
        buf.write("~\2\2\u0588\u058a\5\u00c0a\2\u0589\u0588\3\2\2\2\u0589")
        buf.write("\u058a\3\2\2\2\u058a\u058b\3\2\2\2\u058b\u058c\7\177\2")
        buf.write("\2\u058c\u00ad\3\2\2\2\u058d\u0592\7j\2\2\u058e\u0592")
        buf.write("\7Q\2\2\u058f\u0590\7Q\2\2\u0590\u0592\7P\2\2\u0591\u058d")
        buf.write("\3\2\2\2\u0591\u058e\3\2\2\2\u0591\u058f\3\2\2\2\u0591")
        buf.write("\u0592\3\2\2\2\u0592\u0593\3\2\2\2\u0593\u0594\5\u00b0")
        buf.write("Y\2\u0594\u0599\5\u00b2Z\2\u0595\u0596\7\u0085\2\2\u0596")
        buf.write("\u0598\5\u00b2Z\2\u0597\u0595\3\2\2\2\u0598\u059b\3\2")
        buf.write("\2\2\u0599\u0597\3\2\2\2\u0599\u059a\3\2\2\2\u059a\u05a1")
        buf.write("\3\2\2\2\u059b\u0599\3\2\2\2\u059c\u059d\7-\2\2\u059d")
        buf.write("\u059e\5\u016c\u00b7\2\u059e\u059f\5\u016e\u00b8\2\u059f")
        buf.write("\u05a1\3\2\2\2\u05a0\u0591\3\2\2\2\u05a0\u059c\3\2\2\2")
        buf.write("\u05a1\u00af\3\2\2\2\u05a2\u05a5\7k\2\2\u05a3\u05a5\5")
        buf.write("\6\4\2\u05a4\u05a2\3\2\2\2\u05a4\u05a3\3\2\2\2\u05a5\u00b1")
        buf.write("\3\2\2\2\u05a6\u05ac\5\u01b4\u00db\2\u05a7\u05a9\7\u0092")
        buf.write("\2\2\u05a8\u05aa\7Q\2\2\u05a9\u05a8\3\2\2\2\u05a9\u05aa")
        buf.write("\3\2\2\2\u05aa\u05ab\3\2\2\2\u05ab\u05ad\5\u00b4[\2\u05ac")
        buf.write("\u05a7\3\2\2\2\u05ac\u05ad\3\2\2\2\u05ad\u00b3\3\2\2\2")
        buf.write("\u05ae\u05b2\5\36\20\2\u05af\u05b2\5\u0146\u00a4\2\u05b0")
        buf.write("\u05b2\5\u0176\u00bc\2\u05b1\u05ae\3\2\2\2\u05b1\u05af")
        buf.write("\3\2\2\2\u05b1\u05b0\3\2\2\2\u05b2\u00b5\3\2\2\2\u05b3")
        buf.write("\u05b4\7\34\2\2\u05b4\u05b5\5\6\4\2\u05b5\u05b6\5\u010a")
        buf.write("\u0086\2\u05b6\u00b7\3\2\2\2\u05b7\u05ba\5\u00acW\2\u05b8")
        buf.write("\u05ba\5\u00aaV\2\u05b9\u05b7\3\2\2\2\u05b9\u05b8\3\2")
        buf.write("\2\2\u05ba\u00b9\3\2\2\2\u05bb\u05bd\5\u00bc_\2\u05bc")
        buf.write("\u05bb\3\2\2\2\u05bd\u05be\3\2\2\2\u05be\u05bc\3\2\2\2")
        buf.write("\u05be\u05bf\3\2\2\2\u05bf\u05c0\3\2\2\2\u05c0\u05c1\5")
        buf.write("\u00c0a\2\u05c1\u00bb\3\2\2\2\u05c2\u05c3\7\27\2\2\u05c3")
        buf.write("\u05c5\5\36\20\2\u05c4\u05c6\5\u00be`\2\u05c5\u05c4\3")
        buf.write("\2\2\2\u05c5\u05c6\3\2\2\2\u05c6\u05c7\3\2\2\2\u05c7\u05c8")
        buf.write("\7\u0086\2\2\u05c8\u05cc\3\2\2\2\u05c9\u05ca\7\37\2\2")
        buf.write("\u05ca\u05cc\7\u0086\2\2\u05cb\u05c2\3\2\2\2\u05cb\u05c9")
        buf.write("\3\2\2\2\u05cc\u00bd\3\2\2\2\u05cd\u05ce\7o\2\2\u05ce")
        buf.write("\u05cf\5\36\20\2\u05cf\u00bf\3\2\2\2\u05d0\u05d2\5\u009a")
        buf.write("N\2\u05d1\u05d0\3\2\2\2\u05d2\u05d3\3\2\2\2\u05d3\u05d1")
        buf.write("\3\2\2\2\u05d3\u05d4\3\2\2\2\u05d4\u00c1\3\2\2\2\u05d5")
        buf.write("\u05df\5\u00aeX\2\u05d6\u05db\5\36\20\2\u05d7\u05d8\7")
        buf.write("\u0085\2\2\u05d8\u05da\5\36\20\2\u05d9\u05d7\3\2\2\2\u05da")
        buf.write("\u05dd\3\2\2\2\u05db\u05d9\3\2\2\2\u05db\u05dc\3\2\2\2")
        buf.write("\u05dc\u05df\3\2\2\2\u05dd\u05db\3\2\2\2\u05de\u05d5\3")
        buf.write("\2\2\2\u05de\u05d6\3\2\2\2\u05df\u00c3\3\2\2\2\u05e0\u05e5")
        buf.write("\5\36\20\2\u05e1\u05e2\7\u0085\2\2\u05e2\u05e4\5\36\20")
        buf.write("\2\u05e3\u05e1\3\2\2\2\u05e4\u05e7\3\2\2\2\u05e5\u05e3")
        buf.write("\3\2\2\2\u05e5\u05e6\3\2\2\2\u05e6\u00c5\3\2\2\2\u05e7")
        buf.write("\u05e5\3\2\2\2\u05e8\u05ec\5\u00c8e\2\u05e9\u05eb\5\u00c8")
        buf.write("e\2\u05ea\u05e9\3\2\2\2\u05eb\u05ee\3\2\2\2\u05ec\u05ea")
        buf.write("\3\2\2\2\u05ec\u05ed\3\2\2\2\u05ed\u05f0\3\2\2\2\u05ee")
        buf.write("\u05ec\3\2\2\2\u05ef\u05f1\5\u00caf\2\u05f0\u05ef\3\2")
        buf.write("\2\2\u05f0\u05f1\3\2\2\2\u05f1\u05f4\3\2\2\2\u05f2\u05f4")
        buf.write("\5\u00caf\2\u05f3\u05e8\3\2\2\2\u05f3\u05f2\3\2\2\2\u05f4")
        buf.write("\u00c7\3\2\2\2\u05f5\u05f6\7\30\2\2\u05f6\u05f7\7\u0082")
        buf.write("\2\2\u05f7\u05f9\5\26\f\2\u05f8\u05fa\5\u01b4\u00db\2")
        buf.write("\u05f9\u05f8\3\2\2\2\u05f9\u05fa\3\2\2\2\u05fa\u05fb\3")
        buf.write("\2\2\2\u05fb\u05fd\7\u0083\2\2\u05fc\u05fe\5\u00ccg\2")
        buf.write("\u05fd\u05fc\3\2\2\2\u05fd\u05fe\3\2\2\2\u05fe\u05ff\3")
        buf.write("\2\2\2\u05ff\u0600\5\u00acW\2\u0600\u00c9\3\2\2\2\u0601")
        buf.write("\u0603\7\30\2\2\u0602\u0604\5\u00ccg\2\u0603\u0602\3\2")
        buf.write("\2\2\u0603\u0604\3\2\2\2\u0604\u0605\3\2\2\2\u0605\u0606")
        buf.write("\5\u00acW\2\u0606\u00cb\3\2\2\2\u0607\u0608\7o\2\2\u0608")
        buf.write("\u0609\7\u0082\2\2\u0609\u060a\5\36\20\2\u060a\u060b\7")
        buf.write("\u0083\2\2\u060b\u00cd\3\2\2\2\u060c\u060d\7,\2\2\u060d")
        buf.write("\u060e\5\u00acW\2\u060e\u00cf\3\2\2\2\u060f\u0612\5\u00ae")
        buf.write("X\2\u0610\u0612\5\36\20\2\u0611\u060f\3\2\2\2\u0611\u0610")
        buf.write("\3\2\2\2\u0612\u00d1\3\2\2\2\u0613\u0614\7B\2\2\u0614")
        buf.write("\u0615\5\u00d4k\2\u0615\u0617\5\u00d6l\2\u0616\u0618\7")
        buf.write("\u0087\2\2\u0617\u0616\3\2\2\2\u0617\u0618\3\2\2\2\u0618")
        buf.write("\u00d3\3\2\2\2\u0619\u061e\5\u01b4\u00db\2\u061a\u061b")
        buf.write("\7\u0084\2\2\u061b\u061d\5\u01b4\u00db\2\u061c\u061a\3")
        buf.write("\2\2\2\u061d\u0620\3\2\2\2\u061e\u061c\3\2\2\2\u061e\u061f")
        buf.write("\3\2\2\2\u061f\u00d5\3\2\2\2\u0620\u061e\3\2\2\2\u0621")
        buf.write("\u0623\7~\2\2\u0622\u0624\5\u00d8m\2\u0623\u0622\3\2\2")
        buf.write("\2\u0623\u0624\3\2\2\2\u0624\u0626\3\2\2\2\u0625\u0627")
        buf.write("\5\u00dco\2\u0626\u0625\3\2\2\2\u0626\u0627\3\2\2\2\u0627")
        buf.write("\u0629\3\2\2\2\u0628\u062a\5\u00e0q\2\u0629\u0628\3\2")
        buf.write("\2\2\u0629\u062a\3\2\2\2\u062a\u062b\3\2\2\2\u062b\u062c")
        buf.write("\7\177\2\2\u062c\u00d7\3\2\2\2\u062d\u062f\5\u00dan\2")
        buf.write("\u062e\u062d\3\2\2\2\u062f\u0630\3\2\2\2\u0630\u062e\3")
        buf.write("\2\2\2\u0630\u0631\3\2\2\2\u0631\u00d9\3\2\2\2\u0632\u0633")
        buf.write("\7*\2\2\u0633\u0634\7\f\2\2\u0634\u0635\5\u01b4\u00db")
        buf.write("\2\u0635\u0636\7\u0087\2\2\u0636\u00db\3\2\2\2\u0637\u0639")
        buf.write("\5\u00dep\2\u0638\u0637\3\2\2\2\u0639\u063a\3\2\2\2\u063a")
        buf.write("\u0638\3\2\2\2\u063a\u063b\3\2\2\2\u063b\u00dd\3\2\2\2")
        buf.write("\u063c\u063d\7j\2\2\u063d\u063e\5\u01b4\u00db\2\u063e")
        buf.write("\u063f\7\u0092\2\2\u063f\u0640\5\4\3\2\u0640\u0641\7\u0087")
        buf.write("\2\2\u0641\u064c\3\2\2\2\u0642\u0643\7j\2\2\u0643\u0644")
        buf.write("\5\4\3\2\u0644\u0645\7\u0087\2\2\u0645\u064c\3\2\2\2\u0646")
        buf.write("\u0647\7j\2\2\u0647\u0648\7[\2\2\u0648\u0649\5\4\3\2\u0649")
        buf.write("\u064a\7\u0087\2\2\u064a\u064c\3\2\2\2\u064b\u063c\3\2")
        buf.write("\2\2\u064b\u0642\3\2\2\2\u064b\u0646\3\2\2\2\u064c\u00df")
        buf.write("\3\2\2\2\u064d\u064f\5\u00e2r\2\u064e\u064d\3\2\2\2\u064f")
        buf.write("\u0650\3\2\2\2\u0650\u064e\3\2\2\2\u0650\u0651\3\2\2\2")
        buf.write("\u0651\u00e1\3\2\2\2\u0652\u0655\5\u00d2j\2\u0653\u0655")
        buf.write("\5\u00e4s\2\u0654\u0652\3\2\2\2\u0654\u0653\3\2\2\2\u0655")
        buf.write("\u00e3\3\2\2\2\u0656\u0658\5\u0160\u00b1\2\u0657\u0656")
        buf.write("\3\2\2\2\u0657\u0658\3\2\2\2\u0658\u065a\3\2\2\2\u0659")
        buf.write("\u065b\5\u0102\u0082\2\u065a\u0659\3\2\2\2\u065a\u065b")
        buf.write("\3\2\2\2\u065b\u0661\3\2\2\2\u065c\u0662\5\u0190\u00c9")
        buf.write("\2\u065d\u0662\5\u0192\u00ca\2\u065e\u0662\5\u0194\u00cb")
        buf.write("\2\u065f\u0662\5\u0196\u00cc\2\u0660\u0662\5\u0198\u00cd")
        buf.write("\2\u0661\u065c\3\2\2\2\u0661\u065d\3\2\2\2\u0661\u065e")
        buf.write("\3\2\2\2\u0661\u065f\3\2\2\2\u0661\u0660\3\2\2\2\u0662")
        buf.write("\u00e5\3\2\2\2\u0663\u0664\5\u01b4\u00db\2\u0664\u0665")
        buf.write("\7\u0096\2\2\u0665\u0667\5\u01b4\u00db\2\u0666\u0668\5")
        buf.write("\30\r\2\u0667\u0666\3\2\2\2\u0667\u0668\3\2\2\2\u0668")
        buf.write("\u00e7\3\2\2\2\u0669\u066a\7\u0093\2\2\u066a\u066f\5\u00ea")
        buf.write("v\2\u066b\u066c\7\u0085\2\2\u066c\u066e\5\u00eav\2\u066d")
        buf.write("\u066b\3\2\2\2\u066e\u0671\3\2\2\2\u066f\u066d\3\2\2\2")
        buf.write("\u066f\u0670\3\2\2\2\u0670\u0672\3\2\2\2\u0671\u066f\3")
        buf.write("\2\2\2\u0672\u0673\7\u0094\2\2\u0673\u00e9\3\2\2\2\u0674")
        buf.write("\u0676\5\u0160\u00b1\2\u0675\u0674\3\2\2\2\u0675\u0676")
        buf.write("\3\2\2\2\u0676\u0677\3\2\2\2\u0677\u0678\5\u01b4\u00db")
        buf.write("\2\u0678\u00eb\3\2\2\2\u0679\u067a\7\u0086\2\2\u067a\u067f")
        buf.write("\5\26\f\2\u067b\u067c\7\u0085\2\2\u067c\u067e\5\4\3\2")
        buf.write("\u067d\u067b\3\2\2\2\u067e\u0681\3\2\2\2\u067f\u067d\3")
        buf.write("\2\2\2\u067f\u0680\3\2\2\2\u0680\u00ed\3\2\2\2\u0681\u067f")
        buf.write("\3\2\2\2\u0682\u0687\5\4\3\2\u0683\u0684\7\u0085\2\2\u0684")
        buf.write("\u0686\5\4\3\2\u0685\u0683\3\2\2\2\u0686\u0689\3\2\2\2")
        buf.write("\u0687\u0685\3\2\2\2\u0687\u0688\3\2\2\2\u0688\u00ef\3")
        buf.write("\2\2\2\u0689\u0687\3\2\2\2\u068a\u068c\5\u00f2z\2\u068b")
        buf.write("\u068a\3\2\2\2\u068c\u068d\3\2\2\2\u068d\u068b\3\2\2\2")
        buf.write("\u068d\u068e\3\2\2\2\u068e\u00f1\3\2\2\2\u068f\u0690\7")
        buf.write("p\2\2\u0690\u0691\5\u01b4\u00db\2\u0691\u0692\7\u0086")
        buf.write("\2\2\u0692\u0693\5\u00f4{\2\u0693\u00f3\3\2\2\2\u0694")
        buf.write("\u069f\5\u00fa~\2\u0695\u0698\5\u00f6|\2\u0696\u0697\7")
        buf.write("\u0085\2\2\u0697\u0699\5\u00f8}\2\u0698\u0696\3\2\2\2")
        buf.write("\u0698\u0699\3\2\2\2\u0699\u069c\3\2\2\2\u069a\u069b\7")
        buf.write("\u0085\2\2\u069b\u069d\5\u00fa~\2\u069c\u069a\3\2\2\2")
        buf.write("\u069c\u069d\3\2\2\2\u069d\u069f\3\2\2\2\u069e\u0694\3")
        buf.write("\2\2\2\u069e\u0695\3\2\2\2\u069f\u00f5\3\2\2\2\u06a0\u06a8")
        buf.write("\5\26\f\2\u06a1\u06a3\7\33\2\2\u06a2\u06a4\7\u0095\2\2")
        buf.write("\u06a3\u06a2\3\2\2\2\u06a3\u06a4\3\2\2\2\u06a4\u06a8\3")
        buf.write("\2\2\2\u06a5\u06a8\7]\2\2\u06a6\u06a8\7g\2\2\u06a7\u06a0")
        buf.write("\3\2\2\2\u06a7\u06a1\3\2\2\2\u06a7\u06a5\3\2\2\2\u06a7")
        buf.write("\u06a6\3\2\2\2\u06a8\u00f7\3\2\2\2\u06a9\u06ae\5\4\3\2")
        buf.write("\u06aa\u06ab\7\u0085\2\2\u06ab\u06ad\5\4\3\2\u06ac\u06aa")
        buf.write("\3\2\2\2\u06ad\u06b0\3\2\2\2\u06ae\u06ac\3\2\2\2\u06ae")
        buf.write("\u06af\3\2\2\2\u06af\u00f9\3\2\2\2\u06b0\u06ae\3\2\2\2")
        buf.write("\u06b1\u06b2\7C\2\2\u06b2\u06b3\7\u0082\2\2\u06b3\u06b4")
        buf.write("\7\u0083\2\2\u06b4\u00fb\3\2\2\2\u06b5\u06b7\7~\2\2\u06b6")
        buf.write("\u06b8\5\u00fe\u0080\2\u06b7\u06b6\3\2\2\2\u06b7\u06b8")
        buf.write("\3\2\2\2\u06b8\u06b9\3\2\2\2\u06b9\u06ba\7\177\2\2\u06ba")
        buf.write("\u00fd\3\2\2\2\u06bb\u06bd\5\u0100\u0081\2\u06bc\u06bb")
        buf.write("\3\2\2\2\u06bd\u06be\3\2\2\2\u06be\u06bc\3\2\2\2\u06be")
        buf.write("\u06bf\3\2\2\2\u06bf\u00ff\3\2\2\2\u06c0\u06c2\5\u0160")
        buf.write("\u00b1\2\u06c1\u06c0\3\2\2\2\u06c1\u06c2\3\2\2\2\u06c2")
        buf.write("\u06c4\3\2\2\2\u06c3\u06c5\5\u0102\u0082\2\u06c4\u06c3")
        buf.write("\3\2\2\2\u06c4\u06c5\3\2\2\2\u06c5\u06c8\3\2\2\2\u06c6")
        buf.write("\u06c9\5\u0106\u0084\2\u06c7\u06c9\5\u01a4\u00d3\2\u06c8")
        buf.write("\u06c6\3\2\2\2\u06c8\u06c7\3\2\2\2\u06c9\u0101\3\2\2\2")
        buf.write("\u06ca\u06cc\5\u0104\u0083\2\u06cb\u06ca\3\2\2\2\u06cc")
        buf.write("\u06cd\3\2\2\2\u06cd\u06cb\3\2\2\2\u06cd\u06ce\3\2\2\2")
        buf.write("\u06ce\u0103\3\2\2\2\u06cf\u06d0\t\f\2\2\u06d0\u0105\3")
        buf.write("\2\2\2\u06d1\u06e5\5\u01a0\u00d1\2\u06d2\u06e5\5\u0108")
        buf.write("\u0085\2\u06d3\u06e5\5\u019a\u00ce\2\u06d4\u06da\5\u0136")
        buf.write("\u009c\2\u06d5\u06db\5\u013a\u009e\2\u06d6\u06d7\5\u0178")
        buf.write("\u00bd\2\u06d7\u06d8\5L\'\2\u06d8\u06d9\7\u0087\2\2\u06d9")
        buf.write("\u06db\3\2\2\2\u06da\u06d5\3\2\2\2\u06da\u06d6\3\2\2\2")
        buf.write("\u06db\u06e5\3\2\2\2\u06dc\u06e5\5\u01a6\u00d4\2\u06dd")
        buf.write("\u06de\7m\2\2\u06de\u06e5\5\u01a8\u00d5\2\u06df\u06e5")
        buf.write("\5\u0190\u00c9\2\u06e0\u06e5\5\u0192\u00ca\2\u06e1\u06e5")
        buf.write("\5\u0194\u00cb\2\u06e2\u06e5\5\u0196\u00cc\2\u06e3\u06e5")
        buf.write("\5\u0198\u00cd\2\u06e4\u06d1\3\2\2\2\u06e4\u06d2\3\2\2")
        buf.write("\2\u06e4\u06d3\3\2\2\2\u06e4\u06d4\3\2\2\2\u06e4\u06dc")
        buf.write("\3\2\2\2\u06e4\u06dd\3\2\2\2\u06e4\u06df\3\2\2\2\u06e4")
        buf.write("\u06e0\3\2\2\2\u06e4\u06e1\3\2\2\2\u06e4\u06e2\3\2\2\2")
        buf.write("\u06e4\u06e3\3\2\2\2\u06e5\u0107\3\2\2\2\u06e6\u06ec\7")
        buf.write("Q\2\2\u06e7\u06e8\7P\2\2\u06e8\u06ec\7Q\2\2\u06e9\u06ea")
        buf.write("\7Q\2\2\u06ea\u06ec\7P\2\2\u06eb\u06e6\3\2\2\2\u06eb\u06e7")
        buf.write("\3\2\2\2\u06eb\u06e9\3\2\2\2\u06eb\u06ec\3\2\2\2\u06ec")
        buf.write("\u06ed\3\2\2\2\u06ed\u06f7\5\6\4\2\u06ee\u06ef\5\4\3\2")
        buf.write("\u06ef\u06f0\7\u0084\2\2\u06f0\u06f1\5\u01a2\u00d2\2\u06f1")
        buf.write("\u06f8\3\2\2\2\u06f2\u06f8\5\u01a8\u00d5\2\u06f3\u06f8")
        buf.write("\5\u019e\u00d0\2\u06f4\u06f8\5\u01a2\u00d2\2\u06f5\u06f8")
        buf.write("\5\u01ac\u00d7\2\u06f6\u06f8\5\u019c\u00cf\2\u06f7\u06ee")
        buf.write("\3\2\2\2\u06f7\u06f2\3\2\2\2\u06f7\u06f3\3\2\2\2\u06f7")
        buf.write("\u06f4\3\2\2\2\u06f7\u06f5\3\2\2\2\u06f7\u06f6\3\2\2\2")
        buf.write("\u06f8\u0109\3\2\2\2\u06f9\u06fe\5\u010c\u0087\2\u06fa")
        buf.write("\u06fb\7\u0085\2\2\u06fb\u06fd\5\u010c\u0087\2\u06fc\u06fa")
        buf.write("\3\2\2\2\u06fd\u0700\3\2\2\2\u06fe\u06fc\3\2\2\2\u06fe")
        buf.write("\u06ff\3\2\2\2\u06ff\u010b\3\2\2\2\u0700\u06fe\3\2\2\2")
        buf.write("\u0701\u0702\5\u01b4\u00db\2\u0702\u0703\7\u0092\2\2\u0703")
        buf.write("\u0704\5\36\20\2\u0704\u010d\3\2\2\2\u0705\u070a\5\u0110")
        buf.write("\u0089\2\u0706\u0707\7\u0085\2\2\u0707\u0709\5\u0110\u0089")
        buf.write("\2\u0708\u0706\3\2\2\2\u0709\u070c\3\2\2\2\u070a\u0708")
        buf.write("\3\2\2\2\u070a\u070b\3\2\2\2\u070b\u010f\3\2\2\2\u070c")
        buf.write("\u070a\3\2\2\2\u070d\u0710\5\u01b4\u00db\2\u070e\u070f")
        buf.write("\7\u0092\2\2\u070f\u0711\5\u0112\u008a\2\u0710\u070e\3")
        buf.write("\2\2\2\u0710\u0711\3\2\2\2\u0711\u0111\3\2\2\2\u0712\u0715")
        buf.write("\5\36\20\2\u0713\u0715\5\u0146\u00a4\2\u0714\u0712\3\2")
        buf.write("\2\2\u0714\u0713\3\2\2\2\u0715\u0113\3\2\2\2\u0716\u0719")
        buf.write("\5\6\4\2\u0717\u0719\7m\2\2\u0718\u0716\3\2\2\2\u0718")
        buf.write("\u0717\3\2\2\2\u0719\u0115\3\2\2\2\u071a\u071b\5\4\3\2")
        buf.write("\u071b\u0117\3\2\2\2\u071c\u071f\5\u00acW\2\u071d\u071f")
        buf.write("\7\u0087\2\2\u071e\u071c\3\2\2\2\u071e\u071d\3\2\2\2\u071f")
        buf.write("\u0119\3\2\2\2\u0720\u0727\5\u0122\u0092\2\u0721\u0724")
        buf.write("\5\u011c\u008f\2\u0722\u0723\7\u0085\2\2\u0723\u0725\5")
        buf.write("\u0122\u0092\2\u0724\u0722\3\2\2\2\u0724\u0725\3\2\2\2")
        buf.write("\u0725\u0727\3\2\2\2\u0726\u0720\3\2\2\2\u0726\u0721\3")
        buf.write("\2\2\2\u0727\u011b\3\2\2\2\u0728\u072d\5\u011e\u0090\2")
        buf.write("\u0729\u072a\7\u0085\2\2\u072a\u072c\5\u011e\u0090\2\u072b")
        buf.write("\u0729\3\2\2\2\u072c\u072f\3\2\2\2\u072d\u072b\3\2\2\2")
        buf.write("\u072d\u072e\3\2\2\2\u072e\u011d\3\2\2\2\u072f\u072d\3")
        buf.write("\2\2\2\u0730\u0732\5\u0160\u00b1\2\u0731\u0730\3\2\2\2")
        buf.write("\u0731\u0732\3\2\2\2\u0732\u0734\3\2\2\2\u0733\u0735\5")
        buf.write("\u0120\u0091\2\u0734\u0733\3\2\2\2\u0734\u0735\3\2\2\2")
        buf.write("\u0735\u0736\3\2\2\2\u0736\u0739\5\u01ae\u00d8\2\u0737")
        buf.write("\u0739\7\r\2\2\u0738\u0731\3\2\2\2\u0738\u0737\3\2\2\2")
        buf.write("\u0739\u011f\3\2\2\2\u073a\u0743\7Q\2\2\u073b\u0743\7")
        buf.write("I\2\2\u073c\u0743\7\67\2\2\u073d\u073e\7Q\2\2\u073e\u0743")
        buf.write("\7_\2\2\u073f\u0740\7\67\2\2\u0740\u0743\7_\2\2\u0741")
        buf.write("\u0743\7_\2\2\u0742\u073a\3\2\2\2\u0742\u073b\3\2\2\2")
        buf.write("\u0742\u073c\3\2\2\2\u0742\u073d\3\2\2\2\u0742\u073f\3")
        buf.write("\2\2\2\u0742\u0741\3\2\2\2\u0743\u0121\3\2\2\2\u0744\u0746")
        buf.write("\5\u0160\u00b1\2\u0745\u0744\3\2\2\2\u0745\u0746\3\2\2")
        buf.write("\2\u0746\u0747\3\2\2\2\u0747\u0748\7K\2\2\u0748\u0749")
        buf.write("\5\u0142\u00a2\2\u0749\u074a\5\u01b4\u00db\2\u074a\u0123")
        buf.write("\3\2\2\2\u074b\u074d\5\u0160\u00b1\2\u074c\u074b\3\2\2")
        buf.write("\2\u074c\u074d\3\2\2\2\u074d\u074f\3\2\2\2\u074e\u0750")
        buf.write("\5\u012a\u0096\2\u074f\u074e\3\2\2\2\u074f\u0750\3\2\2")
        buf.write("\2\u0750\u075b\3\2\2\2\u0751\u0752\7\62\2\2\u0752\u0754")
        buf.write("\5\u012c\u0097\2\u0753\u0755\5\u0128\u0095\2\u0754\u0753")
        buf.write("\3\2\2\2\u0754\u0755\3\2\2\2\u0755\u075c\3\2\2\2\u0756")
        buf.write("\u0757\7W\2\2\u0757\u0759\5\u012c\u0097\2\u0758\u075a")
        buf.write("\5\u0126\u0094\2\u0759\u0758\3\2\2\2\u0759\u075a\3\2\2")
        buf.write("\2\u075a\u075c\3\2\2\2\u075b\u0751\3\2\2\2\u075b\u0756")
        buf.write("\3\2\2\2\u075c\u0125\3\2\2\2\u075d\u075f\5\u0160\u00b1")
        buf.write("\2\u075e\u075d\3\2\2\2\u075e\u075f\3\2\2\2\u075f\u0761")
        buf.write("\3\2\2\2\u0760\u0762\5\u012a\u0096\2\u0761\u0760\3\2\2")
        buf.write("\2\u0761\u0762\3\2\2\2\u0762\u0763\3\2\2\2\u0763\u0764")
        buf.write("\7\62\2\2\u0764\u0765\5\u012c\u0097\2\u0765\u0127\3\2")
        buf.write("\2\2\u0766\u0768\5\u0160\u00b1\2\u0767\u0766\3\2\2\2\u0767")
        buf.write("\u0768\3\2\2\2\u0768\u076a\3\2\2\2\u0769\u076b\5\u012a")
        buf.write("\u0096\2\u076a\u0769\3\2\2\2\u076a\u076b\3\2\2\2\u076b")
        buf.write("\u076c\3\2\2\2\u076c\u076d\7W\2\2\u076d\u076e\5\u012c")
        buf.write("\u0097\2\u076e\u0129\3\2\2\2\u076f\u0777\7N\2\2\u0770")
        buf.write("\u0777\7:\2\2\u0771\u0777\7M\2\2\u0772\u0773\7N\2\2\u0773")
        buf.write("\u0777\7:\2\2\u0774\u0775\7:\2\2\u0775\u0777\7N\2\2\u0776")
        buf.write("\u076f\3\2\2\2\u0776\u0770\3\2\2\2\u0776\u0771\3\2\2\2")
        buf.write("\u0776\u0772\3\2\2\2\u0776\u0774\3\2\2\2\u0777\u012b\3")
        buf.write("\2\2\2\u0778\u077b\5\u00acW\2\u0779\u077b\7\u0087\2\2")
        buf.write("\u077a\u0778\3\2\2\2\u077a\u0779\3\2\2\2\u077b\u012d\3")
        buf.write("\2\2\2\u077c\u077e\5\u0160\u00b1\2\u077d\u077c\3\2\2\2")
        buf.write("\u077d\u077e\3\2\2\2\u077e\u0787\3\2\2\2\u077f\u0780\7")
        buf.write("\13\2\2\u0780\u0781\5\u00acW\2\u0781\u0782\5\u0132\u009a")
        buf.write("\2\u0782\u0788\3\2\2\2\u0783\u0784\7R\2\2\u0784\u0785")
        buf.write("\5\u00acW\2\u0785\u0786\5\u0130\u0099\2\u0786\u0788\3")
        buf.write("\2\2\2\u0787\u077f\3\2\2\2\u0787\u0783\3\2\2\2\u0788\u012f")
        buf.write("\3\2\2\2\u0789\u078b\5\u0160\u00b1\2\u078a\u0789\3\2\2")
        buf.write("\2\u078a\u078b\3\2\2\2\u078b\u078c\3\2\2\2\u078c\u078d")
        buf.write("\7\13\2\2\u078d\u078e\5\u00acW\2\u078e\u0131\3\2\2\2\u078f")
        buf.write("\u0791\5\u0160\u00b1\2\u0790\u078f\3\2\2\2\u0790\u0791")
        buf.write("\3\2\2\2\u0791\u0792\3\2\2\2\u0792\u0793\7R\2\2\u0793")
        buf.write("\u0794\5\u00acW\2\u0794\u0133\3\2\2\2\u0795\u07ac\7\u0088")
        buf.write("\2\2\u0796\u07ac\7\u0089\2\2\u0797\u07ac\7\u0090\2\2\u0798")
        buf.write("\u07ac\7\u0091\2\2\u0799\u07ac\7\u0098\2\2\u079a\u07ac")
        buf.write("\7\u0099\2\2\u079b\u07ac\7a\2\2\u079c\u07ac\7+\2\2\u079d")
        buf.write("\u07ac\7\u008a\2\2\u079e\u07ac\7\u008b\2\2\u079f\u07ac")
        buf.write("\7\u008c\2\2\u07a0\u07ac\7\u008d\2\2\u07a1\u07ac\7\u008e")
        buf.write("\2\2\u07a2\u07ac\7\u008f\2\2\u07a3\u07ac\7\u00a9\2\2\u07a4")
        buf.write("\u07ac\5\u017a\u00be\2\u07a5\u07ac\7\u009d\2\2\u07a6\u07ac")
        buf.write("\7\u009e\2\2\u07a7\u07ac\7\u0094\2\2\u07a8\u07ac\7\u0093")
        buf.write("\2\2\u07a9\u07ac\7\u00a0\2\2\u07aa\u07ac\7\u009f\2\2\u07ab")
        buf.write("\u0795\3\2\2\2\u07ab\u0796\3\2\2\2\u07ab\u0797\3\2\2\2")
        buf.write("\u07ab\u0798\3\2\2\2\u07ab\u0799\3\2\2\2\u07ab\u079a\3")
        buf.write("\2\2\2\u07ab\u079b\3\2\2\2\u07ab\u079c\3\2\2\2\u07ab\u079d")
        buf.write("\3\2\2\2\u07ab\u079e\3\2\2\2\u07ab\u079f\3\2\2\2\u07ab")
        buf.write("\u07a0\3\2\2\2\u07ab\u07a1\3\2\2\2\u07ab\u07a2\3\2\2\2")
        buf.write("\u07ab\u07a3\3\2\2\2\u07ab\u07a4\3\2\2\2\u07ab\u07a5\3")
        buf.write("\2\2\2\u07ab\u07a6\3\2\2\2\u07ab\u07a7\3\2\2\2\u07ab\u07a8")
        buf.write("\3\2\2\2\u07ab\u07a9\3\2\2\2\u07ab\u07aa\3\2\2\2\u07ac")
        buf.write("\u0135\3\2\2\2\u07ad\u07ae\t\r\2\2\u07ae\u07af\7G\2\2")
        buf.write("\u07af\u07b0\5\6\4\2\u07b0\u07b1\7\u0082\2\2\u07b1\u07b2")
        buf.write("\5\u01ae\u00d8\2\u07b2\u07b3\7\u0083\2\2\u07b3\u0137\3")
        buf.write("\2\2\2\u07b4\u07b5\7\u0086\2\2\u07b5\u07b6\t\16\2\2\u07b6")
        buf.write("\u07b8\7\u0082\2\2\u07b7\u07b9\5\32\16\2\u07b8\u07b7\3")
        buf.write("\2\2\2\u07b8\u07b9\3\2\2\2\u07b9\u07ba\3\2\2\2\u07ba\u07bb")
        buf.write("\7\u0083\2\2\u07bb\u0139\3\2\2\2\u07bc\u07bf\5\u00acW")
        buf.write("\2\u07bd\u07bf\7\u0087\2\2\u07be\u07bc\3\2\2\2\u07be\u07bd")
        buf.write("\3\2\2\2\u07bf\u013b\3\2\2\2\u07c0\u07c1\7\u0086\2\2\u07c1")
        buf.write("\u07c2\5\u00eex\2\u07c2\u013d\3\2\2\2\u07c3\u07c7\7~\2")
        buf.write("\2\u07c4\u07c6\5\u0140\u00a1\2\u07c5\u07c4\3\2\2\2\u07c6")
        buf.write("\u07c9\3\2\2\2\u07c7\u07c5\3\2\2\2\u07c7\u07c8\3\2\2\2")
        buf.write("\u07c8\u07ca\3\2\2\2\u07c9\u07c7\3\2\2\2\u07ca\u07cb\7")
        buf.write("\177\2\2\u07cb\u013f\3\2\2\2\u07cc\u07ce\5\u0160\u00b1")
        buf.write("\2\u07cd\u07cc\3\2\2\2\u07cd\u07ce\3\2\2\2\u07ce\u07d0")
        buf.write("\3\2\2\2\u07cf\u07d1\5\u0102\u0082\2\u07d0\u07cf\3\2\2")
        buf.write("\2\u07d0\u07d1\3\2\2\2\u07d1\u07dc\3\2\2\2\u07d2\u07dd")
        buf.write("\5\u0106\u0084\2\u07d3\u07d4\7-\2\2\u07d4\u07d6\5\6\4")
        buf.write("\2\u07d5\u07d7\5\u0174\u00bb\2\u07d6\u07d5\3\2\2\2\u07d7")
        buf.write("\u07d8\3\2\2\2\u07d8\u07d6\3\2\2\2\u07d8\u07d9\3\2\2\2")
        buf.write("\u07d9\u07da\3\2\2\2\u07da\u07db\7\u0087\2\2\u07db\u07dd")
        buf.write("\3\2\2\2\u07dc\u07d2\3\2\2\2\u07dc\u07d3\3\2\2\2\u07dd")
        buf.write("\u0141\3\2\2\2\u07de\u07e6\5\b\5\2\u07df\u07e1\t\17\2")
        buf.write("\2\u07e0\u07df\3\2\2\2\u07e1\u07e4\3\2\2\2\u07e2\u07e0")
        buf.write("\3\2\2\2\u07e2\u07e3\3\2\2\2\u07e3\u07e5\3\2\2\2\u07e4")
        buf.write("\u07e2\3\2\2\2\u07e5\u07e7\5\u0144\u00a3\2\u07e6\u07e2")
        buf.write("\3\2\2\2\u07e7\u07e8\3\2\2\2\u07e8\u07e6\3\2\2\2\u07e8")
        buf.write("\u07e9\3\2\2\2\u07e9\u0143\3\2\2\2\u07ea\u07ee\7\u0080")
        buf.write("\2\2\u07eb\u07ed\7\u0085\2\2\u07ec\u07eb\3\2\2\2\u07ed")
        buf.write("\u07f0\3\2\2\2\u07ee\u07ec\3\2\2\2\u07ee\u07ef\3\2\2\2")
        buf.write("\u07ef\u07f1\3\2\2\2\u07f0\u07ee\3\2\2\2\u07f1\u07f2\7")
        buf.write("\u0081\2\2\u07f2\u0145\3\2\2\2\u07f3\u07ff\7~\2\2\u07f4")
        buf.write("\u07f9\5\u0112\u008a\2\u07f5\u07f6\7\u0085\2\2\u07f6\u07f8")
        buf.write("\5\u0112\u008a\2\u07f7\u07f5\3\2\2\2\u07f8\u07fb\3\2\2")
        buf.write("\2\u07f9\u07f7\3\2\2\2\u07f9\u07fa\3\2\2\2\u07fa\u07fd")
        buf.write("\3\2\2\2\u07fb\u07f9\3\2\2\2\u07fc\u07fe\7\u0085\2\2\u07fd")
        buf.write("\u07fc\3\2\2\2\u07fd\u07fe\3\2\2\2\u07fe\u0800\3\2\2\2")
        buf.write("\u07ff\u07f4\3\2\2\2\u07ff\u0800\3\2\2\2\u0800\u0801\3")
        buf.write("\2\2\2\u0801\u0802\7\177\2\2\u0802\u0147\3\2\2\2\u0803")
        buf.write("\u0804\7\u0093\2\2\u0804\u0809\5\u014a\u00a6\2\u0805\u0806")
        buf.write("\7\u0085\2\2\u0806\u0808\5\u014a\u00a6\2\u0807\u0805\3")
        buf.write("\2\2\2\u0808\u080b\3\2\2\2\u0809\u0807\3\2\2\2\u0809\u080a")
        buf.write("\3\2\2\2\u080a\u080c\3\2\2\2\u080b\u0809\3\2\2\2\u080c")
        buf.write("\u080d\7\u0094\2\2\u080d\u0149\3\2\2\2\u080e\u0810\5\u0160")
        buf.write("\u00b1\2\u080f\u080e\3\2\2\2\u080f\u0810\3\2\2\2\u0810")
        buf.write("\u0812\3\2\2\2\u0811\u0813\5\u014c\u00a7\2\u0812\u0811")
        buf.write("\3\2\2\2\u0812\u0813\3\2\2\2\u0813\u0814\3\2\2\2\u0814")
        buf.write("\u0815\5\u01b4\u00db\2\u0815\u014b\3\2\2\2\u0816\u0817")
        buf.write("\t\20\2\2\u0817\u014d\3\2\2\2\u0818\u0819\7\u0086\2\2")
        buf.write("\u0819\u081a\5\u00eex\2\u081a\u014f\3\2\2\2\u081b\u081f")
        buf.write("\7~\2\2\u081c\u081e\5\u0152\u00aa\2\u081d\u081c\3\2\2")
        buf.write("\2\u081e\u0821\3\2\2\2\u081f\u081d\3\2\2\2\u081f\u0820")
        buf.write("\3\2\2\2\u0820\u0822\3\2\2\2\u0821\u081f\3\2\2\2\u0822")
        buf.write("\u0823\7\177\2\2\u0823\u0151\3\2\2\2\u0824\u0826\5\u0160")
        buf.write("\u00b1\2\u0825\u0824\3\2\2\2\u0825\u0826\3\2\2\2\u0826")
        buf.write("\u0828\3\2\2\2\u0827\u0829\7C\2\2\u0828\u0827\3\2\2\2")
        buf.write("\u0828\u0829\3\2\2\2\u0829\u0869\3\2\2\2\u082a\u082c\7")
        buf.write("h\2\2\u082b\u082a\3\2\2\2\u082b\u082c\3\2\2\2\u082c\u0832")
        buf.write("\3\2\2\2\u082d\u0833\7Q\2\2\u082e\u082f\7Q\2\2\u082f\u0833")
        buf.write("\7P\2\2\u0830\u0831\7P\2\2\u0831\u0833\7Q\2\2\u0832\u082d")
        buf.write("\3\2\2\2\u0832\u082e\3\2\2\2\u0832\u0830\3\2\2\2\u0832")
        buf.write("\u0833\3\2\2\2\u0833\u0834\3\2\2\2\u0834\u0850\5\6\4\2")
        buf.write("\u0835\u0837\5\u01b4\u00db\2\u0836\u0838\5\u00e8u\2\u0837")
        buf.write("\u0836\3\2\2\2\u0837\u0838\3\2\2\2\u0838\u0839\3\2\2\2")
        buf.write("\u0839\u083b\7\u0082\2\2\u083a\u083c\5\u011a\u008e\2\u083b")
        buf.write("\u083a\3\2\2\2\u083b\u083c\3\2\2\2\u083c\u083d\3\2\2\2")
        buf.write("\u083d\u083f\7\u0083\2\2\u083e\u0840\5\u00f0y\2\u083f")
        buf.write("\u083e\3\2\2\2\u083f\u0840\3\2\2\2\u0840\u0841\3\2\2\2")
        buf.write("\u0841\u0842\7\u0087\2\2\u0842\u0851\3\2\2\2\u0843\u0844")
        buf.write("\5\u01b4\u00db\2\u0844\u0845\7~\2\2\u0845\u0846\5\u0154")
        buf.write("\u00ab\2\u0846\u0847\7\177\2\2\u0847\u0851\3\2\2\2\u0848")
        buf.write("\u0849\7_\2\2\u0849\u084a\7\u0080\2\2\u084a\u084b\5\u011a")
        buf.write("\u008e\2\u084b\u084c\7\u0081\2\2\u084c\u084d\7~\2\2\u084d")
        buf.write("\u084e\5\u0154\u00ab\2\u084e\u084f\7\177\2\2\u084f\u0851")
        buf.write("\3\2\2\2\u0850\u0835\3\2\2\2\u0850\u0843\3\2\2\2\u0850")
        buf.write("\u0848\3\2\2\2\u0851\u086a\3\2\2\2\u0852\u0854\7h\2\2")
        buf.write("\u0853\u0852\3\2\2\2\u0853\u0854\3\2\2\2\u0854\u0855\3")
        buf.write("\2\2\2\u0855\u0856\7m\2\2\u0856\u0858\5\u01b4\u00db\2")
        buf.write("\u0857\u0859\5\u00e8u\2\u0858\u0857\3\2\2\2\u0858\u0859")
        buf.write("\3\2\2\2\u0859\u085a\3\2\2\2\u085a\u085c\7\u0082\2\2\u085b")
        buf.write("\u085d\5\u011a\u008e\2\u085c\u085b\3\2\2\2\u085c\u085d")
        buf.write("\3\2\2\2\u085d\u085e\3\2\2\2\u085e\u0860\7\u0083\2\2\u085f")
        buf.write("\u0861\5\u00f0y\2\u0860\u085f\3\2\2\2\u0860\u0861\3\2")
        buf.write("\2\2\u0861\u0862\3\2\2\2\u0862\u0863\7\u0087\2\2\u0863")
        buf.write("\u086a\3\2\2\2\u0864\u0865\7(\2\2\u0865\u0866\5\6\4\2")
        buf.write("\u0866\u0867\5\u01b4\u00db\2\u0867\u0868\7\u0087\2\2\u0868")
        buf.write("\u086a\3\2\2\2\u0869\u082b\3\2\2\2\u0869\u0853\3\2\2\2")
        buf.write("\u0869\u0864\3\2\2\2\u086a\u0153\3\2\2\2\u086b\u086d\5")
        buf.write("\u0160\u00b1\2\u086c\u086b\3\2\2\2\u086c\u086d\3\2\2\2")
        buf.write("\u086d\u0880\3\2\2\2\u086e\u086f\7\62\2\2\u086f\u0875")
        buf.write("\7\u0087\2\2\u0870\u0872\5\u0160\u00b1\2\u0871\u0870\3")
        buf.write("\2\2\2\u0871\u0872\3\2\2\2\u0872\u0873\3\2\2\2\u0873\u0874")
        buf.write("\7W\2\2\u0874\u0876\7\u0087\2\2\u0875\u0871\3\2\2\2\u0875")
        buf.write("\u0876\3\2\2\2\u0876\u0881\3\2\2\2\u0877\u0878\7W\2\2")
        buf.write("\u0878\u087e\7\u0087\2\2\u0879\u087b\5\u0160\u00b1\2\u087a")
        buf.write("\u0879\3\2\2\2\u087a\u087b\3\2\2\2\u087b\u087c\3\2\2\2")
        buf.write("\u087c\u087d\7\62\2\2\u087d\u087f\7\u0087\2\2\u087e\u087a")
        buf.write("\3\2\2\2\u087e\u087f\3\2\2\2\u087f\u0881\3\2\2\2\u0880")
        buf.write("\u086e\3\2\2\2\u0880\u0877\3\2\2\2\u0881\u0155\3\2\2\2")
        buf.write("\u0882\u0883\7\u0086\2\2\u0883\u0884\5\6\4\2\u0884\u0157")
        buf.write("\3\2\2\2\u0885\u0891\7~\2\2\u0886\u088b\5\u015a\u00ae")
        buf.write("\2\u0887\u0888\7\u0085\2\2\u0888\u088a\5\u015a\u00ae\2")
        buf.write("\u0889\u0887\3\2\2\2\u088a\u088d\3\2\2\2\u088b\u0889\3")
        buf.write("\2\2\2\u088b\u088c\3\2\2\2\u088c\u088f\3\2\2\2\u088d\u088b")
        buf.write("\3\2\2\2\u088e\u0890\7\u0085\2\2\u088f\u088e\3\2\2\2\u088f")
        buf.write("\u0890\3\2\2\2\u0890\u0892\3\2\2\2\u0891\u0886\3\2\2\2")
        buf.write("\u0891\u0892\3\2\2\2\u0892\u0893\3\2\2\2\u0893\u0894\7")
        buf.write("\177\2\2\u0894\u0159\3\2\2\2\u0895\u0897\5\u0160\u00b1")
        buf.write("\2\u0896\u0895\3\2\2\2\u0896\u0897\3\2\2\2\u0897\u0898")
        buf.write("\3\2\2\2\u0898\u089b\5\u01b4\u00db\2\u0899\u089a\7\u0092")
        buf.write("\2\2\u089a\u089c\5\36\20\2\u089b\u0899\3\2\2\2\u089b\u089c")
        buf.write("\3\2\2\2\u089c\u015b\3\2\2\2\u089d\u089e\7\u0080\2\2\u089e")
        buf.write("\u089f\5\u015e\u00b0\2\u089f\u08a0\7\u0086\2\2\u08a0\u08a2")
        buf.write("\5\u0166\u00b4\2\u08a1\u08a3\7\u0085\2\2\u08a2\u08a1\3")
        buf.write("\2\2\2\u08a2\u08a3\3\2\2\2\u08a3\u08a4\3\2\2\2\u08a4\u08a5")
        buf.write("\7\u0081\2\2\u08a5\u015d\3\2\2\2\u08a6\u08a9\5\u018e\u00c8")
        buf.write("\2\u08a7\u08a9\5\u01b4\u00db\2\u08a8\u08a6\3\2\2\2\u08a8")
        buf.write("\u08a7\3\2\2\2\u08a9\u015f\3\2\2\2\u08aa\u08ac\5\u0162")
        buf.write("\u00b2\2\u08ab\u08aa\3\2\2\2\u08ac\u08ad\3\2\2\2\u08ad")
        buf.write("\u08ab\3\2\2\2\u08ad\u08ae\3\2\2\2\u08ae\u0161\3\2\2\2")
        buf.write("\u08af\u08b3\7\u0080\2\2\u08b0\u08b1\5\u0164\u00b3\2\u08b1")
        buf.write("\u08b2\7\u0086\2\2\u08b2\u08b4\3\2\2\2\u08b3\u08b0\3\2")
        buf.write("\2\2\u08b3\u08b4\3\2\2\2\u08b4\u08b5\3\2\2\2\u08b5\u08b7")
        buf.write("\5\u0166\u00b4\2\u08b6\u08b8\7\u0085\2\2\u08b7\u08b6\3")
        buf.write("\2\2\2\u08b7\u08b8\3\2\2\2\u08b8\u08b9\3\2\2\2\u08b9\u08ba")
        buf.write("\7\u0081\2\2\u08ba\u0163\3\2\2\2\u08bb\u08be\5\u018e\u00c8")
        buf.write("\2\u08bc\u08be\5\u01b4\u00db\2\u08bd\u08bb\3\2\2\2\u08bd")
        buf.write("\u08bc\3\2\2\2\u08be\u0165\3\2\2\2\u08bf\u08c4\5\u0168")
        buf.write("\u00b5\2\u08c0\u08c1\7\u0085\2\2\u08c1\u08c3\5\u0168\u00b5")
        buf.write("\2\u08c2\u08c0\3\2\2\2\u08c3\u08c6\3\2\2\2\u08c4\u08c2")
        buf.write("\3\2\2\2\u08c4\u08c5\3\2\2\2\u08c5\u0167\3\2\2\2\u08c6")
        buf.write("\u08c4\3\2\2\2\u08c7\u08d4\5\4\3\2\u08c8\u08d1\7\u0082")
        buf.write("\2\2\u08c9\u08ce\5\u016a\u00b6\2\u08ca\u08cb\7\u0085\2")
        buf.write("\2\u08cb\u08cd\5\u016a\u00b6\2\u08cc\u08ca\3\2\2\2\u08cd")
        buf.write("\u08d0\3\2\2\2\u08ce\u08cc\3\2\2\2\u08ce\u08cf\3\2\2\2")
        buf.write("\u08cf\u08d2\3\2\2\2\u08d0\u08ce\3\2\2\2\u08d1\u08c9\3")
        buf.write("\2\2\2\u08d1\u08d2\3\2\2\2\u08d2\u08d3\3\2\2\2\u08d3\u08d5")
        buf.write("\7\u0083\2\2\u08d4\u08c8\3\2\2\2\u08d4\u08d5\3\2\2\2\u08d5")
        buf.write("\u0169\3\2\2\2\u08d6\u08d7\5\u01b4\u00db\2\u08d7\u08d8")
        buf.write("\7\u0086\2\2\u08d8\u08da\3\2\2\2\u08d9\u08d6\3\2\2\2\u08d9")
        buf.write("\u08da\3\2\2\2\u08da\u08db\3\2\2\2\u08db\u08dc\5\36\20")
        buf.write("\2\u08dc\u016b\3\2\2\2\u08dd\u08e0\5\16\b\2\u08de\u08e0")
        buf.write("\5\26\f\2\u08df\u08dd\3\2\2\2\u08df\u08de\3\2\2\2\u08e0")
        buf.write("\u08e5\3\2\2\2\u08e1\u08e4\5\u0144\u00a3\2\u08e2\u08e4")
        buf.write("\7\u0095\2\2\u08e3\u08e1\3\2\2\2\u08e3\u08e2\3\2\2\2\u08e4")
        buf.write("\u08e7\3\2\2\2\u08e5\u08e3\3\2\2\2\u08e5\u08e6\3\2\2\2")
        buf.write("\u08e6\u08e8\3\2\2\2\u08e7\u08e5\3\2\2\2\u08e8\u08e9\7")
        buf.write("\u008a\2\2\u08e9\u08ed\3\2\2\2\u08ea\u08eb\7m\2\2\u08eb")
        buf.write("\u08ed\7\u008a\2\2\u08ec\u08df\3\2\2\2\u08ec\u08ea\3\2")
        buf.write("\2\2\u08ed\u016d\3\2\2\2\u08ee\u08f3\5\u0170\u00b9\2\u08ef")
        buf.write("\u08f0\7\u0085\2\2\u08f0\u08f2\5\u0170\u00b9\2\u08f1\u08ef")
        buf.write("\3\2\2\2\u08f2\u08f5\3\2\2\2\u08f3\u08f1\3\2\2\2\u08f3")
        buf.write("\u08f4\3\2\2\2\u08f4\u016f\3\2\2\2\u08f5\u08f3\3\2\2\2")
        buf.write("\u08f6\u08f7\5\u01b4\u00db\2\u08f7\u08f8\7\u0092\2\2\u08f8")
        buf.write("\u08f9\5\u0172\u00ba\2\u08f9\u0171\3\2\2\2\u08fa\u08fc")
        buf.write("\7\u008d\2\2\u08fb\u08fa\3\2\2\2\u08fb\u08fc\3\2\2\2\u08fc")
        buf.write("\u08fd\3\2\2\2\u08fd\u0900\5\36\20\2\u08fe\u0900\5\u0176")
        buf.write("\u00bc\2\u08ff\u08fb\3\2\2\2\u08ff\u08fe\3\2\2\2\u0900")
        buf.write("\u0173\3\2\2\2\u0901\u0902\5\u01b4\u00db\2\u0902\u0903")
        buf.write("\7\u0080\2\2\u0903\u0904\5\36\20\2\u0904\u0905\7\u0081")
        buf.write("\2\2\u0905\u0175\3\2\2\2\u0906\u0907\7Z\2\2\u0907\u0908")
        buf.write("\5\6\4\2\u0908\u0909\7\u0080\2\2\u0909\u090a\5\36\20\2")
        buf.write("\u090a\u090b\7\u0081\2\2\u090b\u0924\3\2\2\2\u090c\u090e")
        buf.write("\7Z\2\2\u090d\u090f\5\6\4\2\u090e\u090d\3\2\2\2\u090e")
        buf.write("\u090f\3\2\2\2\u090f\u0910\3\2\2\2\u0910\u0912\7\u0080")
        buf.write("\2\2\u0911\u0913\5\36\20\2\u0912\u0911\3\2\2\2\u0912\u0913")
        buf.write("\3\2\2\2\u0913\u0914\3\2\2\2\u0914\u0915\7\u0081\2\2\u0915")
        buf.write("\u0916\7~\2\2\u0916\u091b\5\36\20\2\u0917\u0918\7\u0085")
        buf.write("\2\2\u0918\u091a\5\36\20\2\u0919\u0917\3\2\2\2\u091a\u091d")
        buf.write("\3\2\2\2\u091b\u0919\3\2\2\2\u091b\u091c\3\2\2\2\u091c")
        buf.write("\u091f\3\2\2\2\u091d\u091b\3\2\2\2\u091e\u0920\7\u0085")
        buf.write("\2\2\u091f\u091e\3\2\2\2\u091f\u0920\3\2\2\2\u0920\u0921")
        buf.write("\3\2\2\2\u0921\u0922\7\177\2\2\u0922\u0924\3\2\2\2\u0923")
        buf.write("\u0906\3\2\2\2\u0923\u090c\3\2\2\2\u0924\u0177\3\2\2\2")
        buf.write("\u0925\u0926\7\u0092\2\2\u0926\u0927\7\u0094\2\2\u0927")
        buf.write("\u0928\6\u00bd\2\3\u0928\u0179\3\2\2\2\u0929\u092a\7\u0094")
        buf.write("\2\2\u092a\u092b\7\u0094\2\2\u092b\u092c\6\u00be\3\3\u092c")
        buf.write("\u017b\3\2\2\2\u092d\u092e\7\u0094\2\2\u092e\u092f\7\u00a0")
        buf.write("\2\2\u092f\u0930\6\u00bf\4\3\u0930\u017d\3\2\2\2\u0931")
        buf.write("\u093a\5\u0180\u00c1\2\u0932\u093a\5\u0182\u00c2\2\u0933")
        buf.write("\u093a\7u\2\2\u0934\u093a\7v\2\2\u0935\u093a\7w\2\2\u0936")
        buf.write("\u093a\7x\2\2\u0937\u093a\7y\2\2\u0938\u093a\7D\2\2\u0939")
        buf.write("\u0931\3\2\2\2\u0939\u0932\3\2\2\2\u0939\u0933\3\2\2\2")
        buf.write("\u0939\u0934\3\2\2\2\u0939\u0935\3\2\2\2\u0939\u0936\3")
        buf.write("\2\2\2\u0939\u0937\3\2\2\2\u0939\u0938\3\2\2\2\u093a\u017f")
        buf.write("\3\2\2\2\u093b\u093c\t\21\2\2\u093c\u0181\3\2\2\2\u093d")
        buf.write("\u0942\5\u0184\u00c3\2\u093e\u0942\5\u0186\u00c4\2\u093f")
        buf.write("\u0942\7z\2\2\u0940\u0942\7{\2\2\u0941\u093d\3\2\2\2\u0941")
        buf.write("\u093e\3\2\2\2\u0941\u093f\3\2\2\2\u0941\u0940\3\2\2\2")
        buf.write("\u0942\u0183\3\2\2\2\u0943\u0947\7|\2\2\u0944\u0946\5")
        buf.write("\u0188\u00c5\2\u0945\u0944\3\2\2\2\u0946\u0949\3\2\2\2")
        buf.write("\u0947\u0945\3\2\2\2\u0947\u0948\3\2\2\2\u0948\u094a\3")
        buf.write("\2\2\2\u0949\u0947\3\2\2\2\u094a\u094b\7\u00b1\2\2\u094b")
        buf.write("\u0185\3\2\2\2\u094c\u0950\7}\2\2\u094d\u094f\5\u018a")
        buf.write("\u00c6\2\u094e\u094d\3\2\2\2\u094f\u0952\3\2\2\2\u0950")
        buf.write("\u094e\3\2\2\2\u0950\u0951\3\2\2\2\u0951\u0953\3\2\2\2")
        buf.write("\u0952\u0950\3\2\2\2\u0953\u0954\7\u00b1\2\2\u0954\u0187")
        buf.write("\3\2\2\2\u0955\u095a\5\u018c\u00c7\2\u0956\u095a\7\u00ad")
        buf.write("\2\2\u0957\u095a\7\u00af\2\2\u0958\u095a\7\u00b2\2\2\u0959")
        buf.write("\u0955\3\2\2\2\u0959\u0956\3\2\2\2\u0959\u0957\3\2\2\2")
        buf.write("\u0959\u0958\3\2\2\2\u095a\u0189\3\2\2\2\u095b\u0960\5")
        buf.write("\u018c\u00c7\2\u095c\u0960\7\u00ad\2\2\u095d\u0960\7\u00b0")
        buf.write("\2\2\u095e\u0960\7\u00b3\2\2\u095f\u095b\3\2\2\2\u095f")
        buf.write("\u095c\3\2\2\2\u095f\u095d\3\2\2\2\u095f\u095e\3\2\2\2")
        buf.write("\u0960\u018b\3\2\2\2\u0961\u0966\5\36\20\2\u0962\u0963")
        buf.write("\7\u0085\2\2\u0963\u0965\5\36\20\2\u0964\u0962\3\2\2\2")
        buf.write("\u0965\u0968\3\2\2\2\u0966\u0964\3\2\2\2\u0966\u0967\3")
        buf.write("\2\2\2\u0967\u096f\3\2\2\2\u0968\u0966\3\2\2\2\u0969\u096b")
        buf.write("\7\u0086\2\2\u096a\u096c\7\u00b5\2\2\u096b\u096a\3\2\2")
        buf.write("\2\u096c\u096d\3\2\2\2\u096d\u096b\3\2\2\2\u096d\u096e")
        buf.write("\3\2\2\2\u096e\u0970\3\2\2\2\u096f\u0969\3\2\2\2\u096f")
        buf.write("\u0970\3\2\2\2\u0970\u018d\3\2\2\2\u0971\u0972\t\22\2")
        buf.write("\2\u0972\u018f\3\2\2\2\u0973\u0974\7\33\2\2\u0974\u0976")
        buf.write("\5\u01b4\u00db\2\u0975\u0977\5\u00e8u\2\u0976\u0975\3")
        buf.write("\2\2\2\u0976\u0977\3\2\2\2\u0977\u0979\3\2\2\2\u0978\u097a")
        buf.write("\5\u00ecw\2\u0979\u0978\3\2\2\2\u0979\u097a\3\2\2\2\u097a")
        buf.write("\u097c\3\2\2\2\u097b\u097d\5\u00f0y\2\u097c\u097b\3\2")
        buf.write("\2\2\u097c\u097d\3\2\2\2\u097d\u097e\3\2\2\2\u097e\u0980")
        buf.write("\5\u00fc\177\2\u097f\u0981\7\u0087\2\2\u0980\u097f\3\2")
        buf.write("\2\2\u0980\u0981\3\2\2\2\u0981\u0191\3\2\2\2\u0982\u0984")
        buf.write("\t\23\2\2\u0983\u0982\3\2\2\2\u0983\u0984\3\2\2\2\u0984")
        buf.write("\u0985\3\2\2\2\u0985\u0986\7]\2\2\u0986\u0988\5\u01b4")
        buf.write("\u00db\2\u0987\u0989\5\u00e8u\2\u0988\u0987\3\2\2\2\u0988")
        buf.write("\u0989\3\2\2\2\u0989\u098b\3\2\2\2\u098a\u098c\5\u013c")
        buf.write("\u009f\2\u098b\u098a\3\2\2\2\u098b\u098c\3\2\2\2\u098c")
        buf.write("\u098e\3\2\2\2\u098d\u098f\5\u00f0y\2\u098e\u098d\3\2")
        buf.write("\2\2\u098e\u098f\3\2\2\2\u098f\u0990\3\2\2\2\u0990\u0992")
        buf.write("\5\u013e\u00a0\2\u0991\u0993\7\u0087\2\2\u0992\u0991\3")
        buf.write("\2\2\2\u0992\u0993\3\2\2\2\u0993\u0193\3\2\2\2\u0994\u0995")
        buf.write("\79\2\2\u0995\u0997\5\u01b4\u00db\2\u0996\u0998\5\u0148")
        buf.write("\u00a5\2\u0997\u0996\3\2\2\2\u0997\u0998\3\2\2\2\u0998")
        buf.write("\u099a\3\2\2\2\u0999\u099b\5\u014e\u00a8\2\u099a\u0999")
        buf.write("\3\2\2\2\u099a\u099b\3\2\2\2\u099b\u099d\3\2\2\2\u099c")
        buf.write("\u099e\5\u00f0y\2\u099d\u099c\3\2\2\2\u099d\u099e\3\2")
        buf.write("\2\2\u099e\u099f\3\2\2\2\u099f\u09a1\5\u00fc\177\2\u09a0")
        buf.write("\u09a2\7\u0087\2\2\u09a1\u09a0\3\2\2\2\u09a1\u09a2\3\2")
        buf.write("\2\2\u09a2\u0195\3\2\2\2\u09a3\u09a4\7&\2\2\u09a4\u09a6")
        buf.write("\5\u01b4\u00db\2\u09a5\u09a7\5\u0156\u00ac\2\u09a6\u09a5")
        buf.write("\3\2\2\2\u09a6\u09a7\3\2\2\2\u09a7\u09a8\3\2\2\2\u09a8")
        buf.write("\u09aa\5\u0158\u00ad\2\u09a9\u09ab\7\u0087\2\2\u09aa\u09a9")
        buf.write("\3\2\2\2\u09aa\u09ab\3\2\2\2\u09ab\u0197\3\2\2\2\u09ac")
        buf.write("\u09ad\7 \2\2\u09ad\u09ae\5\u0114\u008b\2\u09ae\u09b0")
        buf.write("\5\u01b4\u00db\2\u09af\u09b1\5\u0148\u00a5\2\u09b0\u09af")
        buf.write("\3\2\2\2\u09b0\u09b1\3\2\2\2\u09b1\u09b2\3\2\2\2\u09b2")
        buf.write("\u09b4\7\u0082\2\2\u09b3\u09b5\5\u011a\u008e\2\u09b4\u09b3")
        buf.write("\3\2\2\2\u09b4\u09b5\3\2\2\2\u09b5\u09b6\3\2\2\2\u09b6")
        buf.write("\u09b8\7\u0083\2\2\u09b7\u09b9\5\u00f0y\2\u09b8\u09b7")
        buf.write("\3\2\2\2\u09b8\u09b9\3\2\2\2\u09b9\u09ba\3\2\2\2\u09ba")
        buf.write("\u09bb\7\u0087\2\2\u09bb\u0199\3\2\2\2\u09bc\u09bd\7(")
        buf.write("\2\2\u09bd\u09c6\5\6\4\2\u09be\u09bf\5\u010e\u0088\2\u09bf")
        buf.write("\u09c0\7\u0087\2\2\u09c0\u09c7\3\2\2\2\u09c1\u09c2\5\u0116")
        buf.write("\u008c\2\u09c2\u09c3\7~\2\2\u09c3\u09c4\5\u012e\u0098")
        buf.write("\2\u09c4\u09c5\7\177\2\2\u09c5\u09c7\3\2\2\2\u09c6\u09be")
        buf.write("\3\2\2\2\u09c6\u09c1\3\2\2\2\u09c7\u019b\3\2\2\2\u09c8")
        buf.write("\u09c9\5\u010e\u0088\2\u09c9\u09ca\7\u0087\2\2\u09ca\u019d")
        buf.write("\3\2\2\2\u09cb\u09d9\5\u0116\u008c\2\u09cc\u09cd\7~\2")
        buf.write("\2\u09cd\u09ce\5\u0124\u0093\2\u09ce\u09d3\7\177\2\2\u09cf")
        buf.write("\u09d0\7\u0092\2\2\u09d0\u09d1\5\u0112\u008a\2\u09d1\u09d2")
        buf.write("\7\u0087\2\2\u09d2\u09d4\3\2\2\2\u09d3\u09cf\3\2\2\2\u09d3")
        buf.write("\u09d4\3\2\2\2\u09d4\u09da\3\2\2\2\u09d5\u09d6\5\u0178")
        buf.write("\u00bd\2\u09d6\u09d7\5L\'\2\u09d7\u09d8\7\u0087\2\2\u09d8")
        buf.write("\u09da\3\2\2\2\u09d9\u09cc\3\2\2\2\u09d9\u09d5\3\2\2\2")
        buf.write("\u09da\u019f\3\2\2\2\u09db\u09dc\7\34\2\2\u09dc\u09dd")
        buf.write("\5\6\4\2\u09dd\u09de\5\u010a\u0086\2\u09de\u09df\7\u0087")
        buf.write("\2\2\u09df\u01a1\3\2\2\2\u09e0\u09e1\7_\2\2\u09e1\u09e2")
        buf.write("\7\u0080\2\2\u09e2\u09e3\5\u011a\u008e\2\u09e3\u09ec\7")
        buf.write("\u0081\2\2\u09e4\u09e5\7~\2\2\u09e5\u09e6\5\u0124\u0093")
        buf.write("\2\u09e6\u09e7\7\177\2\2\u09e7\u09ed\3\2\2\2\u09e8\u09e9")
        buf.write("\5\u0178\u00bd\2\u09e9\u09ea\5L\'\2\u09ea\u09eb\7\u0087")
        buf.write("\2\2\u09eb\u09ed\3\2\2\2\u09ec\u09e4\3\2\2\2\u09ec\u09e8")
        buf.write("\3\2\2\2\u09ed\u01a3\3\2\2\2\u09ee\u09ef\7\u0091\2\2\u09ef")
        buf.write("\u09f0\5\u01b4\u00db\2\u09f0\u09f1\7\u0082\2\2\u09f1\u09f2")
        buf.write("\7\u0083\2\2\u09f2\u09f3\5\u013a\u009e\2\u09f3\u01a5\3")
        buf.write("\2\2\2\u09f4\u09f5\5\u01b4\u00db\2\u09f5\u09f7\7\u0082")
        buf.write("\2\2\u09f6\u09f8\5\u011a\u008e\2\u09f7\u09f6\3\2\2\2\u09f7")
        buf.write("\u09f8\3\2\2\2\u09f8\u09f9\3\2\2\2\u09f9\u09fb\7\u0083")
        buf.write("\2\2\u09fa\u09fc\5\u0138\u009d\2\u09fb\u09fa\3\2\2\2\u09fb")
        buf.write("\u09fc\3\2\2\2\u09fc\u09fd\3\2\2\2\u09fd\u09fe\5\u013a")
        buf.write("\u009e\2\u09fe\u01a7\3\2\2\2\u09ff\u0a01\5\u01aa\u00d6")
        buf.write("\2\u0a00\u0a02\5\u00e8u\2\u0a01\u0a00\3\2\2\2\u0a01\u0a02")
        buf.write("\3\2\2\2\u0a02\u0a03\3\2\2\2\u0a03\u0a05\7\u0082\2\2\u0a04")
        buf.write("\u0a06\5\u011a\u008e\2\u0a05\u0a04\3\2\2\2\u0a05\u0a06")
        buf.write("\3\2\2\2\u0a06\u0a07\3\2\2\2\u0a07\u0a09\7\u0083\2\2\u0a08")
        buf.write("\u0a0a\5\u00f0y\2\u0a09\u0a08\3\2\2\2\u0a09\u0a0a\3\2")
        buf.write("\2\2\u0a0a\u0a10\3\2\2\2\u0a0b\u0a11\5\u0118\u008d\2\u0a0c")
        buf.write("\u0a0d\5\u0178\u00bd\2\u0a0d\u0a0e\5L\'\2\u0a0e\u0a0f")
        buf.write("\7\u0087\2\2\u0a0f\u0a11\3\2\2\2\u0a10\u0a0b\3\2\2\2\u0a10")
        buf.write("\u0a0c\3\2\2\2\u0a11\u01a9\3\2\2\2\u0a12\u0a18\5\u01b4")
        buf.write("\u00db\2\u0a13\u0a14\5\u01b4\u00db\2\u0a14\u0a15\7\u0096")
        buf.write("\2\2\u0a15\u0a16\5\u01b4\u00db\2\u0a16\u0a18\3\2\2\2\u0a17")
        buf.write("\u0a12\3\2\2\2\u0a17\u0a13\3\2\2\2\u0a18\u0a20\3\2\2\2")
        buf.write("\u0a19\u0a1b\5\30\r\2\u0a1a\u0a19\3\2\2\2\u0a1a\u0a1b")
        buf.write("\3\2\2\2\u0a1b\u0a1c\3\2\2\2\u0a1c\u0a1d\7\u0084\2\2\u0a1d")
        buf.write("\u0a1f\5\u01b4\u00db\2\u0a1e\u0a1a\3\2\2\2\u0a1f\u0a22")
        buf.write("\3\2\2\2\u0a20\u0a1e\3\2\2\2\u0a20\u0a21\3\2\2\2\u0a21")
        buf.write("\u01ab\3\2\2\2\u0a22\u0a20\3\2\2\2\u0a23\u0a24\7G\2\2")
        buf.write("\u0a24\u0a25\5\u0134\u009b\2\u0a25\u0a27\7\u0082\2\2\u0a26")
        buf.write("\u0a28\7\67\2\2\u0a27\u0a26\3\2\2\2\u0a27\u0a28\3\2\2")
        buf.write("\2\u0a28\u0a29\3\2\2\2\u0a29\u0a2f\5\u01ae\u00d8\2\u0a2a")
        buf.write("\u0a2c\7\u0085\2\2\u0a2b\u0a2d\7\67\2\2\u0a2c\u0a2b\3")
        buf.write("\2\2\2\u0a2c\u0a2d\3\2\2\2\u0a2d\u0a2e\3\2\2\2\u0a2e\u0a30")
        buf.write("\5\u01ae\u00d8\2\u0a2f\u0a2a\3\2\2\2\u0a2f\u0a30\3\2\2")
        buf.write("\2\u0a30\u0a31\3\2\2\2\u0a31\u0a37\7\u0083\2\2\u0a32\u0a38")
        buf.write("\5\u013a\u009e\2\u0a33\u0a34\5\u0178\u00bd\2\u0a34\u0a35")
        buf.write("\5L\'\2\u0a35\u0a36\7\u0087\2\2\u0a36\u0a38\3\2\2\2\u0a37")
        buf.write("\u0a32\3\2\2\2\u0a37\u0a33\3\2\2\2\u0a38\u01ad\3\2\2\2")
        buf.write("\u0a39\u0a3a\5\6\4\2\u0a3a\u0a3d\5\u01b4\u00db\2\u0a3b")
        buf.write("\u0a3c\7\u0092\2\2\u0a3c\u0a3e\5\36\20\2\u0a3d\u0a3b\3")
        buf.write("\2\2\2\u0a3d\u0a3e\3\2\2\2\u0a3e\u01af\3\2\2\2\u0a3f\u0a41")
        buf.write("\7\u0082\2\2\u0a40\u0a42\5\32\16\2\u0a41\u0a40\3\2\2\2")
        buf.write("\u0a41\u0a42\3\2\2\2\u0a42\u0a43\3\2\2\2\u0a43\u0a44\7")
        buf.write("\u0083\2\2\u0a44\u01b1\3\2\2\2\u0a45\u0a47\7\u0082\2\2")
        buf.write("\u0a46\u0a48\5\32\16\2\u0a47\u0a46\3\2\2\2\u0a47\u0a48")
        buf.write("\3\2\2\2\u0a48\u0a49\3\2\2\2\u0a49\u0a4b\7\u0083\2\2\u0a4a")
        buf.write("\u0a4c\5Z.\2\u0a4b\u0a4a\3\2\2\2\u0a4b\u0a4c\3\2\2\2\u0a4c")
        buf.write("\u01b3\3\2\2\2\u0a4d\u0a4e\t\24\2\2\u0a4e\u01b5\3\2\2")
        buf.write("\2\u0159\u01b7\u01ba\u01bd\u01c2\u01c6\u01cc\u01cf\u01d4")
        buf.write("\u01d8\u01df\u01e1\u01e9\u01f1\u01f7\u01fb\u0200\u020a")
        buf.write("\u0212\u021c\u0222\u0225\u022d\u0232\u023c\u0249\u0251")
        buf.write("\u0257\u0259\u0260\u0268\u0270\u0278\u0280\u0288\u0292")
        buf.write("\u0294\u029a\u029f\u02a7\u02af\u02b7\u02b9\u02bc\u02c3")
        buf.write("\u02c8\u02cf\u02d3\u02d5\u02f1\u02f5\u02fa\u02fe\u0306")
        buf.write("\u0309\u030e\u0312\u0316\u031c\u032a\u0330\u033c\u0340")
        buf.write("\u0345\u0349\u034f\u0357\u0360\u0372\u0375\u037a\u037d")
        buf.write("\u038c\u0392\u0396\u039c\u03a1\u03a4\u03ac\u03b4\u03bf")
        buf.write("\u03c4\u03c9\u03cb\u03d4\u03dc\u03e3\u03eb\u03ef\u03f8")
        buf.write("\u03fd\u03ff\u0408\u0410\u0414\u0419\u041b\u0420\u0424")
        buf.write("\u042b\u0433\u0435\u0439\u043c\u043f\u0447\u0451\u0462")
        buf.write("\u0469\u046d\u0477\u047c\u0483\u048c\u0491\u0498\u04a4")
        buf.write("\u04af\u04b7\u04bc\u04c5\u04ce\u04d7\u04dd\u04e2\u04e6")
        buf.write("\u04ea\u04ee\u04f2\u04f9\u0501\u050e\u0518\u052e\u0532")
        buf.write("\u0536\u053b\u054f\u0554\u0559\u0560\u0563\u0579\u0585")
        buf.write("\u0589\u0591\u0599\u05a0\u05a4\u05a9\u05ac\u05b1\u05b9")
        buf.write("\u05be\u05c5\u05cb\u05d3\u05db\u05de\u05e5\u05ec\u05f0")
        buf.write("\u05f3\u05f9\u05fd\u0603\u0611\u0617\u061e\u0623\u0626")
        buf.write("\u0629\u0630\u063a\u064b\u0650\u0654\u0657\u065a\u0661")
        buf.write("\u0667\u066f\u0675\u067f\u0687\u068d\u0698\u069c\u069e")
        buf.write("\u06a3\u06a7\u06ae\u06b7\u06be\u06c1\u06c4\u06c8\u06cd")
        buf.write("\u06da\u06e4\u06eb\u06f7\u06fe\u070a\u0710\u0714\u0718")
        buf.write("\u071e\u0724\u0726\u072d\u0731\u0734\u0738\u0742\u0745")
        buf.write("\u074c\u074f\u0754\u0759\u075b\u075e\u0761\u0767\u076a")
        buf.write("\u0776\u077a\u077d\u0787\u078a\u0790\u07ab\u07b8\u07be")
        buf.write("\u07c7\u07cd\u07d0\u07d8\u07dc\u07e2\u07e8\u07ee\u07f9")
        buf.write("\u07fd\u07ff\u0809\u080f\u0812\u081f\u0825\u0828\u082b")
        buf.write("\u0832\u0837\u083b\u083f\u0850\u0853\u0858\u085c\u0860")
        buf.write("\u0869\u086c\u0871\u0875\u087a\u087e\u0880\u088b\u088f")
        buf.write("\u0891\u0896\u089b\u08a2\u08a8\u08ad\u08b3\u08b7\u08bd")
        buf.write("\u08c4\u08ce\u08d1\u08d4\u08d9\u08df\u08e3\u08e5\u08ec")
        buf.write("\u08f3\u08fb\u08ff\u090e\u0912\u091b\u091f\u0923\u0939")
        buf.write("\u0941\u0947\u0950\u0959\u095f\u0966\u096d\u096f\u0976")
        buf.write("\u0979\u097c\u0980\u0983\u0988\u098b\u098e\u0992\u0997")
        buf.write("\u099a\u099d\u09a1\u09a6\u09aa\u09b0\u09b4\u09b8\u09c6")
        buf.write("\u09d3\u09d9\u09ec\u09f7\u09fb\u0a01\u0a05\u0a09\u0a10")
        buf.write("\u0a17\u0a1a\u0a20\u0a27\u0a2c\u0a2f\u0a37\u0a3d\u0a41")
        buf.write("\u0a47\u0a4b")
        return buf.getvalue()


class CSharpParser ( Parser ):

    grammarFileName = "CSharpParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\u00EF\u00BB\u00BF'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'#'", "'abstract'", 
                     "'add'", "'alias'", "'__arglist'", "'as'", "'ascending'", 
                     "'async'", "'await'", "'base'", "'bool'", "'break'", 
                     "'by'", "'byte'", "'case'", "'catch'", "'char'", "'checked'", 
                     "'class'", "'const'", "'continue'", "'decimal'", "'default'", 
                     "'delegate'", "'descending'", "'do'", "'double'", "'dynamic'", 
                     "'else'", "'enum'", "'equals'", "'event'", "'explicit'", 
                     "'extern'", "'false'", "'finally'", "'fixed'", "'float'", 
                     "'for'", "'foreach'", "'from'", "'get'", "'goto'", 
                     "'group'", "'if'", "'implicit'", "'in'", "'int'", "'interface'", 
                     "'internal'", "'into'", "'is'", "'join'", "'let'", 
                     "'lock'", "'long'", "'nameof'", "'namespace'", "'new'", 
                     "'null'", "'object'", "'on'", "'operator'", "'orderby'", 
                     "'out'", "'override'", "'params'", "'partial'", "'private'", 
                     "'protected'", "'public'", "'readonly'", "'ref'", "'remove'", 
                     "'return'", "'sbyte'", "'sealed'", "'select'", "'set'", 
                     "'short'", "'sizeof'", "'stackalloc'", "'static'", 
                     "'string'", "'struct'", "'switch'", "'this'", "'throw'", 
                     "'true'", "'try'", "'typeof'", "'uint'", "'ulong'", 
                     "'unchecked'", "'unmanaged'", "'unsafe'", "'ushort'", 
                     "'using'", "'var'", "'virtual'", "'void'", "'volatile'", 
                     "'when'", "'where'", "'while'", "'yield'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'{'", "'}'", "'['", "']'", 
                     "'('", "')'", "'.'", "','", "':'", "';'", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'&'", "'|'", "'^'", "'!'", "'~'", 
                     "'='", "'<'", "'>'", "'?'", "'::'", "'??'", "'++'", 
                     "'--'", "'&&'", "'||'", "'->'", "'=='", "'!='", "'<='", 
                     "'>='", "'+='", "'-='", "'*='", "'/='", "'%='", "'&='", 
                     "'|='", "'^='", "'<<'", "'<<='", "'??='", "'..'", "'{{'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'define'", "'undef'", "'elif'", 
                     "'endif'", "'line'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'hidden'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'}}'" ]

    symbolicNames = [ "<INVALID>", "BYTE_ORDER_MARK", "SINGLE_LINE_DOC_COMMENT", 
                      "DELIMITED_DOC_COMMENT", "SINGLE_LINE_COMMENT", "DELIMITED_COMMENT", 
                      "WHITESPACES", "SHARP", "ABSTRACT", "ADD", "ALIAS", 
                      "ARGLIST", "AS", "ASCENDING", "ASYNC", "AWAIT", "BASE", 
                      "BOOL", "BREAK", "BY", "BYTE", "CASE", "CATCH", "CHAR", 
                      "CHECKED", "CLASS", "CONST", "CONTINUE", "DECIMAL", 
                      "DEFAULT", "DELEGATE", "DESCENDING", "DO", "DOUBLE", 
                      "DYNAMIC", "ELSE", "ENUM", "EQUALS", "EVENT", "EXPLICIT", 
                      "EXTERN", "FALSE", "FINALLY", "FIXED", "FLOAT", "FOR", 
                      "FOREACH", "FROM", "GET", "GOTO", "GROUP", "IF", "IMPLICIT", 
                      "IN", "INT", "INTERFACE", "INTERNAL", "INTO", "IS", 
                      "JOIN", "LET", "LOCK", "LONG", "NAMEOF", "NAMESPACE", 
                      "NEW", "NULL", "OBJECT", "ON", "OPERATOR", "ORDERBY", 
                      "OUT", "OVERRIDE", "PARAMS", "PARTIAL", "PRIVATE", 
                      "PROTECTED", "PUBLIC", "READONLY", "REF", "REMOVE", 
                      "RETURN", "SBYTE", "SEALED", "SELECT", "SET", "SHORT", 
                      "SIZEOF", "STACKALLOC", "STATIC", "STRING", "STRUCT", 
                      "SWITCH", "THIS", "THROW", "TRUE", "TRY", "TYPEOF", 
                      "UINT", "ULONG", "UNCHECKED", "UNMANAGED", "UNSAFE", 
                      "USHORT", "USING", "VAR", "VIRTUAL", "VOID", "VOLATILE", 
                      "WHEN", "WHERE", "WHILE", "YIELD", "IDENTIFIER", "LITERAL_ACCESS", 
                      "INTEGER_LITERAL", "HEX_INTEGER_LITERAL", "BIN_INTEGER_LITERAL", 
                      "REAL_LITERAL", "CHARACTER_LITERAL", "REGULAR_STRING", 
                      "VERBATIUM_STRING", "INTERPOLATED_REGULAR_STRING_START", 
                      "INTERPOLATED_VERBATIUM_STRING_START", "OPEN_BRACE", 
                      "CLOSE_BRACE", "OPEN_BRACKET", "CLOSE_BRACKET", "OPEN_PARENS", 
                      "CLOSE_PARENS", "DOT", "COMMA", "COLON", "SEMICOLON", 
                      "PLUS", "MINUS", "STAR", "DIV", "PERCENT", "AMP", 
                      "BITWISE_OR", "CARET", "BANG", "TILDE", "ASSIGNMENT", 
                      "LT", "GT", "INTERR", "DOUBLE_COLON", "OP_COALESCING", 
                      "OP_INC", "OP_DEC", "OP_AND", "OP_OR", "OP_PTR", "OP_EQ", 
                      "OP_NE", "OP_LE", "OP_GE", "OP_ADD_ASSIGNMENT", "OP_SUB_ASSIGNMENT", 
                      "OP_MULT_ASSIGNMENT", "OP_DIV_ASSIGNMENT", "OP_MOD_ASSIGNMENT", 
                      "OP_AND_ASSIGNMENT", "OP_OR_ASSIGNMENT", "OP_XOR_ASSIGNMENT", 
                      "OP_LEFT_SHIFT", "OP_LEFT_SHIFT_ASSIGNMENT", "OP_COALESCING_ASSIGNMENT", 
                      "OP_RANGE", "DOUBLE_CURLY_INSIDE", "OPEN_BRACE_INSIDE", 
                      "REGULAR_CHAR_INSIDE", "VERBATIUM_DOUBLE_QUOTE_INSIDE", 
                      "DOUBLE_QUOTE_INSIDE", "REGULAR_STRING_INSIDE", "VERBATIUM_INSIDE_STRING", 
                      "CLOSE_BRACE_INSIDE", "FORMAT_STRING", "DIRECTIVE_WHITESPACES", 
                      "DIGITS", "DEFINE", "UNDEF", "ELIF", "ENDIF", "LINE", 
                      "ERROR", "WARNING", "REGION", "ENDREGION", "PRAGMA", 
                      "NULLABLE", "DIRECTIVE_HIDDEN", "CONDITIONAL_SYMBOL", 
                      "DIRECTIVE_NEW_LINE", "TEXT", "DOUBLE_CURLY_CLOSE_INSIDE" ]

    RULE_compilation_unit = 0
    RULE_namespace_or_type_name = 1
    RULE_type_ = 2
    RULE_base_type = 3
    RULE_tuple_type = 4
    RULE_tuple_element = 5
    RULE_simple_type = 6
    RULE_numeric_type = 7
    RULE_integral_type = 8
    RULE_floating_point_type = 9
    RULE_class_type = 10
    RULE_type_argument_list = 11
    RULE_argument_list = 12
    RULE_argument = 13
    RULE_expression = 14
    RULE_non_assignment_expression = 15
    RULE_assignment = 16
    RULE_assignment_operator = 17
    RULE_conditional_expression = 18
    RULE_null_coalescing_expression = 19
    RULE_conditional_or_expression = 20
    RULE_conditional_and_expression = 21
    RULE_inclusive_or_expression = 22
    RULE_exclusive_or_expression = 23
    RULE_and_expression = 24
    RULE_equality_expression = 25
    RULE_relational_expression = 26
    RULE_shift_expression = 27
    RULE_additive_expression = 28
    RULE_multiplicative_expression = 29
    RULE_switch_expression = 30
    RULE_switch_expression_arms = 31
    RULE_switch_expression_arm = 32
    RULE_range_expression = 33
    RULE_unary_expression = 34
    RULE_primary_expression = 35
    RULE_primary_expression_start = 36
    RULE_throwable_expression = 37
    RULE_throw_expression = 38
    RULE_member_access = 39
    RULE_bracket_expression = 40
    RULE_indexer_argument = 41
    RULE_predefined_type = 42
    RULE_expression_list = 43
    RULE_object_or_collection_initializer = 44
    RULE_object_initializer = 45
    RULE_member_initializer_list = 46
    RULE_member_initializer = 47
    RULE_initializer_value = 48
    RULE_collection_initializer = 49
    RULE_element_initializer = 50
    RULE_anonymous_object_initializer = 51
    RULE_member_declarator_list = 52
    RULE_member_declarator = 53
    RULE_unbound_type_name = 54
    RULE_generic_dimension_specifier = 55
    RULE_isType = 56
    RULE_isTypePatternArms = 57
    RULE_isTypePatternArm = 58
    RULE_lambda_expression = 59
    RULE_anonymous_function_signature = 60
    RULE_explicit_anonymous_function_parameter_list = 61
    RULE_explicit_anonymous_function_parameter = 62
    RULE_implicit_anonymous_function_parameter_list = 63
    RULE_anonymous_function_body = 64
    RULE_query_expression = 65
    RULE_from_clause = 66
    RULE_query_body = 67
    RULE_query_body_clause = 68
    RULE_let_clause = 69
    RULE_where_clause = 70
    RULE_combined_join_clause = 71
    RULE_orderby_clause = 72
    RULE_ordering = 73
    RULE_select_or_group_clause = 74
    RULE_query_continuation = 75
    RULE_statement = 76
    RULE_declarationStatement = 77
    RULE_local_function_declaration = 78
    RULE_local_function_header = 79
    RULE_local_function_modifiers = 80
    RULE_local_function_body = 81
    RULE_labeled_Statement = 82
    RULE_embedded_statement = 83
    RULE_simple_embedded_statement = 84
    RULE_block = 85
    RULE_local_variable_declaration = 86
    RULE_local_variable_type = 87
    RULE_local_variable_declarator = 88
    RULE_local_variable_initializer = 89
    RULE_local_constant_declaration = 90
    RULE_if_body = 91
    RULE_switch_section = 92
    RULE_switch_label = 93
    RULE_case_guard = 94
    RULE_statement_list = 95
    RULE_for_initializer = 96
    RULE_for_iterator = 97
    RULE_catch_clauses = 98
    RULE_specific_catch_clause = 99
    RULE_general_catch_clause = 100
    RULE_exception_filter = 101
    RULE_finally_clause = 102
    RULE_resource_acquisition = 103
    RULE_namespace_declaration = 104
    RULE_qualified_identifier = 105
    RULE_namespace_body = 106
    RULE_extern_alias_directives = 107
    RULE_extern_alias_directive = 108
    RULE_using_directives = 109
    RULE_using_directive = 110
    RULE_namespace_member_declarations = 111
    RULE_namespace_member_declaration = 112
    RULE_type_declaration = 113
    RULE_qualified_alias_member = 114
    RULE_type_parameter_list = 115
    RULE_type_parameter = 116
    RULE_class_base = 117
    RULE_interface_type_list = 118
    RULE_type_parameter_constraints_clauses = 119
    RULE_type_parameter_constraints_clause = 120
    RULE_type_parameter_constraints = 121
    RULE_primary_constraint = 122
    RULE_secondary_constraints = 123
    RULE_constructor_constraint = 124
    RULE_class_body = 125
    RULE_class_member_declarations = 126
    RULE_class_member_declaration = 127
    RULE_all_member_modifiers = 128
    RULE_all_member_modifier = 129
    RULE_common_member_declaration = 130
    RULE_typed_member_declaration = 131
    RULE_constant_declarators = 132
    RULE_constant_declarator = 133
    RULE_variable_declarators = 134
    RULE_variable_declarator = 135
    RULE_variable_initializer = 136
    RULE_return_type = 137
    RULE_member_name = 138
    RULE_method_body = 139
    RULE_formal_parameter_list = 140
    RULE_fixed_parameters = 141
    RULE_fixed_parameter = 142
    RULE_parameter_modifier = 143
    RULE_parameter_array = 144
    RULE_accessor_declarations = 145
    RULE_get_accessor_declaration = 146
    RULE_set_accessor_declaration = 147
    RULE_accessor_modifier = 148
    RULE_accessor_body = 149
    RULE_event_accessor_declarations = 150
    RULE_add_accessor_declaration = 151
    RULE_remove_accessor_declaration = 152
    RULE_overloadable_operator = 153
    RULE_conversion_operator_declarator = 154
    RULE_constructor_initializer = 155
    RULE_body = 156
    RULE_struct_interfaces = 157
    RULE_struct_body = 158
    RULE_struct_member_declaration = 159
    RULE_array_type = 160
    RULE_rank_specifier = 161
    RULE_array_initializer = 162
    RULE_variant_type_parameter_list = 163
    RULE_variant_type_parameter = 164
    RULE_variance_annotation = 165
    RULE_interface_base = 166
    RULE_interface_body = 167
    RULE_interface_member_declaration = 168
    RULE_interface_accessors = 169
    RULE_enum_base = 170
    RULE_enum_body = 171
    RULE_enum_member_declaration = 172
    RULE_global_attribute_section = 173
    RULE_global_attribute_target = 174
    RULE_attributes = 175
    RULE_attribute_section = 176
    RULE_attribute_target = 177
    RULE_attribute_list = 178
    RULE_attribute = 179
    RULE_attribute_argument = 180
    RULE_pointer_type = 181
    RULE_fixed_pointer_declarators = 182
    RULE_fixed_pointer_declarator = 183
    RULE_fixed_pointer_initializer = 184
    RULE_fixed_size_buffer_declarator = 185
    RULE_stackalloc_initializer = 186
    RULE_right_arrow = 187
    RULE_right_shift = 188
    RULE_right_shift_assignment = 189
    RULE_literal = 190
    RULE_boolean_literal = 191
    RULE_string_literal = 192
    RULE_interpolated_regular_string = 193
    RULE_interpolated_verbatium_string = 194
    RULE_interpolated_regular_string_part = 195
    RULE_interpolated_verbatium_string_part = 196
    RULE_interpolated_string_expression = 197
    RULE_keyword = 198
    RULE_class_definition = 199
    RULE_struct_definition = 200
    RULE_interface_definition = 201
    RULE_enum_definition = 202
    RULE_delegate_definition = 203
    RULE_event_declaration = 204
    RULE_field_declaration = 205
    RULE_property_declaration = 206
    RULE_constant_declaration = 207
    RULE_indexer_declaration = 208
    RULE_destructor_definition = 209
    RULE_constructor_declaration = 210
    RULE_method_declaration = 211
    RULE_method_member_name = 212
    RULE_operator_declaration = 213
    RULE_arg_declaration = 214
    RULE_method_invocation = 215
    RULE_object_creation_expression = 216
    RULE_identifier = 217

    ruleNames =  [ "compilation_unit", "namespace_or_type_name", "type_", 
                   "base_type", "tuple_type", "tuple_element", "simple_type", 
                   "numeric_type", "integral_type", "floating_point_type", 
                   "class_type", "type_argument_list", "argument_list", 
                   "argument", "expression", "non_assignment_expression", 
                   "assignment", "assignment_operator", "conditional_expression", 
                   "null_coalescing_expression", "conditional_or_expression", 
                   "conditional_and_expression", "inclusive_or_expression", 
                   "exclusive_or_expression", "and_expression", "equality_expression", 
                   "relational_expression", "shift_expression", "additive_expression", 
                   "multiplicative_expression", "switch_expression", "switch_expression_arms", 
                   "switch_expression_arm", "range_expression", "unary_expression", 
                   "primary_expression", "primary_expression_start", "throwable_expression", 
                   "throw_expression", "member_access", "bracket_expression", 
                   "indexer_argument", "predefined_type", "expression_list", 
                   "object_or_collection_initializer", "object_initializer", 
                   "member_initializer_list", "member_initializer", "initializer_value", 
                   "collection_initializer", "element_initializer", "anonymous_object_initializer", 
                   "member_declarator_list", "member_declarator", "unbound_type_name", 
                   "generic_dimension_specifier", "isType", "isTypePatternArms", 
                   "isTypePatternArm", "lambda_expression", "anonymous_function_signature", 
                   "explicit_anonymous_function_parameter_list", "explicit_anonymous_function_parameter", 
                   "implicit_anonymous_function_parameter_list", "anonymous_function_body", 
                   "query_expression", "from_clause", "query_body", "query_body_clause", 
                   "let_clause", "where_clause", "combined_join_clause", 
                   "orderby_clause", "ordering", "select_or_group_clause", 
                   "query_continuation", "statement", "declarationStatement", 
                   "local_function_declaration", "local_function_header", 
                   "local_function_modifiers", "local_function_body", "labeled_Statement", 
                   "embedded_statement", "simple_embedded_statement", "block", 
                   "local_variable_declaration", "local_variable_type", 
                   "local_variable_declarator", "local_variable_initializer", 
                   "local_constant_declaration", "if_body", "switch_section", 
                   "switch_label", "case_guard", "statement_list", "for_initializer", 
                   "for_iterator", "catch_clauses", "specific_catch_clause", 
                   "general_catch_clause", "exception_filter", "finally_clause", 
                   "resource_acquisition", "namespace_declaration", "qualified_identifier", 
                   "namespace_body", "extern_alias_directives", "extern_alias_directive", 
                   "using_directives", "using_directive", "namespace_member_declarations", 
                   "namespace_member_declaration", "type_declaration", "qualified_alias_member", 
                   "type_parameter_list", "type_parameter", "class_base", 
                   "interface_type_list", "type_parameter_constraints_clauses", 
                   "type_parameter_constraints_clause", "type_parameter_constraints", 
                   "primary_constraint", "secondary_constraints", "constructor_constraint", 
                   "class_body", "class_member_declarations", "class_member_declaration", 
                   "all_member_modifiers", "all_member_modifier", "common_member_declaration", 
                   "typed_member_declaration", "constant_declarators", "constant_declarator", 
                   "variable_declarators", "variable_declarator", "variable_initializer", 
                   "return_type", "member_name", "method_body", "formal_parameter_list", 
                   "fixed_parameters", "fixed_parameter", "parameter_modifier", 
                   "parameter_array", "accessor_declarations", "get_accessor_declaration", 
                   "set_accessor_declaration", "accessor_modifier", "accessor_body", 
                   "event_accessor_declarations", "add_accessor_declaration", 
                   "remove_accessor_declaration", "overloadable_operator", 
                   "conversion_operator_declarator", "constructor_initializer", 
                   "body", "struct_interfaces", "struct_body", "struct_member_declaration", 
                   "array_type", "rank_specifier", "array_initializer", 
                   "variant_type_parameter_list", "variant_type_parameter", 
                   "variance_annotation", "interface_base", "interface_body", 
                   "interface_member_declaration", "interface_accessors", 
                   "enum_base", "enum_body", "enum_member_declaration", 
                   "global_attribute_section", "global_attribute_target", 
                   "attributes", "attribute_section", "attribute_target", 
                   "attribute_list", "attribute", "attribute_argument", 
                   "pointer_type", "fixed_pointer_declarators", "fixed_pointer_declarator", 
                   "fixed_pointer_initializer", "fixed_size_buffer_declarator", 
                   "stackalloc_initializer", "right_arrow", "right_shift", 
                   "right_shift_assignment", "literal", "boolean_literal", 
                   "string_literal", "interpolated_regular_string", "interpolated_verbatium_string", 
                   "interpolated_regular_string_part", "interpolated_verbatium_string_part", 
                   "interpolated_string_expression", "keyword", "class_definition", 
                   "struct_definition", "interface_definition", "enum_definition", 
                   "delegate_definition", "event_declaration", "field_declaration", 
                   "property_declaration", "constant_declaration", "indexer_declaration", 
                   "destructor_definition", "constructor_declaration", "method_declaration", 
                   "method_member_name", "operator_declaration", "arg_declaration", 
                   "method_invocation", "object_creation_expression", "identifier" ]

    EOF = Token.EOF
    BYTE_ORDER_MARK=1
    SINGLE_LINE_DOC_COMMENT=2
    DELIMITED_DOC_COMMENT=3
    SINGLE_LINE_COMMENT=4
    DELIMITED_COMMENT=5
    WHITESPACES=6
    SHARP=7
    ABSTRACT=8
    ADD=9
    ALIAS=10
    ARGLIST=11
    AS=12
    ASCENDING=13
    ASYNC=14
    AWAIT=15
    BASE=16
    BOOL=17
    BREAK=18
    BY=19
    BYTE=20
    CASE=21
    CATCH=22
    CHAR=23
    CHECKED=24
    CLASS=25
    CONST=26
    CONTINUE=27
    DECIMAL=28
    DEFAULT=29
    DELEGATE=30
    DESCENDING=31
    DO=32
    DOUBLE=33
    DYNAMIC=34
    ELSE=35
    ENUM=36
    EQUALS=37
    EVENT=38
    EXPLICIT=39
    EXTERN=40
    FALSE=41
    FINALLY=42
    FIXED=43
    FLOAT=44
    FOR=45
    FOREACH=46
    FROM=47
    GET=48
    GOTO=49
    GROUP=50
    IF=51
    IMPLICIT=52
    IN=53
    INT=54
    INTERFACE=55
    INTERNAL=56
    INTO=57
    IS=58
    JOIN=59
    LET=60
    LOCK=61
    LONG=62
    NAMEOF=63
    NAMESPACE=64
    NEW=65
    NULL=66
    OBJECT=67
    ON=68
    OPERATOR=69
    ORDERBY=70
    OUT=71
    OVERRIDE=72
    PARAMS=73
    PARTIAL=74
    PRIVATE=75
    PROTECTED=76
    PUBLIC=77
    READONLY=78
    REF=79
    REMOVE=80
    RETURN=81
    SBYTE=82
    SEALED=83
    SELECT=84
    SET=85
    SHORT=86
    SIZEOF=87
    STACKALLOC=88
    STATIC=89
    STRING=90
    STRUCT=91
    SWITCH=92
    THIS=93
    THROW=94
    TRUE=95
    TRY=96
    TYPEOF=97
    UINT=98
    ULONG=99
    UNCHECKED=100
    UNMANAGED=101
    UNSAFE=102
    USHORT=103
    USING=104
    VAR=105
    VIRTUAL=106
    VOID=107
    VOLATILE=108
    WHEN=109
    WHERE=110
    WHILE=111
    YIELD=112
    IDENTIFIER=113
    LITERAL_ACCESS=114
    INTEGER_LITERAL=115
    HEX_INTEGER_LITERAL=116
    BIN_INTEGER_LITERAL=117
    REAL_LITERAL=118
    CHARACTER_LITERAL=119
    REGULAR_STRING=120
    VERBATIUM_STRING=121
    INTERPOLATED_REGULAR_STRING_START=122
    INTERPOLATED_VERBATIUM_STRING_START=123
    OPEN_BRACE=124
    CLOSE_BRACE=125
    OPEN_BRACKET=126
    CLOSE_BRACKET=127
    OPEN_PARENS=128
    CLOSE_PARENS=129
    DOT=130
    COMMA=131
    COLON=132
    SEMICOLON=133
    PLUS=134
    MINUS=135
    STAR=136
    DIV=137
    PERCENT=138
    AMP=139
    BITWISE_OR=140
    CARET=141
    BANG=142
    TILDE=143
    ASSIGNMENT=144
    LT=145
    GT=146
    INTERR=147
    DOUBLE_COLON=148
    OP_COALESCING=149
    OP_INC=150
    OP_DEC=151
    OP_AND=152
    OP_OR=153
    OP_PTR=154
    OP_EQ=155
    OP_NE=156
    OP_LE=157
    OP_GE=158
    OP_ADD_ASSIGNMENT=159
    OP_SUB_ASSIGNMENT=160
    OP_MULT_ASSIGNMENT=161
    OP_DIV_ASSIGNMENT=162
    OP_MOD_ASSIGNMENT=163
    OP_AND_ASSIGNMENT=164
    OP_OR_ASSIGNMENT=165
    OP_XOR_ASSIGNMENT=166
    OP_LEFT_SHIFT=167
    OP_LEFT_SHIFT_ASSIGNMENT=168
    OP_COALESCING_ASSIGNMENT=169
    OP_RANGE=170
    DOUBLE_CURLY_INSIDE=171
    OPEN_BRACE_INSIDE=172
    REGULAR_CHAR_INSIDE=173
    VERBATIUM_DOUBLE_QUOTE_INSIDE=174
    DOUBLE_QUOTE_INSIDE=175
    REGULAR_STRING_INSIDE=176
    VERBATIUM_INSIDE_STRING=177
    CLOSE_BRACE_INSIDE=178
    FORMAT_STRING=179
    DIRECTIVE_WHITESPACES=180
    DIGITS=181
    DEFINE=182
    UNDEF=183
    ELIF=184
    ENDIF=185
    LINE=186
    ERROR=187
    WARNING=188
    REGION=189
    ENDREGION=190
    PRAGMA=191
    NULLABLE=192
    DIRECTIVE_HIDDEN=193
    CONDITIONAL_SYMBOL=194
    DIRECTIVE_NEW_LINE=195
    TEXT=196
    DOUBLE_CURLY_CLOSE_INSIDE=197

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Compilation_unitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CSharpParser.EOF, 0)

        def BYTE_ORDER_MARK(self):
            return self.getToken(CSharpParser.BYTE_ORDER_MARK, 0)

        def extern_alias_directives(self):
            return self.getTypedRuleContext(CSharpParser.Extern_alias_directivesContext,0)


        def using_directives(self):
            return self.getTypedRuleContext(CSharpParser.Using_directivesContext,0)


        def global_attribute_section(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Global_attribute_sectionContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Global_attribute_sectionContext,i)


        def namespace_member_declarations(self):
            return self.getTypedRuleContext(CSharpParser.Namespace_member_declarationsContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_compilation_unit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompilation_unit" ):
                listener.enterCompilation_unit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompilation_unit" ):
                listener.exitCompilation_unit(self)




    def compilation_unit(self):

        localctx = CSharpParser.Compilation_unitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_compilation_unit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.BYTE_ORDER_MARK:
                self.state = 436
                self.match(CSharpParser.BYTE_ORDER_MARK)


            self.state = 440
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 439
                self.extern_alias_directives()


            self.state = 443
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.USING:
                self.state = 442
                self.using_directives()


            self.state = 448
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 445
                    self.global_attribute_section() 
                self.state = 450
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 452
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ABSTRACT) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.CLASS) | (1 << CSharpParser.DELEGATE) | (1 << CSharpParser.ENUM) | (1 << CSharpParser.EXTERN) | (1 << CSharpParser.INTERFACE) | (1 << CSharpParser.INTERNAL))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CSharpParser.NAMESPACE - 64)) | (1 << (CSharpParser.NEW - 64)) | (1 << (CSharpParser.OVERRIDE - 64)) | (1 << (CSharpParser.PARTIAL - 64)) | (1 << (CSharpParser.PRIVATE - 64)) | (1 << (CSharpParser.PROTECTED - 64)) | (1 << (CSharpParser.PUBLIC - 64)) | (1 << (CSharpParser.READONLY - 64)) | (1 << (CSharpParser.REF - 64)) | (1 << (CSharpParser.SEALED - 64)) | (1 << (CSharpParser.STATIC - 64)) | (1 << (CSharpParser.STRUCT - 64)) | (1 << (CSharpParser.UNSAFE - 64)) | (1 << (CSharpParser.VIRTUAL - 64)) | (1 << (CSharpParser.VOLATILE - 64)) | (1 << (CSharpParser.OPEN_BRACKET - 64)))) != 0):
                self.state = 451
                self.namespace_member_declarations()


            self.state = 454
            self.match(CSharpParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Namespace_or_type_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(CSharpParser.IdentifierContext,i)


        def qualified_alias_member(self):
            return self.getTypedRuleContext(CSharpParser.Qualified_alias_memberContext,0)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.DOT)
            else:
                return self.getToken(CSharpParser.DOT, i)

        def type_argument_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Type_argument_listContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Type_argument_listContext,i)


        def getRuleIndex(self):
            return CSharpParser.RULE_namespace_or_type_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamespace_or_type_name" ):
                listener.enterNamespace_or_type_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamespace_or_type_name" ):
                listener.exitNamespace_or_type_name(self)




    def namespace_or_type_name(self):

        localctx = CSharpParser.Namespace_or_type_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_namespace_or_type_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 461
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 456
                self.identifier()
                self.state = 458
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 457
                    self.type_argument_list()


                pass

            elif la_ == 2:
                self.state = 460
                self.qualified_alias_member()
                pass


            self.state = 470
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 463
                    self.match(CSharpParser.DOT)
                    self.state = 464
                    self.identifier()
                    self.state = 466
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        self.state = 465
                        self.type_argument_list()

             
                self.state = 472
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def base_type(self):
            return self.getTypedRuleContext(CSharpParser.Base_typeContext,0)


        def INTERR(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.INTERR)
            else:
                return self.getToken(CSharpParser.INTERR, i)

        def rank_specifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Rank_specifierContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Rank_specifierContext,i)


        def STAR(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.STAR)
            else:
                return self.getToken(CSharpParser.STAR, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_type_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_" ):
                listener.enterType_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_" ):
                listener.exitType_(self)




    def type_(self):

        localctx = CSharpParser.Type_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_type_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 473
            self.base_type()
            self.state = 479
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 477
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [CSharpParser.INTERR]:
                        self.state = 474
                        self.match(CSharpParser.INTERR)
                        pass
                    elif token in [CSharpParser.OPEN_BRACKET]:
                        self.state = 475
                        self.rank_specifier()
                        pass
                    elif token in [CSharpParser.STAR]:
                        self.state = 476
                        self.match(CSharpParser.STAR)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 481
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Base_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_type(self):
            return self.getTypedRuleContext(CSharpParser.Simple_typeContext,0)


        def class_type(self):
            return self.getTypedRuleContext(CSharpParser.Class_typeContext,0)


        def VOID(self):
            return self.getToken(CSharpParser.VOID, 0)

        def STAR(self):
            return self.getToken(CSharpParser.STAR, 0)

        def tuple_type(self):
            return self.getTypedRuleContext(CSharpParser.Tuple_typeContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_base_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBase_type" ):
                listener.enterBase_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBase_type" ):
                listener.exitBase_type(self)




    def base_type(self):

        localctx = CSharpParser.Base_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_base_type)
        try:
            self.state = 487
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.BOOL, CSharpParser.BYTE, CSharpParser.CHAR, CSharpParser.DECIMAL, CSharpParser.DOUBLE, CSharpParser.FLOAT, CSharpParser.INT, CSharpParser.LONG, CSharpParser.SBYTE, CSharpParser.SHORT, CSharpParser.UINT, CSharpParser.ULONG, CSharpParser.USHORT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 482
                self.simple_type()
                pass
            elif token in [CSharpParser.ADD, CSharpParser.ALIAS, CSharpParser.ARGLIST, CSharpParser.ASCENDING, CSharpParser.ASYNC, CSharpParser.AWAIT, CSharpParser.BY, CSharpParser.DESCENDING, CSharpParser.DYNAMIC, CSharpParser.EQUALS, CSharpParser.FROM, CSharpParser.GET, CSharpParser.GROUP, CSharpParser.INTO, CSharpParser.JOIN, CSharpParser.LET, CSharpParser.NAMEOF, CSharpParser.OBJECT, CSharpParser.ON, CSharpParser.ORDERBY, CSharpParser.PARTIAL, CSharpParser.REMOVE, CSharpParser.SELECT, CSharpParser.SET, CSharpParser.STRING, CSharpParser.UNMANAGED, CSharpParser.VAR, CSharpParser.WHEN, CSharpParser.WHERE, CSharpParser.YIELD, CSharpParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 483
                self.class_type()
                pass
            elif token in [CSharpParser.VOID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 484
                self.match(CSharpParser.VOID)
                self.state = 485
                self.match(CSharpParser.STAR)
                pass
            elif token in [CSharpParser.OPEN_PARENS]:
                self.enterOuterAlt(localctx, 4)
                self.state = 486
                self.tuple_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tuple_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)

        def tuple_element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Tuple_elementContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Tuple_elementContext,i)


        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_tuple_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTuple_type" ):
                listener.enterTuple_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTuple_type" ):
                listener.exitTuple_type(self)




    def tuple_type(self):

        localctx = CSharpParser.Tuple_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_tuple_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 489
            self.match(CSharpParser.OPEN_PARENS)
            self.state = 490
            self.tuple_element()
            self.state = 493 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 491
                self.match(CSharpParser.COMMA)
                self.state = 492
                self.tuple_element()
                self.state = 495 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CSharpParser.COMMA):
                    break

            self.state = 497
            self.match(CSharpParser.CLOSE_PARENS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tuple_elementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(CSharpParser.Type_Context,0)


        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_tuple_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTuple_element" ):
                listener.enterTuple_element(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTuple_element" ):
                listener.exitTuple_element(self)




    def tuple_element(self):

        localctx = CSharpParser.Tuple_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_tuple_element)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 499
            self.type_()
            self.state = 501
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BY) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.NAMEOF))) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & ((1 << (CSharpParser.ON - 68)) | (1 << (CSharpParser.ORDERBY - 68)) | (1 << (CSharpParser.PARTIAL - 68)) | (1 << (CSharpParser.REMOVE - 68)) | (1 << (CSharpParser.SELECT - 68)) | (1 << (CSharpParser.SET - 68)) | (1 << (CSharpParser.UNMANAGED - 68)) | (1 << (CSharpParser.VAR - 68)) | (1 << (CSharpParser.WHEN - 68)) | (1 << (CSharpParser.WHERE - 68)) | (1 << (CSharpParser.YIELD - 68)) | (1 << (CSharpParser.IDENTIFIER - 68)))) != 0):
                self.state = 500
                self.identifier()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numeric_type(self):
            return self.getTypedRuleContext(CSharpParser.Numeric_typeContext,0)


        def BOOL(self):
            return self.getToken(CSharpParser.BOOL, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_simple_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimple_type" ):
                listener.enterSimple_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimple_type" ):
                listener.exitSimple_type(self)




    def simple_type(self):

        localctx = CSharpParser.Simple_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_simple_type)
        try:
            self.state = 505
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.BYTE, CSharpParser.CHAR, CSharpParser.DECIMAL, CSharpParser.DOUBLE, CSharpParser.FLOAT, CSharpParser.INT, CSharpParser.LONG, CSharpParser.SBYTE, CSharpParser.SHORT, CSharpParser.UINT, CSharpParser.ULONG, CSharpParser.USHORT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 503
                self.numeric_type()
                pass
            elif token in [CSharpParser.BOOL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 504
                self.match(CSharpParser.BOOL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Numeric_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def integral_type(self):
            return self.getTypedRuleContext(CSharpParser.Integral_typeContext,0)


        def floating_point_type(self):
            return self.getTypedRuleContext(CSharpParser.Floating_point_typeContext,0)


        def DECIMAL(self):
            return self.getToken(CSharpParser.DECIMAL, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_numeric_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumeric_type" ):
                listener.enterNumeric_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumeric_type" ):
                listener.exitNumeric_type(self)




    def numeric_type(self):

        localctx = CSharpParser.Numeric_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_numeric_type)
        try:
            self.state = 510
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.BYTE, CSharpParser.CHAR, CSharpParser.INT, CSharpParser.LONG, CSharpParser.SBYTE, CSharpParser.SHORT, CSharpParser.UINT, CSharpParser.ULONG, CSharpParser.USHORT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 507
                self.integral_type()
                pass
            elif token in [CSharpParser.DOUBLE, CSharpParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 508
                self.floating_point_type()
                pass
            elif token in [CSharpParser.DECIMAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 509
                self.match(CSharpParser.DECIMAL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Integral_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SBYTE(self):
            return self.getToken(CSharpParser.SBYTE, 0)

        def BYTE(self):
            return self.getToken(CSharpParser.BYTE, 0)

        def SHORT(self):
            return self.getToken(CSharpParser.SHORT, 0)

        def USHORT(self):
            return self.getToken(CSharpParser.USHORT, 0)

        def INT(self):
            return self.getToken(CSharpParser.INT, 0)

        def UINT(self):
            return self.getToken(CSharpParser.UINT, 0)

        def LONG(self):
            return self.getToken(CSharpParser.LONG, 0)

        def ULONG(self):
            return self.getToken(CSharpParser.ULONG, 0)

        def CHAR(self):
            return self.getToken(CSharpParser.CHAR, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_integral_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntegral_type" ):
                listener.enterIntegral_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntegral_type" ):
                listener.exitIntegral_type(self)




    def integral_type(self):

        localctx = CSharpParser.Integral_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_integral_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 512
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.INT) | (1 << CSharpParser.LONG))) != 0) or ((((_la - 82)) & ~0x3f) == 0 and ((1 << (_la - 82)) & ((1 << (CSharpParser.SBYTE - 82)) | (1 << (CSharpParser.SHORT - 82)) | (1 << (CSharpParser.UINT - 82)) | (1 << (CSharpParser.ULONG - 82)) | (1 << (CSharpParser.USHORT - 82)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Floating_point_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(CSharpParser.FLOAT, 0)

        def DOUBLE(self):
            return self.getToken(CSharpParser.DOUBLE, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_floating_point_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloating_point_type" ):
                listener.enterFloating_point_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloating_point_type" ):
                listener.exitFloating_point_type(self)




    def floating_point_type(self):

        localctx = CSharpParser.Floating_point_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_floating_point_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 514
            _la = self._input.LA(1)
            if not(_la==CSharpParser.DOUBLE or _la==CSharpParser.FLOAT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def namespace_or_type_name(self):
            return self.getTypedRuleContext(CSharpParser.Namespace_or_type_nameContext,0)


        def OBJECT(self):
            return self.getToken(CSharpParser.OBJECT, 0)

        def DYNAMIC(self):
            return self.getToken(CSharpParser.DYNAMIC, 0)

        def STRING(self):
            return self.getToken(CSharpParser.STRING, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_class_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_type" ):
                listener.enterClass_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_type" ):
                listener.exitClass_type(self)




    def class_type(self):

        localctx = CSharpParser.Class_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_class_type)
        try:
            self.state = 520
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 516
                self.namespace_or_type_name()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 517
                self.match(CSharpParser.OBJECT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 518
                self.match(CSharpParser.DYNAMIC)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 519
                self.match(CSharpParser.STRING)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_argument_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(CSharpParser.LT, 0)

        def type_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Type_Context)
            else:
                return self.getTypedRuleContext(CSharpParser.Type_Context,i)


        def GT(self):
            return self.getToken(CSharpParser.GT, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_type_argument_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_argument_list" ):
                listener.enterType_argument_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_argument_list" ):
                listener.exitType_argument_list(self)




    def type_argument_list(self):

        localctx = CSharpParser.Type_argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_type_argument_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 522
            self.match(CSharpParser.LT)
            self.state = 523
            self.type_()
            self.state = 528
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.COMMA:
                self.state = 524
                self.match(CSharpParser.COMMA)
                self.state = 525
                self.type_()
                self.state = 530
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 531
            self.match(CSharpParser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Argument_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(CSharpParser.ArgumentContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_argument_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument_list" ):
                listener.enterArgument_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument_list" ):
                listener.exitArgument_list(self)




    def argument_list(self):

        localctx = CSharpParser.Argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_argument_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 533
            self.argument()
            self.state = 538
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.COMMA:
                self.state = 534
                self.match(CSharpParser.COMMA)
                self.state = 535
                self.argument()
                self.state = 540
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.refout = None # Token

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def COLON(self):
            return self.getToken(CSharpParser.COLON, 0)

        def REF(self):
            return self.getToken(CSharpParser.REF, 0)

        def OUT(self):
            return self.getToken(CSharpParser.OUT, 0)

        def IN(self):
            return self.getToken(CSharpParser.IN, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument" ):
                listener.enterArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument" ):
                listener.exitArgument(self)




    def argument(self):

        localctx = CSharpParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_argument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 544
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 541
                self.identifier()
                self.state = 542
                self.match(CSharpParser.COLON)


            self.state = 547
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 546
                localctx.refout = self._input.LT(1)
                _la = self._input.LA(1)
                if not(((((_la - 53)) & ~0x3f) == 0 and ((1 << (_la - 53)) & ((1 << (CSharpParser.IN - 53)) | (1 << (CSharpParser.OUT - 53)) | (1 << (CSharpParser.REF - 53)))) != 0)):
                    localctx.refout = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 549
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(CSharpParser.AssignmentContext,0)


        def non_assignment_expression(self):
            return self.getTypedRuleContext(CSharpParser.Non_assignment_expressionContext,0)


        def REF(self):
            return self.getToken(CSharpParser.REF, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = CSharpParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_expression)
        try:
            self.state = 555
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 551
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 552
                self.non_assignment_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 553
                self.match(CSharpParser.REF)
                self.state = 554
                self.non_assignment_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Non_assignment_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lambda_expression(self):
            return self.getTypedRuleContext(CSharpParser.Lambda_expressionContext,0)


        def query_expression(self):
            return self.getTypedRuleContext(CSharpParser.Query_expressionContext,0)


        def conditional_expression(self):
            return self.getTypedRuleContext(CSharpParser.Conditional_expressionContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_non_assignment_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNon_assignment_expression" ):
                listener.enterNon_assignment_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNon_assignment_expression" ):
                listener.exitNon_assignment_expression(self)




    def non_assignment_expression(self):

        localctx = CSharpParser.Non_assignment_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_non_assignment_expression)
        try:
            self.state = 560
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 557
                self.lambda_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 558
                self.query_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 559
                self.conditional_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary_expression(self):
            return self.getTypedRuleContext(CSharpParser.Unary_expressionContext,0)


        def assignment_operator(self):
            return self.getTypedRuleContext(CSharpParser.Assignment_operatorContext,0)


        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def OP_COALESCING_ASSIGNMENT(self):
            return self.getToken(CSharpParser.OP_COALESCING_ASSIGNMENT, 0)

        def throwable_expression(self):
            return self.getTypedRuleContext(CSharpParser.Throwable_expressionContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = CSharpParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_assignment)
        try:
            self.state = 570
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 562
                self.unary_expression()
                self.state = 563
                self.assignment_operator()
                self.state = 564
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 566
                self.unary_expression()
                self.state = 567
                self.match(CSharpParser.OP_COALESCING_ASSIGNMENT)
                self.state = 568
                self.throwable_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_operatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGNMENT(self):
            return self.getToken(CSharpParser.ASSIGNMENT, 0)

        def OP_ADD_ASSIGNMENT(self):
            return self.getToken(CSharpParser.OP_ADD_ASSIGNMENT, 0)

        def OP_SUB_ASSIGNMENT(self):
            return self.getToken(CSharpParser.OP_SUB_ASSIGNMENT, 0)

        def OP_MULT_ASSIGNMENT(self):
            return self.getToken(CSharpParser.OP_MULT_ASSIGNMENT, 0)

        def OP_DIV_ASSIGNMENT(self):
            return self.getToken(CSharpParser.OP_DIV_ASSIGNMENT, 0)

        def OP_MOD_ASSIGNMENT(self):
            return self.getToken(CSharpParser.OP_MOD_ASSIGNMENT, 0)

        def OP_AND_ASSIGNMENT(self):
            return self.getToken(CSharpParser.OP_AND_ASSIGNMENT, 0)

        def OP_OR_ASSIGNMENT(self):
            return self.getToken(CSharpParser.OP_OR_ASSIGNMENT, 0)

        def OP_XOR_ASSIGNMENT(self):
            return self.getToken(CSharpParser.OP_XOR_ASSIGNMENT, 0)

        def OP_LEFT_SHIFT_ASSIGNMENT(self):
            return self.getToken(CSharpParser.OP_LEFT_SHIFT_ASSIGNMENT, 0)

        def right_shift_assignment(self):
            return self.getTypedRuleContext(CSharpParser.Right_shift_assignmentContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_assignment_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment_operator" ):
                listener.enterAssignment_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment_operator" ):
                listener.exitAssignment_operator(self)




    def assignment_operator(self):

        localctx = CSharpParser.Assignment_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_assignment_operator)
        try:
            self.state = 583
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.ASSIGNMENT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 572
                self.match(CSharpParser.ASSIGNMENT)
                pass
            elif token in [CSharpParser.OP_ADD_ASSIGNMENT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 573
                self.match(CSharpParser.OP_ADD_ASSIGNMENT)
                pass
            elif token in [CSharpParser.OP_SUB_ASSIGNMENT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 574
                self.match(CSharpParser.OP_SUB_ASSIGNMENT)
                pass
            elif token in [CSharpParser.OP_MULT_ASSIGNMENT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 575
                self.match(CSharpParser.OP_MULT_ASSIGNMENT)
                pass
            elif token in [CSharpParser.OP_DIV_ASSIGNMENT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 576
                self.match(CSharpParser.OP_DIV_ASSIGNMENT)
                pass
            elif token in [CSharpParser.OP_MOD_ASSIGNMENT]:
                self.enterOuterAlt(localctx, 6)
                self.state = 577
                self.match(CSharpParser.OP_MOD_ASSIGNMENT)
                pass
            elif token in [CSharpParser.OP_AND_ASSIGNMENT]:
                self.enterOuterAlt(localctx, 7)
                self.state = 578
                self.match(CSharpParser.OP_AND_ASSIGNMENT)
                pass
            elif token in [CSharpParser.OP_OR_ASSIGNMENT]:
                self.enterOuterAlt(localctx, 8)
                self.state = 579
                self.match(CSharpParser.OP_OR_ASSIGNMENT)
                pass
            elif token in [CSharpParser.OP_XOR_ASSIGNMENT]:
                self.enterOuterAlt(localctx, 9)
                self.state = 580
                self.match(CSharpParser.OP_XOR_ASSIGNMENT)
                pass
            elif token in [CSharpParser.OP_LEFT_SHIFT_ASSIGNMENT]:
                self.enterOuterAlt(localctx, 10)
                self.state = 581
                self.match(CSharpParser.OP_LEFT_SHIFT_ASSIGNMENT)
                pass
            elif token in [CSharpParser.GT]:
                self.enterOuterAlt(localctx, 11)
                self.state = 582
                self.right_shift_assignment()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Conditional_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def null_coalescing_expression(self):
            return self.getTypedRuleContext(CSharpParser.Null_coalescing_expressionContext,0)


        def INTERR(self):
            return self.getToken(CSharpParser.INTERR, 0)

        def throwable_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Throwable_expressionContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Throwable_expressionContext,i)


        def COLON(self):
            return self.getToken(CSharpParser.COLON, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_conditional_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional_expression" ):
                listener.enterConditional_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional_expression" ):
                listener.exitConditional_expression(self)




    def conditional_expression(self):

        localctx = CSharpParser.Conditional_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_conditional_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 585
            self.null_coalescing_expression()
            self.state = 591
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 586
                self.match(CSharpParser.INTERR)
                self.state = 587
                self.throwable_expression()
                self.state = 588
                self.match(CSharpParser.COLON)
                self.state = 589
                self.throwable_expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Null_coalescing_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditional_or_expression(self):
            return self.getTypedRuleContext(CSharpParser.Conditional_or_expressionContext,0)


        def OP_COALESCING(self):
            return self.getToken(CSharpParser.OP_COALESCING, 0)

        def null_coalescing_expression(self):
            return self.getTypedRuleContext(CSharpParser.Null_coalescing_expressionContext,0)


        def throw_expression(self):
            return self.getTypedRuleContext(CSharpParser.Throw_expressionContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_null_coalescing_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNull_coalescing_expression" ):
                listener.enterNull_coalescing_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNull_coalescing_expression" ):
                listener.exitNull_coalescing_expression(self)




    def null_coalescing_expression(self):

        localctx = CSharpParser.Null_coalescing_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_null_coalescing_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 593
            self.conditional_or_expression()
            self.state = 599
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.OP_COALESCING:
                self.state = 594
                self.match(CSharpParser.OP_COALESCING)
                self.state = 597
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSharpParser.ADD, CSharpParser.ALIAS, CSharpParser.ARGLIST, CSharpParser.ASCENDING, CSharpParser.ASYNC, CSharpParser.AWAIT, CSharpParser.BASE, CSharpParser.BOOL, CSharpParser.BY, CSharpParser.BYTE, CSharpParser.CHAR, CSharpParser.CHECKED, CSharpParser.DECIMAL, CSharpParser.DEFAULT, CSharpParser.DELEGATE, CSharpParser.DESCENDING, CSharpParser.DOUBLE, CSharpParser.DYNAMIC, CSharpParser.EQUALS, CSharpParser.FALSE, CSharpParser.FLOAT, CSharpParser.FROM, CSharpParser.GET, CSharpParser.GROUP, CSharpParser.INT, CSharpParser.INTO, CSharpParser.JOIN, CSharpParser.LET, CSharpParser.LONG, CSharpParser.NAMEOF, CSharpParser.NEW, CSharpParser.NULL, CSharpParser.OBJECT, CSharpParser.ON, CSharpParser.ORDERBY, CSharpParser.PARTIAL, CSharpParser.REMOVE, CSharpParser.SBYTE, CSharpParser.SELECT, CSharpParser.SET, CSharpParser.SHORT, CSharpParser.SIZEOF, CSharpParser.STRING, CSharpParser.THIS, CSharpParser.TRUE, CSharpParser.TYPEOF, CSharpParser.UINT, CSharpParser.ULONG, CSharpParser.UNCHECKED, CSharpParser.UNMANAGED, CSharpParser.USHORT, CSharpParser.VAR, CSharpParser.WHEN, CSharpParser.WHERE, CSharpParser.YIELD, CSharpParser.IDENTIFIER, CSharpParser.LITERAL_ACCESS, CSharpParser.INTEGER_LITERAL, CSharpParser.HEX_INTEGER_LITERAL, CSharpParser.BIN_INTEGER_LITERAL, CSharpParser.REAL_LITERAL, CSharpParser.CHARACTER_LITERAL, CSharpParser.REGULAR_STRING, CSharpParser.VERBATIUM_STRING, CSharpParser.INTERPOLATED_REGULAR_STRING_START, CSharpParser.INTERPOLATED_VERBATIUM_STRING_START, CSharpParser.OPEN_PARENS, CSharpParser.PLUS, CSharpParser.MINUS, CSharpParser.STAR, CSharpParser.AMP, CSharpParser.CARET, CSharpParser.BANG, CSharpParser.TILDE, CSharpParser.OP_INC, CSharpParser.OP_DEC, CSharpParser.OP_RANGE]:
                    self.state = 595
                    self.null_coalescing_expression()
                    pass
                elif token in [CSharpParser.THROW]:
                    self.state = 596
                    self.throw_expression()
                    pass
                else:
                    raise NoViableAltException(self)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Conditional_or_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditional_and_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Conditional_and_expressionContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Conditional_and_expressionContext,i)


        def OP_OR(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.OP_OR)
            else:
                return self.getToken(CSharpParser.OP_OR, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_conditional_or_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional_or_expression" ):
                listener.enterConditional_or_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional_or_expression" ):
                listener.exitConditional_or_expression(self)




    def conditional_or_expression(self):

        localctx = CSharpParser.Conditional_or_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_conditional_or_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 601
            self.conditional_and_expression()
            self.state = 606
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.OP_OR:
                self.state = 602
                self.match(CSharpParser.OP_OR)
                self.state = 603
                self.conditional_and_expression()
                self.state = 608
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Conditional_and_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def inclusive_or_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Inclusive_or_expressionContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Inclusive_or_expressionContext,i)


        def OP_AND(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.OP_AND)
            else:
                return self.getToken(CSharpParser.OP_AND, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_conditional_and_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional_and_expression" ):
                listener.enterConditional_and_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional_and_expression" ):
                listener.exitConditional_and_expression(self)




    def conditional_and_expression(self):

        localctx = CSharpParser.Conditional_and_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_conditional_and_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 609
            self.inclusive_or_expression()
            self.state = 614
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.OP_AND:
                self.state = 610
                self.match(CSharpParser.OP_AND)
                self.state = 611
                self.inclusive_or_expression()
                self.state = 616
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Inclusive_or_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exclusive_or_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Exclusive_or_expressionContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Exclusive_or_expressionContext,i)


        def BITWISE_OR(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.BITWISE_OR)
            else:
                return self.getToken(CSharpParser.BITWISE_OR, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_inclusive_or_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInclusive_or_expression" ):
                listener.enterInclusive_or_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInclusive_or_expression" ):
                listener.exitInclusive_or_expression(self)




    def inclusive_or_expression(self):

        localctx = CSharpParser.Inclusive_or_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_inclusive_or_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 617
            self.exclusive_or_expression()
            self.state = 622
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.BITWISE_OR:
                self.state = 618
                self.match(CSharpParser.BITWISE_OR)
                self.state = 619
                self.exclusive_or_expression()
                self.state = 624
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exclusive_or_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def and_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.And_expressionContext)
            else:
                return self.getTypedRuleContext(CSharpParser.And_expressionContext,i)


        def CARET(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.CARET)
            else:
                return self.getToken(CSharpParser.CARET, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_exclusive_or_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExclusive_or_expression" ):
                listener.enterExclusive_or_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExclusive_or_expression" ):
                listener.exitExclusive_or_expression(self)




    def exclusive_or_expression(self):

        localctx = CSharpParser.Exclusive_or_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_exclusive_or_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 625
            self.and_expression()
            self.state = 630
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 626
                    self.match(CSharpParser.CARET)
                    self.state = 627
                    self.and_expression() 
                self.state = 632
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class And_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equality_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Equality_expressionContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Equality_expressionContext,i)


        def AMP(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.AMP)
            else:
                return self.getToken(CSharpParser.AMP, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_and_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnd_expression" ):
                listener.enterAnd_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnd_expression" ):
                listener.exitAnd_expression(self)




    def and_expression(self):

        localctx = CSharpParser.And_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_and_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 633
            self.equality_expression()
            self.state = 638
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 634
                    self.match(CSharpParser.AMP)
                    self.state = 635
                    self.equality_expression() 
                self.state = 640
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Equality_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relational_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Relational_expressionContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Relational_expressionContext,i)


        def OP_EQ(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.OP_EQ)
            else:
                return self.getToken(CSharpParser.OP_EQ, i)

        def OP_NE(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.OP_NE)
            else:
                return self.getToken(CSharpParser.OP_NE, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_equality_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEquality_expression" ):
                listener.enterEquality_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEquality_expression" ):
                listener.exitEquality_expression(self)




    def equality_expression(self):

        localctx = CSharpParser.Equality_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_equality_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 641
            self.relational_expression()
            self.state = 646
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.OP_EQ or _la==CSharpParser.OP_NE:
                self.state = 642
                _la = self._input.LA(1)
                if not(_la==CSharpParser.OP_EQ or _la==CSharpParser.OP_NE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 643
                self.relational_expression()
                self.state = 648
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relational_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def shift_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Shift_expressionContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Shift_expressionContext,i)


        def IS(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.IS)
            else:
                return self.getToken(CSharpParser.IS, i)

        def isType(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.IsTypeContext)
            else:
                return self.getTypedRuleContext(CSharpParser.IsTypeContext,i)


        def AS(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.AS)
            else:
                return self.getToken(CSharpParser.AS, i)

        def type_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Type_Context)
            else:
                return self.getTypedRuleContext(CSharpParser.Type_Context,i)


        def LT(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.LT)
            else:
                return self.getToken(CSharpParser.LT, i)

        def GT(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.GT)
            else:
                return self.getToken(CSharpParser.GT, i)

        def OP_LE(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.OP_LE)
            else:
                return self.getToken(CSharpParser.OP_LE, i)

        def OP_GE(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.OP_GE)
            else:
                return self.getToken(CSharpParser.OP_GE, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_relational_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelational_expression" ):
                listener.enterRelational_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelational_expression" ):
                listener.exitRelational_expression(self)




    def relational_expression(self):

        localctx = CSharpParser.Relational_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_relational_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 649
            self.shift_expression()
            self.state = 658
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.AS or _la==CSharpParser.IS or ((((_la - 145)) & ~0x3f) == 0 and ((1 << (_la - 145)) & ((1 << (CSharpParser.LT - 145)) | (1 << (CSharpParser.GT - 145)) | (1 << (CSharpParser.OP_LE - 145)) | (1 << (CSharpParser.OP_GE - 145)))) != 0):
                self.state = 656
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSharpParser.LT, CSharpParser.GT, CSharpParser.OP_LE, CSharpParser.OP_GE]:
                    self.state = 650
                    _la = self._input.LA(1)
                    if not(((((_la - 145)) & ~0x3f) == 0 and ((1 << (_la - 145)) & ((1 << (CSharpParser.LT - 145)) | (1 << (CSharpParser.GT - 145)) | (1 << (CSharpParser.OP_LE - 145)) | (1 << (CSharpParser.OP_GE - 145)))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 651
                    self.shift_expression()
                    pass
                elif token in [CSharpParser.IS]:
                    self.state = 652
                    self.match(CSharpParser.IS)
                    self.state = 653
                    self.isType()
                    pass
                elif token in [CSharpParser.AS]:
                    self.state = 654
                    self.match(CSharpParser.AS)
                    self.state = 655
                    self.type_()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 660
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Shift_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additive_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Additive_expressionContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Additive_expressionContext,i)


        def OP_LEFT_SHIFT(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.OP_LEFT_SHIFT)
            else:
                return self.getToken(CSharpParser.OP_LEFT_SHIFT, i)

        def right_shift(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Right_shiftContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Right_shiftContext,i)


        def getRuleIndex(self):
            return CSharpParser.RULE_shift_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShift_expression" ):
                listener.enterShift_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShift_expression" ):
                listener.exitShift_expression(self)




    def shift_expression(self):

        localctx = CSharpParser.Shift_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_shift_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 661
            self.additive_expression()
            self.state = 669
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 664
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [CSharpParser.OP_LEFT_SHIFT]:
                        self.state = 662
                        self.match(CSharpParser.OP_LEFT_SHIFT)
                        pass
                    elif token in [CSharpParser.GT]:
                        self.state = 663
                        self.right_shift()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 666
                    self.additive_expression() 
                self.state = 671
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Additive_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicative_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Multiplicative_expressionContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Multiplicative_expressionContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.PLUS)
            else:
                return self.getToken(CSharpParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.MINUS)
            else:
                return self.getToken(CSharpParser.MINUS, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_additive_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditive_expression" ):
                listener.enterAdditive_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditive_expression" ):
                listener.exitAdditive_expression(self)




    def additive_expression(self):

        localctx = CSharpParser.Additive_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_additive_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 672
            self.multiplicative_expression()
            self.state = 677
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 673
                    _la = self._input.LA(1)
                    if not(_la==CSharpParser.PLUS or _la==CSharpParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 674
                    self.multiplicative_expression() 
                self.state = 679
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multiplicative_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def switch_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Switch_expressionContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Switch_expressionContext,i)


        def STAR(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.STAR)
            else:
                return self.getToken(CSharpParser.STAR, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.DIV)
            else:
                return self.getToken(CSharpParser.DIV, i)

        def PERCENT(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.PERCENT)
            else:
                return self.getToken(CSharpParser.PERCENT, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_multiplicative_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicative_expression" ):
                listener.enterMultiplicative_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicative_expression" ):
                listener.exitMultiplicative_expression(self)




    def multiplicative_expression(self):

        localctx = CSharpParser.Multiplicative_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_multiplicative_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 680
            self.switch_expression()
            self.state = 685
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 681
                    _la = self._input.LA(1)
                    if not(((((_la - 136)) & ~0x3f) == 0 and ((1 << (_la - 136)) & ((1 << (CSharpParser.STAR - 136)) | (1 << (CSharpParser.DIV - 136)) | (1 << (CSharpParser.PERCENT - 136)))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 682
                    self.switch_expression() 
                self.state = 687
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Switch_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def range_expression(self):
            return self.getTypedRuleContext(CSharpParser.Range_expressionContext,0)


        def SWITCH(self):
            return self.getToken(CSharpParser.SWITCH, 0)

        def OPEN_BRACE(self):
            return self.getToken(CSharpParser.OPEN_BRACE, 0)

        def CLOSE_BRACE(self):
            return self.getToken(CSharpParser.CLOSE_BRACE, 0)

        def switch_expression_arms(self):
            return self.getTypedRuleContext(CSharpParser.Switch_expression_armsContext,0)


        def COMMA(self):
            return self.getToken(CSharpParser.COMMA, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_switch_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitch_expression" ):
                listener.enterSwitch_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitch_expression" ):
                listener.exitSwitch_expression(self)




    def switch_expression(self):

        localctx = CSharpParser.Switch_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_switch_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 688
            self.range_expression()
            self.state = 698
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.SWITCH:
                self.state = 689
                self.match(CSharpParser.SWITCH)
                self.state = 690
                self.match(CSharpParser.OPEN_BRACE)
                self.state = 695
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BASE) | (1 << CSharpParser.BOOL) | (1 << CSharpParser.BY) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.CHECKED) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DEFAULT) | (1 << CSharpParser.DELEGATE) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FALSE) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.INT) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.LONG) | (1 << CSharpParser.NAMEOF))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (CSharpParser.NEW - 65)) | (1 << (CSharpParser.NULL - 65)) | (1 << (CSharpParser.OBJECT - 65)) | (1 << (CSharpParser.ON - 65)) | (1 << (CSharpParser.ORDERBY - 65)) | (1 << (CSharpParser.PARTIAL - 65)) | (1 << (CSharpParser.REF - 65)) | (1 << (CSharpParser.REMOVE - 65)) | (1 << (CSharpParser.SBYTE - 65)) | (1 << (CSharpParser.SELECT - 65)) | (1 << (CSharpParser.SET - 65)) | (1 << (CSharpParser.SHORT - 65)) | (1 << (CSharpParser.SIZEOF - 65)) | (1 << (CSharpParser.STRING - 65)) | (1 << (CSharpParser.THIS - 65)) | (1 << (CSharpParser.TRUE - 65)) | (1 << (CSharpParser.TYPEOF - 65)) | (1 << (CSharpParser.UINT - 65)) | (1 << (CSharpParser.ULONG - 65)) | (1 << (CSharpParser.UNCHECKED - 65)) | (1 << (CSharpParser.UNMANAGED - 65)) | (1 << (CSharpParser.USHORT - 65)) | (1 << (CSharpParser.VAR - 65)) | (1 << (CSharpParser.WHEN - 65)) | (1 << (CSharpParser.WHERE - 65)) | (1 << (CSharpParser.YIELD - 65)) | (1 << (CSharpParser.IDENTIFIER - 65)) | (1 << (CSharpParser.LITERAL_ACCESS - 65)) | (1 << (CSharpParser.INTEGER_LITERAL - 65)) | (1 << (CSharpParser.HEX_INTEGER_LITERAL - 65)) | (1 << (CSharpParser.BIN_INTEGER_LITERAL - 65)) | (1 << (CSharpParser.REAL_LITERAL - 65)) | (1 << (CSharpParser.CHARACTER_LITERAL - 65)) | (1 << (CSharpParser.REGULAR_STRING - 65)) | (1 << (CSharpParser.VERBATIUM_STRING - 65)) | (1 << (CSharpParser.INTERPOLATED_REGULAR_STRING_START - 65)) | (1 << (CSharpParser.INTERPOLATED_VERBATIUM_STRING_START - 65)) | (1 << (CSharpParser.OPEN_PARENS - 65)))) != 0) or ((((_la - 134)) & ~0x3f) == 0 and ((1 << (_la - 134)) & ((1 << (CSharpParser.PLUS - 134)) | (1 << (CSharpParser.MINUS - 134)) | (1 << (CSharpParser.STAR - 134)) | (1 << (CSharpParser.AMP - 134)) | (1 << (CSharpParser.CARET - 134)) | (1 << (CSharpParser.BANG - 134)) | (1 << (CSharpParser.TILDE - 134)) | (1 << (CSharpParser.OP_INC - 134)) | (1 << (CSharpParser.OP_DEC - 134)) | (1 << (CSharpParser.OP_RANGE - 134)))) != 0):
                    self.state = 691
                    self.switch_expression_arms()
                    self.state = 693
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==CSharpParser.COMMA:
                        self.state = 692
                        self.match(CSharpParser.COMMA)




                self.state = 697
                self.match(CSharpParser.CLOSE_BRACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Switch_expression_armsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def switch_expression_arm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Switch_expression_armContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Switch_expression_armContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_switch_expression_arms

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitch_expression_arms" ):
                listener.enterSwitch_expression_arms(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitch_expression_arms" ):
                listener.exitSwitch_expression_arms(self)




    def switch_expression_arms(self):

        localctx = CSharpParser.Switch_expression_armsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_switch_expression_arms)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 700
            self.switch_expression_arm()
            self.state = 705
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 701
                    self.match(CSharpParser.COMMA)
                    self.state = 702
                    self.switch_expression_arm() 
                self.state = 707
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Switch_expression_armContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def right_arrow(self):
            return self.getTypedRuleContext(CSharpParser.Right_arrowContext,0)


        def throwable_expression(self):
            return self.getTypedRuleContext(CSharpParser.Throwable_expressionContext,0)


        def case_guard(self):
            return self.getTypedRuleContext(CSharpParser.Case_guardContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_switch_expression_arm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitch_expression_arm" ):
                listener.enterSwitch_expression_arm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitch_expression_arm" ):
                listener.exitSwitch_expression_arm(self)




    def switch_expression_arm(self):

        localctx = CSharpParser.Switch_expression_armContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_switch_expression_arm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 708
            self.expression()
            self.state = 710
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.WHEN:
                self.state = 709
                self.case_guard()


            self.state = 712
            self.right_arrow()
            self.state = 713
            self.throwable_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Range_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Unary_expressionContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Unary_expressionContext,i)


        def OP_RANGE(self):
            return self.getToken(CSharpParser.OP_RANGE, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_range_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRange_expression" ):
                listener.enterRange_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRange_expression" ):
                listener.exitRange_expression(self)




    def range_expression(self):

        localctx = CSharpParser.Range_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_range_expression)
        self._la = 0 # Token type
        try:
            self.state = 723
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 715
                self.unary_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 717
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BASE) | (1 << CSharpParser.BOOL) | (1 << CSharpParser.BY) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.CHECKED) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DEFAULT) | (1 << CSharpParser.DELEGATE) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FALSE) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.INT) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.LONG) | (1 << CSharpParser.NAMEOF))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (CSharpParser.NEW - 65)) | (1 << (CSharpParser.NULL - 65)) | (1 << (CSharpParser.OBJECT - 65)) | (1 << (CSharpParser.ON - 65)) | (1 << (CSharpParser.ORDERBY - 65)) | (1 << (CSharpParser.PARTIAL - 65)) | (1 << (CSharpParser.REMOVE - 65)) | (1 << (CSharpParser.SBYTE - 65)) | (1 << (CSharpParser.SELECT - 65)) | (1 << (CSharpParser.SET - 65)) | (1 << (CSharpParser.SHORT - 65)) | (1 << (CSharpParser.SIZEOF - 65)) | (1 << (CSharpParser.STRING - 65)) | (1 << (CSharpParser.THIS - 65)) | (1 << (CSharpParser.TRUE - 65)) | (1 << (CSharpParser.TYPEOF - 65)) | (1 << (CSharpParser.UINT - 65)) | (1 << (CSharpParser.ULONG - 65)) | (1 << (CSharpParser.UNCHECKED - 65)) | (1 << (CSharpParser.UNMANAGED - 65)) | (1 << (CSharpParser.USHORT - 65)) | (1 << (CSharpParser.VAR - 65)) | (1 << (CSharpParser.WHEN - 65)) | (1 << (CSharpParser.WHERE - 65)) | (1 << (CSharpParser.YIELD - 65)) | (1 << (CSharpParser.IDENTIFIER - 65)) | (1 << (CSharpParser.LITERAL_ACCESS - 65)) | (1 << (CSharpParser.INTEGER_LITERAL - 65)) | (1 << (CSharpParser.HEX_INTEGER_LITERAL - 65)) | (1 << (CSharpParser.BIN_INTEGER_LITERAL - 65)) | (1 << (CSharpParser.REAL_LITERAL - 65)) | (1 << (CSharpParser.CHARACTER_LITERAL - 65)) | (1 << (CSharpParser.REGULAR_STRING - 65)) | (1 << (CSharpParser.VERBATIUM_STRING - 65)) | (1 << (CSharpParser.INTERPOLATED_REGULAR_STRING_START - 65)) | (1 << (CSharpParser.INTERPOLATED_VERBATIUM_STRING_START - 65)) | (1 << (CSharpParser.OPEN_PARENS - 65)))) != 0) or ((((_la - 134)) & ~0x3f) == 0 and ((1 << (_la - 134)) & ((1 << (CSharpParser.PLUS - 134)) | (1 << (CSharpParser.MINUS - 134)) | (1 << (CSharpParser.STAR - 134)) | (1 << (CSharpParser.AMP - 134)) | (1 << (CSharpParser.CARET - 134)) | (1 << (CSharpParser.BANG - 134)) | (1 << (CSharpParser.TILDE - 134)) | (1 << (CSharpParser.OP_INC - 134)) | (1 << (CSharpParser.OP_DEC - 134)))) != 0):
                    self.state = 716
                    self.unary_expression()


                self.state = 719
                self.match(CSharpParser.OP_RANGE)
                self.state = 721
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
                if la_ == 1:
                    self.state = 720
                    self.unary_expression()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unary_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary_expression(self):
            return self.getTypedRuleContext(CSharpParser.Primary_expressionContext,0)


        def PLUS(self):
            return self.getToken(CSharpParser.PLUS, 0)

        def unary_expression(self):
            return self.getTypedRuleContext(CSharpParser.Unary_expressionContext,0)


        def MINUS(self):
            return self.getToken(CSharpParser.MINUS, 0)

        def BANG(self):
            return self.getToken(CSharpParser.BANG, 0)

        def TILDE(self):
            return self.getToken(CSharpParser.TILDE, 0)

        def OP_INC(self):
            return self.getToken(CSharpParser.OP_INC, 0)

        def OP_DEC(self):
            return self.getToken(CSharpParser.OP_DEC, 0)

        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)

        def type_(self):
            return self.getTypedRuleContext(CSharpParser.Type_Context,0)


        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)

        def AWAIT(self):
            return self.getToken(CSharpParser.AWAIT, 0)

        def AMP(self):
            return self.getToken(CSharpParser.AMP, 0)

        def STAR(self):
            return self.getToken(CSharpParser.STAR, 0)

        def CARET(self):
            return self.getToken(CSharpParser.CARET, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_unary_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary_expression" ):
                listener.enterUnary_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary_expression" ):
                listener.exitUnary_expression(self)




    def unary_expression(self):

        localctx = CSharpParser.Unary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_unary_expression)
        try:
            self.state = 751
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 725
                self.primary_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 726
                self.match(CSharpParser.PLUS)
                self.state = 727
                self.unary_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 728
                self.match(CSharpParser.MINUS)
                self.state = 729
                self.unary_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 730
                self.match(CSharpParser.BANG)
                self.state = 731
                self.unary_expression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 732
                self.match(CSharpParser.TILDE)
                self.state = 733
                self.unary_expression()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 734
                self.match(CSharpParser.OP_INC)
                self.state = 735
                self.unary_expression()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 736
                self.match(CSharpParser.OP_DEC)
                self.state = 737
                self.unary_expression()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 738
                self.match(CSharpParser.OPEN_PARENS)
                self.state = 739
                self.type_()
                self.state = 740
                self.match(CSharpParser.CLOSE_PARENS)
                self.state = 741
                self.unary_expression()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 743
                self.match(CSharpParser.AWAIT)
                self.state = 744
                self.unary_expression()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 745
                self.match(CSharpParser.AMP)
                self.state = 746
                self.unary_expression()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 747
                self.match(CSharpParser.STAR)
                self.state = 748
                self.unary_expression()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 749
                self.match(CSharpParser.CARET)
                self.state = 750
                self.unary_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primary_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.pe = None # Primary_expression_startContext

        def primary_expression_start(self):
            return self.getTypedRuleContext(CSharpParser.Primary_expression_startContext,0)


        def BANG(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.BANG)
            else:
                return self.getToken(CSharpParser.BANG, i)

        def bracket_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Bracket_expressionContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Bracket_expressionContext,i)


        def member_access(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Member_accessContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Member_accessContext,i)


        def method_invocation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Method_invocationContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Method_invocationContext,i)


        def OP_INC(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.OP_INC)
            else:
                return self.getToken(CSharpParser.OP_INC, i)

        def OP_DEC(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.OP_DEC)
            else:
                return self.getToken(CSharpParser.OP_DEC, i)

        def OP_PTR(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.OP_PTR)
            else:
                return self.getToken(CSharpParser.OP_PTR, i)

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(CSharpParser.IdentifierContext,i)


        def getRuleIndex(self):
            return CSharpParser.RULE_primary_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary_expression" ):
                listener.enterPrimary_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary_expression" ):
                listener.exitPrimary_expression(self)




    def primary_expression(self):

        localctx = CSharpParser.Primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_primary_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 753
            localctx.pe = self.primary_expression_start()
            self.state = 755
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.state = 754
                self.match(CSharpParser.BANG)


            self.state = 760
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,50,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 757
                    self.bracket_expression() 
                self.state = 762
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,50,self._ctx)

            self.state = 764
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.state = 763
                self.match(CSharpParser.BANG)


            self.state = 788
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,56,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 772
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [CSharpParser.DOT, CSharpParser.INTERR]:
                        self.state = 766
                        self.member_access()
                        pass
                    elif token in [CSharpParser.OPEN_PARENS]:
                        self.state = 767
                        self.method_invocation()
                        pass
                    elif token in [CSharpParser.OP_INC]:
                        self.state = 768
                        self.match(CSharpParser.OP_INC)
                        pass
                    elif token in [CSharpParser.OP_DEC]:
                        self.state = 769
                        self.match(CSharpParser.OP_DEC)
                        pass
                    elif token in [CSharpParser.OP_PTR]:
                        self.state = 770
                        self.match(CSharpParser.OP_PTR)
                        self.state = 771
                        self.identifier()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 775
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
                    if la_ == 1:
                        self.state = 774
                        self.match(CSharpParser.BANG)


                    self.state = 780
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,54,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 777
                            self.bracket_expression() 
                        self.state = 782
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,54,self._ctx)

                    self.state = 784
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
                    if la_ == 1:
                        self.state = 783
                        self.match(CSharpParser.BANG)

             
                self.state = 790
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,56,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primary_expression_startContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CSharpParser.RULE_primary_expression_start

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LiteralAccessExpressionContext(Primary_expression_startContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Primary_expression_startContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LITERAL_ACCESS(self):
            return self.getToken(CSharpParser.LITERAL_ACCESS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteralAccessExpression" ):
                listener.enterLiteralAccessExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteralAccessExpression" ):
                listener.exitLiteralAccessExpression(self)


    class DefaultValueExpressionContext(Primary_expression_startContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Primary_expression_startContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DEFAULT(self):
            return self.getToken(CSharpParser.DEFAULT, 0)
        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)
        def type_(self):
            return self.getTypedRuleContext(CSharpParser.Type_Context,0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefaultValueExpression" ):
                listener.enterDefaultValueExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefaultValueExpression" ):
                listener.exitDefaultValueExpression(self)


    class BaseAccessExpressionContext(Primary_expression_startContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Primary_expression_startContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BASE(self):
            return self.getToken(CSharpParser.BASE, 0)
        def DOT(self):
            return self.getToken(CSharpParser.DOT, 0)
        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)

        def OPEN_BRACKET(self):
            return self.getToken(CSharpParser.OPEN_BRACKET, 0)
        def expression_list(self):
            return self.getTypedRuleContext(CSharpParser.Expression_listContext,0)

        def CLOSE_BRACKET(self):
            return self.getToken(CSharpParser.CLOSE_BRACKET, 0)
        def type_argument_list(self):
            return self.getTypedRuleContext(CSharpParser.Type_argument_listContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBaseAccessExpression" ):
                listener.enterBaseAccessExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBaseAccessExpression" ):
                listener.exitBaseAccessExpression(self)


    class SizeofExpressionContext(Primary_expression_startContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Primary_expression_startContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SIZEOF(self):
            return self.getToken(CSharpParser.SIZEOF, 0)
        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)
        def type_(self):
            return self.getTypedRuleContext(CSharpParser.Type_Context,0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSizeofExpression" ):
                listener.enterSizeofExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSizeofExpression" ):
                listener.exitSizeofExpression(self)


    class ParenthesisExpressionsContext(Primary_expression_startContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Primary_expression_startContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)
        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenthesisExpressions" ):
                listener.enterParenthesisExpressions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenthesisExpressions" ):
                listener.exitParenthesisExpressions(self)


    class ThisReferenceExpressionContext(Primary_expression_startContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Primary_expression_startContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def THIS(self):
            return self.getToken(CSharpParser.THIS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThisReferenceExpression" ):
                listener.enterThisReferenceExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThisReferenceExpression" ):
                listener.exitThisReferenceExpression(self)


    class ObjectCreationExpressionContext(Primary_expression_startContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Primary_expression_startContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEW(self):
            return self.getToken(CSharpParser.NEW, 0)
        def type_(self):
            return self.getTypedRuleContext(CSharpParser.Type_Context,0)

        def anonymous_object_initializer(self):
            return self.getTypedRuleContext(CSharpParser.Anonymous_object_initializerContext,0)

        def rank_specifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Rank_specifierContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Rank_specifierContext,i)

        def array_initializer(self):
            return self.getTypedRuleContext(CSharpParser.Array_initializerContext,0)

        def object_creation_expression(self):
            return self.getTypedRuleContext(CSharpParser.Object_creation_expressionContext,0)

        def object_or_collection_initializer(self):
            return self.getTypedRuleContext(CSharpParser.Object_or_collection_initializerContext,0)

        def OPEN_BRACKET(self):
            return self.getToken(CSharpParser.OPEN_BRACKET, 0)
        def expression_list(self):
            return self.getTypedRuleContext(CSharpParser.Expression_listContext,0)

        def CLOSE_BRACKET(self):
            return self.getToken(CSharpParser.CLOSE_BRACKET, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObjectCreationExpression" ):
                listener.enterObjectCreationExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObjectCreationExpression" ):
                listener.exitObjectCreationExpression(self)


    class AnonymousMethodExpressionContext(Primary_expression_startContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Primary_expression_startContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DELEGATE(self):
            return self.getToken(CSharpParser.DELEGATE, 0)
        def block(self):
            return self.getTypedRuleContext(CSharpParser.BlockContext,0)

        def ASYNC(self):
            return self.getToken(CSharpParser.ASYNC, 0)
        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)
        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)
        def explicit_anonymous_function_parameter_list(self):
            return self.getTypedRuleContext(CSharpParser.Explicit_anonymous_function_parameter_listContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnonymousMethodExpression" ):
                listener.enterAnonymousMethodExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnonymousMethodExpression" ):
                listener.exitAnonymousMethodExpression(self)


    class TypeofExpressionContext(Primary_expression_startContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Primary_expression_startContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TYPEOF(self):
            return self.getToken(CSharpParser.TYPEOF, 0)
        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)
        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)
        def unbound_type_name(self):
            return self.getTypedRuleContext(CSharpParser.Unbound_type_nameContext,0)

        def type_(self):
            return self.getTypedRuleContext(CSharpParser.Type_Context,0)

        def VOID(self):
            return self.getToken(CSharpParser.VOID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeofExpression" ):
                listener.enterTypeofExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeofExpression" ):
                listener.exitTypeofExpression(self)


    class TupleExpressionContext(Primary_expression_startContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Primary_expression_startContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)
        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(CSharpParser.ArgumentContext,i)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTupleExpression" ):
                listener.enterTupleExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTupleExpression" ):
                listener.exitTupleExpression(self)


    class UncheckedExpressionContext(Primary_expression_startContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Primary_expression_startContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def UNCHECKED(self):
            return self.getToken(CSharpParser.UNCHECKED, 0)
        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)
        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUncheckedExpression" ):
                listener.enterUncheckedExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUncheckedExpression" ):
                listener.exitUncheckedExpression(self)


    class SimpleNameExpressionContext(Primary_expression_startContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Primary_expression_startContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)

        def type_argument_list(self):
            return self.getTypedRuleContext(CSharpParser.Type_argument_listContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleNameExpression" ):
                listener.enterSimpleNameExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleNameExpression" ):
                listener.exitSimpleNameExpression(self)


    class MemberAccessExpressionContext(Primary_expression_startContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Primary_expression_startContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def predefined_type(self):
            return self.getTypedRuleContext(CSharpParser.Predefined_typeContext,0)

        def qualified_alias_member(self):
            return self.getTypedRuleContext(CSharpParser.Qualified_alias_memberContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemberAccessExpression" ):
                listener.enterMemberAccessExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemberAccessExpression" ):
                listener.exitMemberAccessExpression(self)


    class CheckedExpressionContext(Primary_expression_startContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Primary_expression_startContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CHECKED(self):
            return self.getToken(CSharpParser.CHECKED, 0)
        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)
        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCheckedExpression" ):
                listener.enterCheckedExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCheckedExpression" ):
                listener.exitCheckedExpression(self)


    class LiteralExpressionContext(Primary_expression_startContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Primary_expression_startContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(CSharpParser.LiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteralExpression" ):
                listener.enterLiteralExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteralExpression" ):
                listener.exitLiteralExpression(self)


    class NameofExpressionContext(Primary_expression_startContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Primary_expression_startContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NAMEOF(self):
            return self.getToken(CSharpParser.NAMEOF, 0)
        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)
        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(CSharpParser.IdentifierContext,i)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)
        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.DOT)
            else:
                return self.getToken(CSharpParser.DOT, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNameofExpression" ):
                listener.enterNameofExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNameofExpression" ):
                listener.exitNameofExpression(self)



    def primary_expression_start(self):

        localctx = CSharpParser.Primary_expression_startContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_primary_expression_start)
        self._la = 0 # Token type
        try:
            self.state = 912
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,72,self._ctx)
            if la_ == 1:
                localctx = CSharpParser.LiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 791
                self.literal()
                pass

            elif la_ == 2:
                localctx = CSharpParser.SimpleNameExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 792
                self.identifier()
                self.state = 794
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
                if la_ == 1:
                    self.state = 793
                    self.type_argument_list()


                pass

            elif la_ == 3:
                localctx = CSharpParser.ParenthesisExpressionsContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 796
                self.match(CSharpParser.OPEN_PARENS)
                self.state = 797
                self.expression()
                self.state = 798
                self.match(CSharpParser.CLOSE_PARENS)
                pass

            elif la_ == 4:
                localctx = CSharpParser.MemberAccessExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 800
                self.predefined_type()
                pass

            elif la_ == 5:
                localctx = CSharpParser.MemberAccessExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 801
                self.qualified_alias_member()
                pass

            elif la_ == 6:
                localctx = CSharpParser.LiteralAccessExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 802
                self.match(CSharpParser.LITERAL_ACCESS)
                pass

            elif la_ == 7:
                localctx = CSharpParser.ThisReferenceExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 803
                self.match(CSharpParser.THIS)
                pass

            elif la_ == 8:
                localctx = CSharpParser.BaseAccessExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 804
                self.match(CSharpParser.BASE)
                self.state = 814
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSharpParser.DOT]:
                    self.state = 805
                    self.match(CSharpParser.DOT)
                    self.state = 806
                    self.identifier()
                    self.state = 808
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
                    if la_ == 1:
                        self.state = 807
                        self.type_argument_list()


                    pass
                elif token in [CSharpParser.OPEN_BRACKET]:
                    self.state = 810
                    self.match(CSharpParser.OPEN_BRACKET)
                    self.state = 811
                    self.expression_list()
                    self.state = 812
                    self.match(CSharpParser.CLOSE_BRACKET)
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 9:
                localctx = CSharpParser.ObjectCreationExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 816
                self.match(CSharpParser.NEW)
                self.state = 845
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSharpParser.ADD, CSharpParser.ALIAS, CSharpParser.ARGLIST, CSharpParser.ASCENDING, CSharpParser.ASYNC, CSharpParser.AWAIT, CSharpParser.BOOL, CSharpParser.BY, CSharpParser.BYTE, CSharpParser.CHAR, CSharpParser.DECIMAL, CSharpParser.DESCENDING, CSharpParser.DOUBLE, CSharpParser.DYNAMIC, CSharpParser.EQUALS, CSharpParser.FLOAT, CSharpParser.FROM, CSharpParser.GET, CSharpParser.GROUP, CSharpParser.INT, CSharpParser.INTO, CSharpParser.JOIN, CSharpParser.LET, CSharpParser.LONG, CSharpParser.NAMEOF, CSharpParser.OBJECT, CSharpParser.ON, CSharpParser.ORDERBY, CSharpParser.PARTIAL, CSharpParser.REMOVE, CSharpParser.SBYTE, CSharpParser.SELECT, CSharpParser.SET, CSharpParser.SHORT, CSharpParser.STRING, CSharpParser.UINT, CSharpParser.ULONG, CSharpParser.UNMANAGED, CSharpParser.USHORT, CSharpParser.VAR, CSharpParser.VOID, CSharpParser.WHEN, CSharpParser.WHERE, CSharpParser.YIELD, CSharpParser.IDENTIFIER, CSharpParser.OPEN_PARENS]:
                    self.state = 817
                    self.type_()
                    self.state = 839
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
                    if la_ == 1:
                        self.state = 818
                        self.object_creation_expression()
                        pass

                    elif la_ == 2:
                        self.state = 819
                        self.object_or_collection_initializer()
                        pass

                    elif la_ == 3:
                        self.state = 820
                        self.match(CSharpParser.OPEN_BRACKET)
                        self.state = 821
                        self.expression_list()
                        self.state = 822
                        self.match(CSharpParser.CLOSE_BRACKET)
                        self.state = 826
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,60,self._ctx)
                        while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                            if _alt==1:
                                self.state = 823
                                self.rank_specifier() 
                            self.state = 828
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,60,self._ctx)

                        self.state = 830
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==CSharpParser.OPEN_BRACE:
                            self.state = 829
                            self.array_initializer()


                        pass

                    elif la_ == 4:
                        self.state = 833 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while True:
                            self.state = 832
                            self.rank_specifier()
                            self.state = 835 
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if not (_la==CSharpParser.OPEN_BRACKET):
                                break

                        self.state = 837
                        self.array_initializer()
                        pass


                    pass
                elif token in [CSharpParser.OPEN_BRACE]:
                    self.state = 841
                    self.anonymous_object_initializer()
                    pass
                elif token in [CSharpParser.OPEN_BRACKET]:
                    self.state = 842
                    self.rank_specifier()
                    self.state = 843
                    self.array_initializer()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 10:
                localctx = CSharpParser.TupleExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 847
                self.match(CSharpParser.OPEN_PARENS)
                self.state = 848
                self.argument()
                self.state = 851 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 849
                    self.match(CSharpParser.COMMA)
                    self.state = 850
                    self.argument()
                    self.state = 853 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==CSharpParser.COMMA):
                        break

                self.state = 855
                self.match(CSharpParser.CLOSE_PARENS)
                pass

            elif la_ == 11:
                localctx = CSharpParser.TypeofExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 857
                self.match(CSharpParser.TYPEOF)
                self.state = 858
                self.match(CSharpParser.OPEN_PARENS)
                self.state = 862
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,66,self._ctx)
                if la_ == 1:
                    self.state = 859
                    self.unbound_type_name()
                    pass

                elif la_ == 2:
                    self.state = 860
                    self.type_()
                    pass

                elif la_ == 3:
                    self.state = 861
                    self.match(CSharpParser.VOID)
                    pass


                self.state = 864
                self.match(CSharpParser.CLOSE_PARENS)
                pass

            elif la_ == 12:
                localctx = CSharpParser.CheckedExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 865
                self.match(CSharpParser.CHECKED)
                self.state = 866
                self.match(CSharpParser.OPEN_PARENS)
                self.state = 867
                self.expression()
                self.state = 868
                self.match(CSharpParser.CLOSE_PARENS)
                pass

            elif la_ == 13:
                localctx = CSharpParser.UncheckedExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 870
                self.match(CSharpParser.UNCHECKED)
                self.state = 871
                self.match(CSharpParser.OPEN_PARENS)
                self.state = 872
                self.expression()
                self.state = 873
                self.match(CSharpParser.CLOSE_PARENS)
                pass

            elif la_ == 14:
                localctx = CSharpParser.DefaultValueExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 875
                self.match(CSharpParser.DEFAULT)
                self.state = 880
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,67,self._ctx)
                if la_ == 1:
                    self.state = 876
                    self.match(CSharpParser.OPEN_PARENS)
                    self.state = 877
                    self.type_()
                    self.state = 878
                    self.match(CSharpParser.CLOSE_PARENS)


                pass

            elif la_ == 15:
                localctx = CSharpParser.AnonymousMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 883
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.ASYNC:
                    self.state = 882
                    self.match(CSharpParser.ASYNC)


                self.state = 885
                self.match(CSharpParser.DELEGATE)
                self.state = 891
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.OPEN_PARENS:
                    self.state = 886
                    self.match(CSharpParser.OPEN_PARENS)
                    self.state = 888
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BOOL) | (1 << CSharpParser.BY) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.IN) | (1 << CSharpParser.INT) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.LONG) | (1 << CSharpParser.NAMEOF))) != 0) or ((((_la - 67)) & ~0x3f) == 0 and ((1 << (_la - 67)) & ((1 << (CSharpParser.OBJECT - 67)) | (1 << (CSharpParser.ON - 67)) | (1 << (CSharpParser.ORDERBY - 67)) | (1 << (CSharpParser.OUT - 67)) | (1 << (CSharpParser.PARTIAL - 67)) | (1 << (CSharpParser.REF - 67)) | (1 << (CSharpParser.REMOVE - 67)) | (1 << (CSharpParser.SBYTE - 67)) | (1 << (CSharpParser.SELECT - 67)) | (1 << (CSharpParser.SET - 67)) | (1 << (CSharpParser.SHORT - 67)) | (1 << (CSharpParser.STRING - 67)) | (1 << (CSharpParser.UINT - 67)) | (1 << (CSharpParser.ULONG - 67)) | (1 << (CSharpParser.UNMANAGED - 67)) | (1 << (CSharpParser.USHORT - 67)) | (1 << (CSharpParser.VAR - 67)) | (1 << (CSharpParser.VOID - 67)) | (1 << (CSharpParser.WHEN - 67)) | (1 << (CSharpParser.WHERE - 67)) | (1 << (CSharpParser.YIELD - 67)) | (1 << (CSharpParser.IDENTIFIER - 67)) | (1 << (CSharpParser.OPEN_PARENS - 67)))) != 0):
                        self.state = 887
                        self.explicit_anonymous_function_parameter_list()


                    self.state = 890
                    self.match(CSharpParser.CLOSE_PARENS)


                self.state = 893
                self.block()
                pass

            elif la_ == 16:
                localctx = CSharpParser.SizeofExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 16)
                self.state = 894
                self.match(CSharpParser.SIZEOF)
                self.state = 895
                self.match(CSharpParser.OPEN_PARENS)
                self.state = 896
                self.type_()
                self.state = 897
                self.match(CSharpParser.CLOSE_PARENS)
                pass

            elif la_ == 17:
                localctx = CSharpParser.NameofExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 17)
                self.state = 899
                self.match(CSharpParser.NAMEOF)
                self.state = 900
                self.match(CSharpParser.OPEN_PARENS)
                self.state = 906
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,71,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 901
                        self.identifier()
                        self.state = 902
                        self.match(CSharpParser.DOT) 
                    self.state = 908
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,71,self._ctx)

                self.state = 909
                self.identifier()
                self.state = 910
                self.match(CSharpParser.CLOSE_PARENS)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Throwable_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def throw_expression(self):
            return self.getTypedRuleContext(CSharpParser.Throw_expressionContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_throwable_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThrowable_expression" ):
                listener.enterThrowable_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThrowable_expression" ):
                listener.exitThrowable_expression(self)




    def throwable_expression(self):

        localctx = CSharpParser.Throwable_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_throwable_expression)
        try:
            self.state = 916
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.ADD, CSharpParser.ALIAS, CSharpParser.ARGLIST, CSharpParser.ASCENDING, CSharpParser.ASYNC, CSharpParser.AWAIT, CSharpParser.BASE, CSharpParser.BOOL, CSharpParser.BY, CSharpParser.BYTE, CSharpParser.CHAR, CSharpParser.CHECKED, CSharpParser.DECIMAL, CSharpParser.DEFAULT, CSharpParser.DELEGATE, CSharpParser.DESCENDING, CSharpParser.DOUBLE, CSharpParser.DYNAMIC, CSharpParser.EQUALS, CSharpParser.FALSE, CSharpParser.FLOAT, CSharpParser.FROM, CSharpParser.GET, CSharpParser.GROUP, CSharpParser.INT, CSharpParser.INTO, CSharpParser.JOIN, CSharpParser.LET, CSharpParser.LONG, CSharpParser.NAMEOF, CSharpParser.NEW, CSharpParser.NULL, CSharpParser.OBJECT, CSharpParser.ON, CSharpParser.ORDERBY, CSharpParser.PARTIAL, CSharpParser.REF, CSharpParser.REMOVE, CSharpParser.SBYTE, CSharpParser.SELECT, CSharpParser.SET, CSharpParser.SHORT, CSharpParser.SIZEOF, CSharpParser.STRING, CSharpParser.THIS, CSharpParser.TRUE, CSharpParser.TYPEOF, CSharpParser.UINT, CSharpParser.ULONG, CSharpParser.UNCHECKED, CSharpParser.UNMANAGED, CSharpParser.USHORT, CSharpParser.VAR, CSharpParser.WHEN, CSharpParser.WHERE, CSharpParser.YIELD, CSharpParser.IDENTIFIER, CSharpParser.LITERAL_ACCESS, CSharpParser.INTEGER_LITERAL, CSharpParser.HEX_INTEGER_LITERAL, CSharpParser.BIN_INTEGER_LITERAL, CSharpParser.REAL_LITERAL, CSharpParser.CHARACTER_LITERAL, CSharpParser.REGULAR_STRING, CSharpParser.VERBATIUM_STRING, CSharpParser.INTERPOLATED_REGULAR_STRING_START, CSharpParser.INTERPOLATED_VERBATIUM_STRING_START, CSharpParser.OPEN_PARENS, CSharpParser.PLUS, CSharpParser.MINUS, CSharpParser.STAR, CSharpParser.AMP, CSharpParser.CARET, CSharpParser.BANG, CSharpParser.TILDE, CSharpParser.OP_INC, CSharpParser.OP_DEC, CSharpParser.OP_RANGE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 914
                self.expression()
                pass
            elif token in [CSharpParser.THROW]:
                self.enterOuterAlt(localctx, 2)
                self.state = 915
                self.throw_expression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Throw_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def THROW(self):
            return self.getToken(CSharpParser.THROW, 0)

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_throw_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThrow_expression" ):
                listener.enterThrow_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThrow_expression" ):
                listener.exitThrow_expression(self)




    def throw_expression(self):

        localctx = CSharpParser.Throw_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_throw_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 918
            self.match(CSharpParser.THROW)
            self.state = 919
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Member_accessContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(CSharpParser.DOT, 0)

        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def INTERR(self):
            return self.getToken(CSharpParser.INTERR, 0)

        def type_argument_list(self):
            return self.getTypedRuleContext(CSharpParser.Type_argument_listContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_member_access

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMember_access" ):
                listener.enterMember_access(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMember_access" ):
                listener.exitMember_access(self)




    def member_access(self):

        localctx = CSharpParser.Member_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_member_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 922
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.INTERR:
                self.state = 921
                self.match(CSharpParser.INTERR)


            self.state = 924
            self.match(CSharpParser.DOT)
            self.state = 925
            self.identifier()
            self.state = 927
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,75,self._ctx)
            if la_ == 1:
                self.state = 926
                self.type_argument_list()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bracket_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACKET(self):
            return self.getToken(CSharpParser.OPEN_BRACKET, 0)

        def indexer_argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Indexer_argumentContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Indexer_argumentContext,i)


        def CLOSE_BRACKET(self):
            return self.getToken(CSharpParser.CLOSE_BRACKET, 0)

        def INTERR(self):
            return self.getToken(CSharpParser.INTERR, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_bracket_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBracket_expression" ):
                listener.enterBracket_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBracket_expression" ):
                listener.exitBracket_expression(self)




    def bracket_expression(self):

        localctx = CSharpParser.Bracket_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_bracket_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 930
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.INTERR:
                self.state = 929
                self.match(CSharpParser.INTERR)


            self.state = 932
            self.match(CSharpParser.OPEN_BRACKET)
            self.state = 933
            self.indexer_argument()
            self.state = 938
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.COMMA:
                self.state = 934
                self.match(CSharpParser.COMMA)
                self.state = 935
                self.indexer_argument()
                self.state = 940
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 941
            self.match(CSharpParser.CLOSE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Indexer_argumentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def COLON(self):
            return self.getToken(CSharpParser.COLON, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_indexer_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndexer_argument" ):
                listener.enterIndexer_argument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndexer_argument" ):
                listener.exitIndexer_argument(self)




    def indexer_argument(self):

        localctx = CSharpParser.Indexer_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_indexer_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 946
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,78,self._ctx)
            if la_ == 1:
                self.state = 943
                self.identifier()
                self.state = 944
                self.match(CSharpParser.COLON)


            self.state = 948
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Predefined_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL(self):
            return self.getToken(CSharpParser.BOOL, 0)

        def BYTE(self):
            return self.getToken(CSharpParser.BYTE, 0)

        def CHAR(self):
            return self.getToken(CSharpParser.CHAR, 0)

        def DECIMAL(self):
            return self.getToken(CSharpParser.DECIMAL, 0)

        def DOUBLE(self):
            return self.getToken(CSharpParser.DOUBLE, 0)

        def FLOAT(self):
            return self.getToken(CSharpParser.FLOAT, 0)

        def INT(self):
            return self.getToken(CSharpParser.INT, 0)

        def LONG(self):
            return self.getToken(CSharpParser.LONG, 0)

        def OBJECT(self):
            return self.getToken(CSharpParser.OBJECT, 0)

        def SBYTE(self):
            return self.getToken(CSharpParser.SBYTE, 0)

        def SHORT(self):
            return self.getToken(CSharpParser.SHORT, 0)

        def STRING(self):
            return self.getToken(CSharpParser.STRING, 0)

        def UINT(self):
            return self.getToken(CSharpParser.UINT, 0)

        def ULONG(self):
            return self.getToken(CSharpParser.ULONG, 0)

        def USHORT(self):
            return self.getToken(CSharpParser.USHORT, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_predefined_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredefined_type" ):
                listener.enterPredefined_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredefined_type" ):
                listener.exitPredefined_type(self)




    def predefined_type(self):

        localctx = CSharpParser.Predefined_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_predefined_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 950
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.BOOL) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.INT) | (1 << CSharpParser.LONG))) != 0) or ((((_la - 67)) & ~0x3f) == 0 and ((1 << (_la - 67)) & ((1 << (CSharpParser.OBJECT - 67)) | (1 << (CSharpParser.SBYTE - 67)) | (1 << (CSharpParser.SHORT - 67)) | (1 << (CSharpParser.STRING - 67)) | (1 << (CSharpParser.UINT - 67)) | (1 << (CSharpParser.ULONG - 67)) | (1 << (CSharpParser.USHORT - 67)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CSharpParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_expression_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression_list" ):
                listener.enterExpression_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression_list" ):
                listener.exitExpression_list(self)




    def expression_list(self):

        localctx = CSharpParser.Expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_expression_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 952
            self.expression()
            self.state = 957
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.COMMA:
                self.state = 953
                self.match(CSharpParser.COMMA)
                self.state = 954
                self.expression()
                self.state = 959
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Object_or_collection_initializerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def object_initializer(self):
            return self.getTypedRuleContext(CSharpParser.Object_initializerContext,0)


        def collection_initializer(self):
            return self.getTypedRuleContext(CSharpParser.Collection_initializerContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_object_or_collection_initializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObject_or_collection_initializer" ):
                listener.enterObject_or_collection_initializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObject_or_collection_initializer" ):
                listener.exitObject_or_collection_initializer(self)




    def object_or_collection_initializer(self):

        localctx = CSharpParser.Object_or_collection_initializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_object_or_collection_initializer)
        try:
            self.state = 962
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,80,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 960
                self.object_initializer()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 961
                self.collection_initializer()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Object_initializerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACE(self):
            return self.getToken(CSharpParser.OPEN_BRACE, 0)

        def CLOSE_BRACE(self):
            return self.getToken(CSharpParser.CLOSE_BRACE, 0)

        def member_initializer_list(self):
            return self.getTypedRuleContext(CSharpParser.Member_initializer_listContext,0)


        def COMMA(self):
            return self.getToken(CSharpParser.COMMA, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_object_initializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObject_initializer" ):
                listener.enterObject_initializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObject_initializer" ):
                listener.exitObject_initializer(self)




    def object_initializer(self):

        localctx = CSharpParser.Object_initializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_object_initializer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 964
            self.match(CSharpParser.OPEN_BRACE)
            self.state = 969
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BY) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.NAMEOF))) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & ((1 << (CSharpParser.ON - 68)) | (1 << (CSharpParser.ORDERBY - 68)) | (1 << (CSharpParser.PARTIAL - 68)) | (1 << (CSharpParser.REMOVE - 68)) | (1 << (CSharpParser.SELECT - 68)) | (1 << (CSharpParser.SET - 68)) | (1 << (CSharpParser.UNMANAGED - 68)) | (1 << (CSharpParser.VAR - 68)) | (1 << (CSharpParser.WHEN - 68)) | (1 << (CSharpParser.WHERE - 68)) | (1 << (CSharpParser.YIELD - 68)) | (1 << (CSharpParser.IDENTIFIER - 68)) | (1 << (CSharpParser.OPEN_BRACKET - 68)))) != 0):
                self.state = 965
                self.member_initializer_list()
                self.state = 967
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.COMMA:
                    self.state = 966
                    self.match(CSharpParser.COMMA)




            self.state = 971
            self.match(CSharpParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Member_initializer_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member_initializer(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Member_initializerContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Member_initializerContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_member_initializer_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMember_initializer_list" ):
                listener.enterMember_initializer_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMember_initializer_list" ):
                listener.exitMember_initializer_list(self)




    def member_initializer_list(self):

        localctx = CSharpParser.Member_initializer_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_member_initializer_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 973
            self.member_initializer()
            self.state = 978
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,83,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 974
                    self.match(CSharpParser.COMMA)
                    self.state = 975
                    self.member_initializer() 
                self.state = 980
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,83,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Member_initializerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGNMENT(self):
            return self.getToken(CSharpParser.ASSIGNMENT, 0)

        def initializer_value(self):
            return self.getTypedRuleContext(CSharpParser.Initializer_valueContext,0)


        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def OPEN_BRACKET(self):
            return self.getToken(CSharpParser.OPEN_BRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def CLOSE_BRACKET(self):
            return self.getToken(CSharpParser.CLOSE_BRACKET, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_member_initializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMember_initializer" ):
                listener.enterMember_initializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMember_initializer" ):
                listener.exitMember_initializer(self)




    def member_initializer(self):

        localctx = CSharpParser.Member_initializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_member_initializer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 986
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.ADD, CSharpParser.ALIAS, CSharpParser.ARGLIST, CSharpParser.ASCENDING, CSharpParser.ASYNC, CSharpParser.AWAIT, CSharpParser.BY, CSharpParser.DESCENDING, CSharpParser.DYNAMIC, CSharpParser.EQUALS, CSharpParser.FROM, CSharpParser.GET, CSharpParser.GROUP, CSharpParser.INTO, CSharpParser.JOIN, CSharpParser.LET, CSharpParser.NAMEOF, CSharpParser.ON, CSharpParser.ORDERBY, CSharpParser.PARTIAL, CSharpParser.REMOVE, CSharpParser.SELECT, CSharpParser.SET, CSharpParser.UNMANAGED, CSharpParser.VAR, CSharpParser.WHEN, CSharpParser.WHERE, CSharpParser.YIELD, CSharpParser.IDENTIFIER]:
                self.state = 981
                self.identifier()
                pass
            elif token in [CSharpParser.OPEN_BRACKET]:
                self.state = 982
                self.match(CSharpParser.OPEN_BRACKET)
                self.state = 983
                self.expression()
                self.state = 984
                self.match(CSharpParser.CLOSE_BRACKET)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 988
            self.match(CSharpParser.ASSIGNMENT)
            self.state = 989
            self.initializer_value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Initializer_valueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def object_or_collection_initializer(self):
            return self.getTypedRuleContext(CSharpParser.Object_or_collection_initializerContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_initializer_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitializer_value" ):
                listener.enterInitializer_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitializer_value" ):
                listener.exitInitializer_value(self)




    def initializer_value(self):

        localctx = CSharpParser.Initializer_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_initializer_value)
        try:
            self.state = 993
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.ADD, CSharpParser.ALIAS, CSharpParser.ARGLIST, CSharpParser.ASCENDING, CSharpParser.ASYNC, CSharpParser.AWAIT, CSharpParser.BASE, CSharpParser.BOOL, CSharpParser.BY, CSharpParser.BYTE, CSharpParser.CHAR, CSharpParser.CHECKED, CSharpParser.DECIMAL, CSharpParser.DEFAULT, CSharpParser.DELEGATE, CSharpParser.DESCENDING, CSharpParser.DOUBLE, CSharpParser.DYNAMIC, CSharpParser.EQUALS, CSharpParser.FALSE, CSharpParser.FLOAT, CSharpParser.FROM, CSharpParser.GET, CSharpParser.GROUP, CSharpParser.INT, CSharpParser.INTO, CSharpParser.JOIN, CSharpParser.LET, CSharpParser.LONG, CSharpParser.NAMEOF, CSharpParser.NEW, CSharpParser.NULL, CSharpParser.OBJECT, CSharpParser.ON, CSharpParser.ORDERBY, CSharpParser.PARTIAL, CSharpParser.REF, CSharpParser.REMOVE, CSharpParser.SBYTE, CSharpParser.SELECT, CSharpParser.SET, CSharpParser.SHORT, CSharpParser.SIZEOF, CSharpParser.STRING, CSharpParser.THIS, CSharpParser.TRUE, CSharpParser.TYPEOF, CSharpParser.UINT, CSharpParser.ULONG, CSharpParser.UNCHECKED, CSharpParser.UNMANAGED, CSharpParser.USHORT, CSharpParser.VAR, CSharpParser.WHEN, CSharpParser.WHERE, CSharpParser.YIELD, CSharpParser.IDENTIFIER, CSharpParser.LITERAL_ACCESS, CSharpParser.INTEGER_LITERAL, CSharpParser.HEX_INTEGER_LITERAL, CSharpParser.BIN_INTEGER_LITERAL, CSharpParser.REAL_LITERAL, CSharpParser.CHARACTER_LITERAL, CSharpParser.REGULAR_STRING, CSharpParser.VERBATIUM_STRING, CSharpParser.INTERPOLATED_REGULAR_STRING_START, CSharpParser.INTERPOLATED_VERBATIUM_STRING_START, CSharpParser.OPEN_PARENS, CSharpParser.PLUS, CSharpParser.MINUS, CSharpParser.STAR, CSharpParser.AMP, CSharpParser.CARET, CSharpParser.BANG, CSharpParser.TILDE, CSharpParser.OP_INC, CSharpParser.OP_DEC, CSharpParser.OP_RANGE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 991
                self.expression()
                pass
            elif token in [CSharpParser.OPEN_BRACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 992
                self.object_or_collection_initializer()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Collection_initializerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACE(self):
            return self.getToken(CSharpParser.OPEN_BRACE, 0)

        def element_initializer(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Element_initializerContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Element_initializerContext,i)


        def CLOSE_BRACE(self):
            return self.getToken(CSharpParser.CLOSE_BRACE, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_collection_initializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCollection_initializer" ):
                listener.enterCollection_initializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCollection_initializer" ):
                listener.exitCollection_initializer(self)




    def collection_initializer(self):

        localctx = CSharpParser.Collection_initializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_collection_initializer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 995
            self.match(CSharpParser.OPEN_BRACE)
            self.state = 996
            self.element_initializer()
            self.state = 1001
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,86,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 997
                    self.match(CSharpParser.COMMA)
                    self.state = 998
                    self.element_initializer() 
                self.state = 1003
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,86,self._ctx)

            self.state = 1005
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.COMMA:
                self.state = 1004
                self.match(CSharpParser.COMMA)


            self.state = 1007
            self.match(CSharpParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Element_initializerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def non_assignment_expression(self):
            return self.getTypedRuleContext(CSharpParser.Non_assignment_expressionContext,0)


        def OPEN_BRACE(self):
            return self.getToken(CSharpParser.OPEN_BRACE, 0)

        def expression_list(self):
            return self.getTypedRuleContext(CSharpParser.Expression_listContext,0)


        def CLOSE_BRACE(self):
            return self.getToken(CSharpParser.CLOSE_BRACE, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_element_initializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElement_initializer" ):
                listener.enterElement_initializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElement_initializer" ):
                listener.exitElement_initializer(self)




    def element_initializer(self):

        localctx = CSharpParser.Element_initializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_element_initializer)
        try:
            self.state = 1014
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.ADD, CSharpParser.ALIAS, CSharpParser.ARGLIST, CSharpParser.ASCENDING, CSharpParser.ASYNC, CSharpParser.AWAIT, CSharpParser.BASE, CSharpParser.BOOL, CSharpParser.BY, CSharpParser.BYTE, CSharpParser.CHAR, CSharpParser.CHECKED, CSharpParser.DECIMAL, CSharpParser.DEFAULT, CSharpParser.DELEGATE, CSharpParser.DESCENDING, CSharpParser.DOUBLE, CSharpParser.DYNAMIC, CSharpParser.EQUALS, CSharpParser.FALSE, CSharpParser.FLOAT, CSharpParser.FROM, CSharpParser.GET, CSharpParser.GROUP, CSharpParser.INT, CSharpParser.INTO, CSharpParser.JOIN, CSharpParser.LET, CSharpParser.LONG, CSharpParser.NAMEOF, CSharpParser.NEW, CSharpParser.NULL, CSharpParser.OBJECT, CSharpParser.ON, CSharpParser.ORDERBY, CSharpParser.PARTIAL, CSharpParser.REMOVE, CSharpParser.SBYTE, CSharpParser.SELECT, CSharpParser.SET, CSharpParser.SHORT, CSharpParser.SIZEOF, CSharpParser.STRING, CSharpParser.THIS, CSharpParser.TRUE, CSharpParser.TYPEOF, CSharpParser.UINT, CSharpParser.ULONG, CSharpParser.UNCHECKED, CSharpParser.UNMANAGED, CSharpParser.USHORT, CSharpParser.VAR, CSharpParser.WHEN, CSharpParser.WHERE, CSharpParser.YIELD, CSharpParser.IDENTIFIER, CSharpParser.LITERAL_ACCESS, CSharpParser.INTEGER_LITERAL, CSharpParser.HEX_INTEGER_LITERAL, CSharpParser.BIN_INTEGER_LITERAL, CSharpParser.REAL_LITERAL, CSharpParser.CHARACTER_LITERAL, CSharpParser.REGULAR_STRING, CSharpParser.VERBATIUM_STRING, CSharpParser.INTERPOLATED_REGULAR_STRING_START, CSharpParser.INTERPOLATED_VERBATIUM_STRING_START, CSharpParser.OPEN_PARENS, CSharpParser.PLUS, CSharpParser.MINUS, CSharpParser.STAR, CSharpParser.AMP, CSharpParser.CARET, CSharpParser.BANG, CSharpParser.TILDE, CSharpParser.OP_INC, CSharpParser.OP_DEC, CSharpParser.OP_RANGE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1009
                self.non_assignment_expression()
                pass
            elif token in [CSharpParser.OPEN_BRACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1010
                self.match(CSharpParser.OPEN_BRACE)
                self.state = 1011
                self.expression_list()
                self.state = 1012
                self.match(CSharpParser.CLOSE_BRACE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Anonymous_object_initializerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACE(self):
            return self.getToken(CSharpParser.OPEN_BRACE, 0)

        def CLOSE_BRACE(self):
            return self.getToken(CSharpParser.CLOSE_BRACE, 0)

        def member_declarator_list(self):
            return self.getTypedRuleContext(CSharpParser.Member_declarator_listContext,0)


        def COMMA(self):
            return self.getToken(CSharpParser.COMMA, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_anonymous_object_initializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnonymous_object_initializer" ):
                listener.enterAnonymous_object_initializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnonymous_object_initializer" ):
                listener.exitAnonymous_object_initializer(self)




    def anonymous_object_initializer(self):

        localctx = CSharpParser.Anonymous_object_initializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_anonymous_object_initializer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1016
            self.match(CSharpParser.OPEN_BRACE)
            self.state = 1021
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BASE) | (1 << CSharpParser.BOOL) | (1 << CSharpParser.BY) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.CHECKED) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DEFAULT) | (1 << CSharpParser.DELEGATE) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FALSE) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.INT) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.LONG) | (1 << CSharpParser.NAMEOF))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (CSharpParser.NEW - 65)) | (1 << (CSharpParser.NULL - 65)) | (1 << (CSharpParser.OBJECT - 65)) | (1 << (CSharpParser.ON - 65)) | (1 << (CSharpParser.ORDERBY - 65)) | (1 << (CSharpParser.PARTIAL - 65)) | (1 << (CSharpParser.REMOVE - 65)) | (1 << (CSharpParser.SBYTE - 65)) | (1 << (CSharpParser.SELECT - 65)) | (1 << (CSharpParser.SET - 65)) | (1 << (CSharpParser.SHORT - 65)) | (1 << (CSharpParser.SIZEOF - 65)) | (1 << (CSharpParser.STRING - 65)) | (1 << (CSharpParser.THIS - 65)) | (1 << (CSharpParser.TRUE - 65)) | (1 << (CSharpParser.TYPEOF - 65)) | (1 << (CSharpParser.UINT - 65)) | (1 << (CSharpParser.ULONG - 65)) | (1 << (CSharpParser.UNCHECKED - 65)) | (1 << (CSharpParser.UNMANAGED - 65)) | (1 << (CSharpParser.USHORT - 65)) | (1 << (CSharpParser.VAR - 65)) | (1 << (CSharpParser.WHEN - 65)) | (1 << (CSharpParser.WHERE - 65)) | (1 << (CSharpParser.YIELD - 65)) | (1 << (CSharpParser.IDENTIFIER - 65)) | (1 << (CSharpParser.LITERAL_ACCESS - 65)) | (1 << (CSharpParser.INTEGER_LITERAL - 65)) | (1 << (CSharpParser.HEX_INTEGER_LITERAL - 65)) | (1 << (CSharpParser.BIN_INTEGER_LITERAL - 65)) | (1 << (CSharpParser.REAL_LITERAL - 65)) | (1 << (CSharpParser.CHARACTER_LITERAL - 65)) | (1 << (CSharpParser.REGULAR_STRING - 65)) | (1 << (CSharpParser.VERBATIUM_STRING - 65)) | (1 << (CSharpParser.INTERPOLATED_REGULAR_STRING_START - 65)) | (1 << (CSharpParser.INTERPOLATED_VERBATIUM_STRING_START - 65)) | (1 << (CSharpParser.OPEN_PARENS - 65)))) != 0):
                self.state = 1017
                self.member_declarator_list()
                self.state = 1019
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.COMMA:
                    self.state = 1018
                    self.match(CSharpParser.COMMA)




            self.state = 1023
            self.match(CSharpParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Member_declarator_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member_declarator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Member_declaratorContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Member_declaratorContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_member_declarator_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMember_declarator_list" ):
                listener.enterMember_declarator_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMember_declarator_list" ):
                listener.exitMember_declarator_list(self)




    def member_declarator_list(self):

        localctx = CSharpParser.Member_declarator_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_member_declarator_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1025
            self.member_declarator()
            self.state = 1030
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,91,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1026
                    self.match(CSharpParser.COMMA)
                    self.state = 1027
                    self.member_declarator() 
                self.state = 1032
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,91,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Member_declaratorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary_expression(self):
            return self.getTypedRuleContext(CSharpParser.Primary_expressionContext,0)


        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def ASSIGNMENT(self):
            return self.getToken(CSharpParser.ASSIGNMENT, 0)

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_member_declarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMember_declarator" ):
                listener.enterMember_declarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMember_declarator" ):
                listener.exitMember_declarator(self)




    def member_declarator(self):

        localctx = CSharpParser.Member_declaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_member_declarator)
        try:
            self.state = 1038
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,92,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1033
                self.primary_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1034
                self.identifier()
                self.state = 1035
                self.match(CSharpParser.ASSIGNMENT)
                self.state = 1036
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unbound_type_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(CSharpParser.IdentifierContext,i)


        def DOUBLE_COLON(self):
            return self.getToken(CSharpParser.DOUBLE_COLON, 0)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.DOT)
            else:
                return self.getToken(CSharpParser.DOT, i)

        def generic_dimension_specifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Generic_dimension_specifierContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Generic_dimension_specifierContext,i)


        def getRuleIndex(self):
            return CSharpParser.RULE_unbound_type_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnbound_type_name" ):
                listener.enterUnbound_type_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnbound_type_name" ):
                listener.exitUnbound_type_name(self)




    def unbound_type_name(self):

        localctx = CSharpParser.Unbound_type_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_unbound_type_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1040
            self.identifier()
            self.state = 1049
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.CLOSE_PARENS, CSharpParser.DOT, CSharpParser.LT]:
                self.state = 1042
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.LT:
                    self.state = 1041
                    self.generic_dimension_specifier()


                pass
            elif token in [CSharpParser.DOUBLE_COLON]:
                self.state = 1044
                self.match(CSharpParser.DOUBLE_COLON)
                self.state = 1045
                self.identifier()
                self.state = 1047
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.LT:
                    self.state = 1046
                    self.generic_dimension_specifier()


                pass
            else:
                raise NoViableAltException(self)

            self.state = 1058
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.DOT:
                self.state = 1051
                self.match(CSharpParser.DOT)
                self.state = 1052
                self.identifier()
                self.state = 1054
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.LT:
                    self.state = 1053
                    self.generic_dimension_specifier()


                self.state = 1060
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Generic_dimension_specifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(CSharpParser.LT, 0)

        def GT(self):
            return self.getToken(CSharpParser.GT, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_generic_dimension_specifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGeneric_dimension_specifier" ):
                listener.enterGeneric_dimension_specifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGeneric_dimension_specifier" ):
                listener.exitGeneric_dimension_specifier(self)




    def generic_dimension_specifier(self):

        localctx = CSharpParser.Generic_dimension_specifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_generic_dimension_specifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1061
            self.match(CSharpParser.LT)
            self.state = 1065
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.COMMA:
                self.state = 1062
                self.match(CSharpParser.COMMA)
                self.state = 1067
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1068
            self.match(CSharpParser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IsTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def base_type(self):
            return self.getTypedRuleContext(CSharpParser.Base_typeContext,0)


        def rank_specifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Rank_specifierContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Rank_specifierContext,i)


        def STAR(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.STAR)
            else:
                return self.getToken(CSharpParser.STAR, i)

        def INTERR(self):
            return self.getToken(CSharpParser.INTERR, 0)

        def isTypePatternArms(self):
            return self.getTypedRuleContext(CSharpParser.IsTypePatternArmsContext,0)


        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_isType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIsType" ):
                listener.enterIsType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIsType" ):
                listener.exitIsType(self)




    def isType(self):

        localctx = CSharpParser.IsTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_isType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1070
            self.base_type()
            self.state = 1075
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,100,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1073
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [CSharpParser.OPEN_BRACKET]:
                        self.state = 1071
                        self.rank_specifier()
                        pass
                    elif token in [CSharpParser.STAR]:
                        self.state = 1072
                        self.match(CSharpParser.STAR)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 1077
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,100,self._ctx)

            self.state = 1079
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,101,self._ctx)
            if la_ == 1:
                self.state = 1078
                self.match(CSharpParser.INTERR)


            self.state = 1082
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.OPEN_BRACE:
                self.state = 1081
                self.isTypePatternArms()


            self.state = 1085
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,103,self._ctx)
            if la_ == 1:
                self.state = 1084
                self.identifier()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IsTypePatternArmsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACE(self):
            return self.getToken(CSharpParser.OPEN_BRACE, 0)

        def isTypePatternArm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.IsTypePatternArmContext)
            else:
                return self.getTypedRuleContext(CSharpParser.IsTypePatternArmContext,i)


        def CLOSE_BRACE(self):
            return self.getToken(CSharpParser.CLOSE_BRACE, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_isTypePatternArms

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIsTypePatternArms" ):
                listener.enterIsTypePatternArms(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIsTypePatternArms" ):
                listener.exitIsTypePatternArms(self)




    def isTypePatternArms(self):

        localctx = CSharpParser.IsTypePatternArmsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_isTypePatternArms)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1087
            self.match(CSharpParser.OPEN_BRACE)
            self.state = 1088
            self.isTypePatternArm()
            self.state = 1093
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.COMMA:
                self.state = 1089
                self.match(CSharpParser.COMMA)
                self.state = 1090
                self.isTypePatternArm()
                self.state = 1095
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1096
            self.match(CSharpParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IsTypePatternArmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def COLON(self):
            return self.getToken(CSharpParser.COLON, 0)

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_isTypePatternArm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIsTypePatternArm" ):
                listener.enterIsTypePatternArm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIsTypePatternArm" ):
                listener.exitIsTypePatternArm(self)




    def isTypePatternArm(self):

        localctx = CSharpParser.IsTypePatternArmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_isTypePatternArm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1098
            self.identifier()
            self.state = 1099
            self.match(CSharpParser.COLON)
            self.state = 1100
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lambda_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def anonymous_function_signature(self):
            return self.getTypedRuleContext(CSharpParser.Anonymous_function_signatureContext,0)


        def right_arrow(self):
            return self.getTypedRuleContext(CSharpParser.Right_arrowContext,0)


        def anonymous_function_body(self):
            return self.getTypedRuleContext(CSharpParser.Anonymous_function_bodyContext,0)


        def ASYNC(self):
            return self.getToken(CSharpParser.ASYNC, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_lambda_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLambda_expression" ):
                listener.enterLambda_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLambda_expression" ):
                listener.exitLambda_expression(self)




    def lambda_expression(self):

        localctx = CSharpParser.Lambda_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_lambda_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,105,self._ctx)
            if la_ == 1:
                self.state = 1102
                self.match(CSharpParser.ASYNC)


            self.state = 1105
            self.anonymous_function_signature()
            self.state = 1106
            self.right_arrow()
            self.state = 1107
            self.anonymous_function_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Anonymous_function_signatureContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)

        def explicit_anonymous_function_parameter_list(self):
            return self.getTypedRuleContext(CSharpParser.Explicit_anonymous_function_parameter_listContext,0)


        def implicit_anonymous_function_parameter_list(self):
            return self.getTypedRuleContext(CSharpParser.Implicit_anonymous_function_parameter_listContext,0)


        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_anonymous_function_signature

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnonymous_function_signature" ):
                listener.enterAnonymous_function_signature(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnonymous_function_signature" ):
                listener.exitAnonymous_function_signature(self)




    def anonymous_function_signature(self):

        localctx = CSharpParser.Anonymous_function_signatureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_anonymous_function_signature)
        try:
            self.state = 1120
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,106,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1109
                self.match(CSharpParser.OPEN_PARENS)
                self.state = 1110
                self.match(CSharpParser.CLOSE_PARENS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1111
                self.match(CSharpParser.OPEN_PARENS)
                self.state = 1112
                self.explicit_anonymous_function_parameter_list()
                self.state = 1113
                self.match(CSharpParser.CLOSE_PARENS)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1115
                self.match(CSharpParser.OPEN_PARENS)
                self.state = 1116
                self.implicit_anonymous_function_parameter_list()
                self.state = 1117
                self.match(CSharpParser.CLOSE_PARENS)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1119
                self.identifier()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Explicit_anonymous_function_parameter_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def explicit_anonymous_function_parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Explicit_anonymous_function_parameterContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Explicit_anonymous_function_parameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_explicit_anonymous_function_parameter_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExplicit_anonymous_function_parameter_list" ):
                listener.enterExplicit_anonymous_function_parameter_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExplicit_anonymous_function_parameter_list" ):
                listener.exitExplicit_anonymous_function_parameter_list(self)




    def explicit_anonymous_function_parameter_list(self):

        localctx = CSharpParser.Explicit_anonymous_function_parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_explicit_anonymous_function_parameter_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1122
            self.explicit_anonymous_function_parameter()
            self.state = 1127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.COMMA:
                self.state = 1123
                self.match(CSharpParser.COMMA)
                self.state = 1124
                self.explicit_anonymous_function_parameter()
                self.state = 1129
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Explicit_anonymous_function_parameterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.refout = None # Token

        def type_(self):
            return self.getTypedRuleContext(CSharpParser.Type_Context,0)


        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def REF(self):
            return self.getToken(CSharpParser.REF, 0)

        def OUT(self):
            return self.getToken(CSharpParser.OUT, 0)

        def IN(self):
            return self.getToken(CSharpParser.IN, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_explicit_anonymous_function_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExplicit_anonymous_function_parameter" ):
                listener.enterExplicit_anonymous_function_parameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExplicit_anonymous_function_parameter" ):
                listener.exitExplicit_anonymous_function_parameter(self)




    def explicit_anonymous_function_parameter(self):

        localctx = CSharpParser.Explicit_anonymous_function_parameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_explicit_anonymous_function_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 53)) & ~0x3f) == 0 and ((1 << (_la - 53)) & ((1 << (CSharpParser.IN - 53)) | (1 << (CSharpParser.OUT - 53)) | (1 << (CSharpParser.REF - 53)))) != 0):
                self.state = 1130
                localctx.refout = self._input.LT(1)
                _la = self._input.LA(1)
                if not(((((_la - 53)) & ~0x3f) == 0 and ((1 << (_la - 53)) & ((1 << (CSharpParser.IN - 53)) | (1 << (CSharpParser.OUT - 53)) | (1 << (CSharpParser.REF - 53)))) != 0)):
                    localctx.refout = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 1133
            self.type_()
            self.state = 1134
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Implicit_anonymous_function_parameter_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(CSharpParser.IdentifierContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_implicit_anonymous_function_parameter_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImplicit_anonymous_function_parameter_list" ):
                listener.enterImplicit_anonymous_function_parameter_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImplicit_anonymous_function_parameter_list" ):
                listener.exitImplicit_anonymous_function_parameter_list(self)




    def implicit_anonymous_function_parameter_list(self):

        localctx = CSharpParser.Implicit_anonymous_function_parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_implicit_anonymous_function_parameter_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1136
            self.identifier()
            self.state = 1141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.COMMA:
                self.state = 1137
                self.match(CSharpParser.COMMA)
                self.state = 1138
                self.identifier()
                self.state = 1143
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Anonymous_function_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def throwable_expression(self):
            return self.getTypedRuleContext(CSharpParser.Throwable_expressionContext,0)


        def block(self):
            return self.getTypedRuleContext(CSharpParser.BlockContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_anonymous_function_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnonymous_function_body" ):
                listener.enterAnonymous_function_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnonymous_function_body" ):
                listener.exitAnonymous_function_body(self)




    def anonymous_function_body(self):

        localctx = CSharpParser.Anonymous_function_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_anonymous_function_body)
        try:
            self.state = 1146
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.ADD, CSharpParser.ALIAS, CSharpParser.ARGLIST, CSharpParser.ASCENDING, CSharpParser.ASYNC, CSharpParser.AWAIT, CSharpParser.BASE, CSharpParser.BOOL, CSharpParser.BY, CSharpParser.BYTE, CSharpParser.CHAR, CSharpParser.CHECKED, CSharpParser.DECIMAL, CSharpParser.DEFAULT, CSharpParser.DELEGATE, CSharpParser.DESCENDING, CSharpParser.DOUBLE, CSharpParser.DYNAMIC, CSharpParser.EQUALS, CSharpParser.FALSE, CSharpParser.FLOAT, CSharpParser.FROM, CSharpParser.GET, CSharpParser.GROUP, CSharpParser.INT, CSharpParser.INTO, CSharpParser.JOIN, CSharpParser.LET, CSharpParser.LONG, CSharpParser.NAMEOF, CSharpParser.NEW, CSharpParser.NULL, CSharpParser.OBJECT, CSharpParser.ON, CSharpParser.ORDERBY, CSharpParser.PARTIAL, CSharpParser.REF, CSharpParser.REMOVE, CSharpParser.SBYTE, CSharpParser.SELECT, CSharpParser.SET, CSharpParser.SHORT, CSharpParser.SIZEOF, CSharpParser.STRING, CSharpParser.THIS, CSharpParser.THROW, CSharpParser.TRUE, CSharpParser.TYPEOF, CSharpParser.UINT, CSharpParser.ULONG, CSharpParser.UNCHECKED, CSharpParser.UNMANAGED, CSharpParser.USHORT, CSharpParser.VAR, CSharpParser.WHEN, CSharpParser.WHERE, CSharpParser.YIELD, CSharpParser.IDENTIFIER, CSharpParser.LITERAL_ACCESS, CSharpParser.INTEGER_LITERAL, CSharpParser.HEX_INTEGER_LITERAL, CSharpParser.BIN_INTEGER_LITERAL, CSharpParser.REAL_LITERAL, CSharpParser.CHARACTER_LITERAL, CSharpParser.REGULAR_STRING, CSharpParser.VERBATIUM_STRING, CSharpParser.INTERPOLATED_REGULAR_STRING_START, CSharpParser.INTERPOLATED_VERBATIUM_STRING_START, CSharpParser.OPEN_PARENS, CSharpParser.PLUS, CSharpParser.MINUS, CSharpParser.STAR, CSharpParser.AMP, CSharpParser.CARET, CSharpParser.BANG, CSharpParser.TILDE, CSharpParser.OP_INC, CSharpParser.OP_DEC, CSharpParser.OP_RANGE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1144
                self.throwable_expression()
                pass
            elif token in [CSharpParser.OPEN_BRACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1145
                self.block()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Query_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def from_clause(self):
            return self.getTypedRuleContext(CSharpParser.From_clauseContext,0)


        def query_body(self):
            return self.getTypedRuleContext(CSharpParser.Query_bodyContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_query_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery_expression" ):
                listener.enterQuery_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery_expression" ):
                listener.exitQuery_expression(self)




    def query_expression(self):

        localctx = CSharpParser.Query_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_query_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1148
            self.from_clause()
            self.state = 1149
            self.query_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class From_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FROM(self):
            return self.getToken(CSharpParser.FROM, 0)

        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def IN(self):
            return self.getToken(CSharpParser.IN, 0)

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def type_(self):
            return self.getTypedRuleContext(CSharpParser.Type_Context,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_from_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFrom_clause" ):
                listener.enterFrom_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFrom_clause" ):
                listener.exitFrom_clause(self)




    def from_clause(self):

        localctx = CSharpParser.From_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_from_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1151
            self.match(CSharpParser.FROM)
            self.state = 1153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,111,self._ctx)
            if la_ == 1:
                self.state = 1152
                self.type_()


            self.state = 1155
            self.identifier()
            self.state = 1156
            self.match(CSharpParser.IN)
            self.state = 1157
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Query_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def select_or_group_clause(self):
            return self.getTypedRuleContext(CSharpParser.Select_or_group_clauseContext,0)


        def query_body_clause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Query_body_clauseContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Query_body_clauseContext,i)


        def query_continuation(self):
            return self.getTypedRuleContext(CSharpParser.Query_continuationContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_query_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery_body" ):
                listener.enterQuery_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery_body" ):
                listener.exitQuery_body(self)




    def query_body(self):

        localctx = CSharpParser.Query_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_query_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 47)) & ~0x3f) == 0 and ((1 << (_la - 47)) & ((1 << (CSharpParser.FROM - 47)) | (1 << (CSharpParser.JOIN - 47)) | (1 << (CSharpParser.LET - 47)) | (1 << (CSharpParser.ORDERBY - 47)) | (1 << (CSharpParser.WHERE - 47)))) != 0):
                self.state = 1159
                self.query_body_clause()
                self.state = 1164
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1165
            self.select_or_group_clause()
            self.state = 1167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,113,self._ctx)
            if la_ == 1:
                self.state = 1166
                self.query_continuation()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Query_body_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def from_clause(self):
            return self.getTypedRuleContext(CSharpParser.From_clauseContext,0)


        def let_clause(self):
            return self.getTypedRuleContext(CSharpParser.Let_clauseContext,0)


        def where_clause(self):
            return self.getTypedRuleContext(CSharpParser.Where_clauseContext,0)


        def combined_join_clause(self):
            return self.getTypedRuleContext(CSharpParser.Combined_join_clauseContext,0)


        def orderby_clause(self):
            return self.getTypedRuleContext(CSharpParser.Orderby_clauseContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_query_body_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery_body_clause" ):
                listener.enterQuery_body_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery_body_clause" ):
                listener.exitQuery_body_clause(self)




    def query_body_clause(self):

        localctx = CSharpParser.Query_body_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_query_body_clause)
        try:
            self.state = 1174
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.FROM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1169
                self.from_clause()
                pass
            elif token in [CSharpParser.LET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1170
                self.let_clause()
                pass
            elif token in [CSharpParser.WHERE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1171
                self.where_clause()
                pass
            elif token in [CSharpParser.JOIN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 1172
                self.combined_join_clause()
                pass
            elif token in [CSharpParser.ORDERBY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 1173
                self.orderby_clause()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Let_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LET(self):
            return self.getToken(CSharpParser.LET, 0)

        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def ASSIGNMENT(self):
            return self.getToken(CSharpParser.ASSIGNMENT, 0)

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_let_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLet_clause" ):
                listener.enterLet_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLet_clause" ):
                listener.exitLet_clause(self)




    def let_clause(self):

        localctx = CSharpParser.Let_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_let_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1176
            self.match(CSharpParser.LET)
            self.state = 1177
            self.identifier()
            self.state = 1178
            self.match(CSharpParser.ASSIGNMENT)
            self.state = 1179
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Where_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHERE(self):
            return self.getToken(CSharpParser.WHERE, 0)

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_where_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhere_clause" ):
                listener.enterWhere_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhere_clause" ):
                listener.exitWhere_clause(self)




    def where_clause(self):

        localctx = CSharpParser.Where_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_where_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1181
            self.match(CSharpParser.WHERE)
            self.state = 1182
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Combined_join_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def JOIN(self):
            return self.getToken(CSharpParser.JOIN, 0)

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(CSharpParser.IdentifierContext,i)


        def IN(self):
            return self.getToken(CSharpParser.IN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CSharpParser.ExpressionContext,i)


        def ON(self):
            return self.getToken(CSharpParser.ON, 0)

        def EQUALS(self):
            return self.getToken(CSharpParser.EQUALS, 0)

        def type_(self):
            return self.getTypedRuleContext(CSharpParser.Type_Context,0)


        def INTO(self):
            return self.getToken(CSharpParser.INTO, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_combined_join_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCombined_join_clause" ):
                listener.enterCombined_join_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCombined_join_clause" ):
                listener.exitCombined_join_clause(self)




    def combined_join_clause(self):

        localctx = CSharpParser.Combined_join_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_combined_join_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1184
            self.match(CSharpParser.JOIN)
            self.state = 1186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,115,self._ctx)
            if la_ == 1:
                self.state = 1185
                self.type_()


            self.state = 1188
            self.identifier()
            self.state = 1189
            self.match(CSharpParser.IN)
            self.state = 1190
            self.expression()
            self.state = 1191
            self.match(CSharpParser.ON)
            self.state = 1192
            self.expression()
            self.state = 1193
            self.match(CSharpParser.EQUALS)
            self.state = 1194
            self.expression()
            self.state = 1197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.INTO:
                self.state = 1195
                self.match(CSharpParser.INTO)
                self.state = 1196
                self.identifier()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Orderby_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ORDERBY(self):
            return self.getToken(CSharpParser.ORDERBY, 0)

        def ordering(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.OrderingContext)
            else:
                return self.getTypedRuleContext(CSharpParser.OrderingContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_orderby_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrderby_clause" ):
                listener.enterOrderby_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrderby_clause" ):
                listener.exitOrderby_clause(self)




    def orderby_clause(self):

        localctx = CSharpParser.Orderby_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_orderby_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1199
            self.match(CSharpParser.ORDERBY)
            self.state = 1200
            self.ordering()
            self.state = 1205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.COMMA:
                self.state = 1201
                self.match(CSharpParser.COMMA)
                self.state = 1202
                self.ordering()
                self.state = 1207
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrderingContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.dire = None # Token

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def ASCENDING(self):
            return self.getToken(CSharpParser.ASCENDING, 0)

        def DESCENDING(self):
            return self.getToken(CSharpParser.DESCENDING, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_ordering

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrdering" ):
                listener.enterOrdering(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrdering" ):
                listener.exitOrdering(self)




    def ordering(self):

        localctx = CSharpParser.OrderingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_ordering)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1208
            self.expression()
            self.state = 1210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.ASCENDING or _la==CSharpParser.DESCENDING:
                self.state = 1209
                localctx.dire = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==CSharpParser.ASCENDING or _la==CSharpParser.DESCENDING):
                    localctx.dire = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Select_or_group_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELECT(self):
            return self.getToken(CSharpParser.SELECT, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CSharpParser.ExpressionContext,i)


        def GROUP(self):
            return self.getToken(CSharpParser.GROUP, 0)

        def BY(self):
            return self.getToken(CSharpParser.BY, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_select_or_group_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelect_or_group_clause" ):
                listener.enterSelect_or_group_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelect_or_group_clause" ):
                listener.exitSelect_or_group_clause(self)




    def select_or_group_clause(self):

        localctx = CSharpParser.Select_or_group_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_select_or_group_clause)
        try:
            self.state = 1219
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.SELECT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1212
                self.match(CSharpParser.SELECT)
                self.state = 1213
                self.expression()
                pass
            elif token in [CSharpParser.GROUP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1214
                self.match(CSharpParser.GROUP)
                self.state = 1215
                self.expression()
                self.state = 1216
                self.match(CSharpParser.BY)
                self.state = 1217
                self.expression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Query_continuationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTO(self):
            return self.getToken(CSharpParser.INTO, 0)

        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def query_body(self):
            return self.getTypedRuleContext(CSharpParser.Query_bodyContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_query_continuation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery_continuation" ):
                listener.enterQuery_continuation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery_continuation" ):
                listener.exitQuery_continuation(self)




    def query_continuation(self):

        localctx = CSharpParser.Query_continuationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_query_continuation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1221
            self.match(CSharpParser.INTO)
            self.state = 1222
            self.identifier()
            self.state = 1223
            self.query_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def labeled_Statement(self):
            return self.getTypedRuleContext(CSharpParser.Labeled_StatementContext,0)


        def declarationStatement(self):
            return self.getTypedRuleContext(CSharpParser.DeclarationStatementContext,0)


        def embedded_statement(self):
            return self.getTypedRuleContext(CSharpParser.Embedded_statementContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = CSharpParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_statement)
        try:
            self.state = 1228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,120,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1225
                self.labeled_Statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1226
                self.declarationStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1227
                self.embedded_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def local_variable_declaration(self):
            return self.getTypedRuleContext(CSharpParser.Local_variable_declarationContext,0)


        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def local_constant_declaration(self):
            return self.getTypedRuleContext(CSharpParser.Local_constant_declarationContext,0)


        def local_function_declaration(self):
            return self.getTypedRuleContext(CSharpParser.Local_function_declarationContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_declarationStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclarationStatement" ):
                listener.enterDeclarationStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclarationStatement" ):
                listener.exitDeclarationStatement(self)




    def declarationStatement(self):

        localctx = CSharpParser.DeclarationStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_declarationStatement)
        try:
            self.state = 1237
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,121,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1230
                self.local_variable_declaration()
                self.state = 1231
                self.match(CSharpParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1233
                self.local_constant_declaration()
                self.state = 1234
                self.match(CSharpParser.SEMICOLON)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1236
                self.local_function_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Local_function_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def local_function_header(self):
            return self.getTypedRuleContext(CSharpParser.Local_function_headerContext,0)


        def local_function_body(self):
            return self.getTypedRuleContext(CSharpParser.Local_function_bodyContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_local_function_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocal_function_declaration" ):
                listener.enterLocal_function_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocal_function_declaration" ):
                listener.exitLocal_function_declaration(self)




    def local_function_declaration(self):

        localctx = CSharpParser.Local_function_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_local_function_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1239
            self.local_function_header()
            self.state = 1240
            self.local_function_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Local_function_headerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def return_type(self):
            return self.getTypedRuleContext(CSharpParser.Return_typeContext,0)


        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)

        def local_function_modifiers(self):
            return self.getTypedRuleContext(CSharpParser.Local_function_modifiersContext,0)


        def type_parameter_list(self):
            return self.getTypedRuleContext(CSharpParser.Type_parameter_listContext,0)


        def formal_parameter_list(self):
            return self.getTypedRuleContext(CSharpParser.Formal_parameter_listContext,0)


        def type_parameter_constraints_clauses(self):
            return self.getTypedRuleContext(CSharpParser.Type_parameter_constraints_clausesContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_local_function_header

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocal_function_header" ):
                listener.enterLocal_function_header(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocal_function_header" ):
                listener.exitLocal_function_header(self)




    def local_function_header(self):

        localctx = CSharpParser.Local_function_headerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_local_function_header)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1243
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,122,self._ctx)
            if la_ == 1:
                self.state = 1242
                self.local_function_modifiers()


            self.state = 1245
            self.return_type()
            self.state = 1246
            self.identifier()
            self.state = 1248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.LT:
                self.state = 1247
                self.type_parameter_list()


            self.state = 1250
            self.match(CSharpParser.OPEN_PARENS)
            self.state = 1252
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BOOL) | (1 << CSharpParser.BY) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.IN) | (1 << CSharpParser.INT) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.LONG) | (1 << CSharpParser.NAMEOF))) != 0) or ((((_la - 67)) & ~0x3f) == 0 and ((1 << (_la - 67)) & ((1 << (CSharpParser.OBJECT - 67)) | (1 << (CSharpParser.ON - 67)) | (1 << (CSharpParser.ORDERBY - 67)) | (1 << (CSharpParser.OUT - 67)) | (1 << (CSharpParser.PARAMS - 67)) | (1 << (CSharpParser.PARTIAL - 67)) | (1 << (CSharpParser.REF - 67)) | (1 << (CSharpParser.REMOVE - 67)) | (1 << (CSharpParser.SBYTE - 67)) | (1 << (CSharpParser.SELECT - 67)) | (1 << (CSharpParser.SET - 67)) | (1 << (CSharpParser.SHORT - 67)) | (1 << (CSharpParser.STRING - 67)) | (1 << (CSharpParser.THIS - 67)) | (1 << (CSharpParser.UINT - 67)) | (1 << (CSharpParser.ULONG - 67)) | (1 << (CSharpParser.UNMANAGED - 67)) | (1 << (CSharpParser.USHORT - 67)) | (1 << (CSharpParser.VAR - 67)) | (1 << (CSharpParser.VOID - 67)) | (1 << (CSharpParser.WHEN - 67)) | (1 << (CSharpParser.WHERE - 67)) | (1 << (CSharpParser.YIELD - 67)) | (1 << (CSharpParser.IDENTIFIER - 67)) | (1 << (CSharpParser.OPEN_BRACKET - 67)) | (1 << (CSharpParser.OPEN_PARENS - 67)))) != 0):
                self.state = 1251
                self.formal_parameter_list()


            self.state = 1254
            self.match(CSharpParser.CLOSE_PARENS)
            self.state = 1256
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.WHERE:
                self.state = 1255
                self.type_parameter_constraints_clauses()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Local_function_modifiersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASYNC(self):
            return self.getToken(CSharpParser.ASYNC, 0)

        def UNSAFE(self):
            return self.getToken(CSharpParser.UNSAFE, 0)

        def STATIC(self):
            return self.getToken(CSharpParser.STATIC, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_local_function_modifiers

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocal_function_modifiers" ):
                listener.enterLocal_function_modifiers(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocal_function_modifiers" ):
                listener.exitLocal_function_modifiers(self)




    def local_function_modifiers(self):

        localctx = CSharpParser.Local_function_modifiersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 160, self.RULE_local_function_modifiers)
        self._la = 0 # Token type
        try:
            self.state = 1264
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.ASYNC, CSharpParser.UNSAFE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1258
                _la = self._input.LA(1)
                if not(_la==CSharpParser.ASYNC or _la==CSharpParser.UNSAFE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 1260
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.STATIC:
                    self.state = 1259
                    self.match(CSharpParser.STATIC)


                pass
            elif token in [CSharpParser.STATIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1262
                self.match(CSharpParser.STATIC)
                self.state = 1263
                _la = self._input.LA(1)
                if not(_la==CSharpParser.ASYNC or _la==CSharpParser.UNSAFE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Local_function_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(CSharpParser.BlockContext,0)


        def right_arrow(self):
            return self.getTypedRuleContext(CSharpParser.Right_arrowContext,0)


        def throwable_expression(self):
            return self.getTypedRuleContext(CSharpParser.Throwable_expressionContext,0)


        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_local_function_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocal_function_body" ):
                listener.enterLocal_function_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocal_function_body" ):
                listener.exitLocal_function_body(self)




    def local_function_body(self):

        localctx = CSharpParser.Local_function_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 162, self.RULE_local_function_body)
        try:
            self.state = 1271
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.OPEN_BRACE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1266
                self.block()
                pass
            elif token in [CSharpParser.ASSIGNMENT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1267
                self.right_arrow()
                self.state = 1268
                self.throwable_expression()
                self.state = 1269
                self.match(CSharpParser.SEMICOLON)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Labeled_StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def COLON(self):
            return self.getToken(CSharpParser.COLON, 0)

        def statement(self):
            return self.getTypedRuleContext(CSharpParser.StatementContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_labeled_Statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabeled_Statement" ):
                listener.enterLabeled_Statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabeled_Statement" ):
                listener.exitLabeled_Statement(self)




    def labeled_Statement(self):

        localctx = CSharpParser.Labeled_StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 164, self.RULE_labeled_Statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1273
            self.identifier()
            self.state = 1274
            self.match(CSharpParser.COLON)
            self.state = 1275
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Embedded_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(CSharpParser.BlockContext,0)


        def simple_embedded_statement(self):
            return self.getTypedRuleContext(CSharpParser.Simple_embedded_statementContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_embedded_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmbedded_statement" ):
                listener.enterEmbedded_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmbedded_statement" ):
                listener.exitEmbedded_statement(self)




    def embedded_statement(self):

        localctx = CSharpParser.Embedded_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 166, self.RULE_embedded_statement)
        try:
            self.state = 1279
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.OPEN_BRACE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1277
                self.block()
                pass
            elif token in [CSharpParser.ADD, CSharpParser.ALIAS, CSharpParser.ARGLIST, CSharpParser.ASCENDING, CSharpParser.ASYNC, CSharpParser.AWAIT, CSharpParser.BASE, CSharpParser.BOOL, CSharpParser.BREAK, CSharpParser.BY, CSharpParser.BYTE, CSharpParser.CHAR, CSharpParser.CHECKED, CSharpParser.CONTINUE, CSharpParser.DECIMAL, CSharpParser.DEFAULT, CSharpParser.DELEGATE, CSharpParser.DESCENDING, CSharpParser.DO, CSharpParser.DOUBLE, CSharpParser.DYNAMIC, CSharpParser.EQUALS, CSharpParser.FALSE, CSharpParser.FIXED, CSharpParser.FLOAT, CSharpParser.FOR, CSharpParser.FOREACH, CSharpParser.FROM, CSharpParser.GET, CSharpParser.GOTO, CSharpParser.GROUP, CSharpParser.IF, CSharpParser.INT, CSharpParser.INTO, CSharpParser.JOIN, CSharpParser.LET, CSharpParser.LOCK, CSharpParser.LONG, CSharpParser.NAMEOF, CSharpParser.NEW, CSharpParser.NULL, CSharpParser.OBJECT, CSharpParser.ON, CSharpParser.ORDERBY, CSharpParser.PARTIAL, CSharpParser.REF, CSharpParser.REMOVE, CSharpParser.RETURN, CSharpParser.SBYTE, CSharpParser.SELECT, CSharpParser.SET, CSharpParser.SHORT, CSharpParser.SIZEOF, CSharpParser.STRING, CSharpParser.SWITCH, CSharpParser.THIS, CSharpParser.THROW, CSharpParser.TRUE, CSharpParser.TRY, CSharpParser.TYPEOF, CSharpParser.UINT, CSharpParser.ULONG, CSharpParser.UNCHECKED, CSharpParser.UNMANAGED, CSharpParser.UNSAFE, CSharpParser.USHORT, CSharpParser.USING, CSharpParser.VAR, CSharpParser.WHEN, CSharpParser.WHERE, CSharpParser.WHILE, CSharpParser.YIELD, CSharpParser.IDENTIFIER, CSharpParser.LITERAL_ACCESS, CSharpParser.INTEGER_LITERAL, CSharpParser.HEX_INTEGER_LITERAL, CSharpParser.BIN_INTEGER_LITERAL, CSharpParser.REAL_LITERAL, CSharpParser.CHARACTER_LITERAL, CSharpParser.REGULAR_STRING, CSharpParser.VERBATIUM_STRING, CSharpParser.INTERPOLATED_REGULAR_STRING_START, CSharpParser.INTERPOLATED_VERBATIUM_STRING_START, CSharpParser.OPEN_PARENS, CSharpParser.SEMICOLON, CSharpParser.PLUS, CSharpParser.MINUS, CSharpParser.STAR, CSharpParser.AMP, CSharpParser.CARET, CSharpParser.BANG, CSharpParser.TILDE, CSharpParser.OP_INC, CSharpParser.OP_DEC, CSharpParser.OP_RANGE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1278
                self.simple_embedded_statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_embedded_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CSharpParser.RULE_simple_embedded_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TryStatementContext(Simple_embedded_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Simple_embedded_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TRY(self):
            return self.getToken(CSharpParser.TRY, 0)
        def block(self):
            return self.getTypedRuleContext(CSharpParser.BlockContext,0)

        def catch_clauses(self):
            return self.getTypedRuleContext(CSharpParser.Catch_clausesContext,0)

        def finally_clause(self):
            return self.getTypedRuleContext(CSharpParser.Finally_clauseContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTryStatement" ):
                listener.enterTryStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTryStatement" ):
                listener.exitTryStatement(self)


    class CheckedStatementContext(Simple_embedded_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Simple_embedded_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CHECKED(self):
            return self.getToken(CSharpParser.CHECKED, 0)
        def block(self):
            return self.getTypedRuleContext(CSharpParser.BlockContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCheckedStatement" ):
                listener.enterCheckedStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCheckedStatement" ):
                listener.exitCheckedStatement(self)


    class ThrowStatementContext(Simple_embedded_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Simple_embedded_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def THROW(self):
            return self.getToken(CSharpParser.THROW, 0)
        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)
        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThrowStatement" ):
                listener.enterThrowStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThrowStatement" ):
                listener.exitThrowStatement(self)


    class TheEmptyStatementContext(Simple_embedded_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Simple_embedded_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTheEmptyStatement" ):
                listener.enterTheEmptyStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTheEmptyStatement" ):
                listener.exitTheEmptyStatement(self)


    class UnsafeStatementContext(Simple_embedded_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Simple_embedded_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def UNSAFE(self):
            return self.getToken(CSharpParser.UNSAFE, 0)
        def block(self):
            return self.getTypedRuleContext(CSharpParser.BlockContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnsafeStatement" ):
                listener.enterUnsafeStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnsafeStatement" ):
                listener.exitUnsafeStatement(self)


    class ForStatementContext(Simple_embedded_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Simple_embedded_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FOR(self):
            return self.getToken(CSharpParser.FOR, 0)
        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)
        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.SEMICOLON)
            else:
                return self.getToken(CSharpParser.SEMICOLON, i)
        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)
        def embedded_statement(self):
            return self.getTypedRuleContext(CSharpParser.Embedded_statementContext,0)

        def for_initializer(self):
            return self.getTypedRuleContext(CSharpParser.For_initializerContext,0)

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)

        def for_iterator(self):
            return self.getTypedRuleContext(CSharpParser.For_iteratorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)


    class BreakStatementContext(Simple_embedded_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Simple_embedded_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BREAK(self):
            return self.getToken(CSharpParser.BREAK, 0)
        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakStatement" ):
                listener.enterBreakStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakStatement" ):
                listener.exitBreakStatement(self)


    class IfStatementContext(Simple_embedded_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Simple_embedded_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(CSharpParser.IF, 0)
        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)
        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)
        def if_body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.If_bodyContext)
            else:
                return self.getTypedRuleContext(CSharpParser.If_bodyContext,i)

        def ELSE(self):
            return self.getToken(CSharpParser.ELSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)


    class ReturnStatementContext(Simple_embedded_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Simple_embedded_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(CSharpParser.RETURN, 0)
        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)
        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)


    class GotoStatementContext(Simple_embedded_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Simple_embedded_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def GOTO(self):
            return self.getToken(CSharpParser.GOTO, 0)
        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)
        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)

        def CASE(self):
            return self.getToken(CSharpParser.CASE, 0)
        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)

        def DEFAULT(self):
            return self.getToken(CSharpParser.DEFAULT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGotoStatement" ):
                listener.enterGotoStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGotoStatement" ):
                listener.exitGotoStatement(self)


    class SwitchStatementContext(Simple_embedded_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Simple_embedded_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SWITCH(self):
            return self.getToken(CSharpParser.SWITCH, 0)
        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)
        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)
        def OPEN_BRACE(self):
            return self.getToken(CSharpParser.OPEN_BRACE, 0)
        def CLOSE_BRACE(self):
            return self.getToken(CSharpParser.CLOSE_BRACE, 0)
        def switch_section(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Switch_sectionContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Switch_sectionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchStatement" ):
                listener.enterSwitchStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchStatement" ):
                listener.exitSwitchStatement(self)


    class FixedStatementContext(Simple_embedded_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Simple_embedded_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FIXED(self):
            return self.getToken(CSharpParser.FIXED, 0)
        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)
        def pointer_type(self):
            return self.getTypedRuleContext(CSharpParser.Pointer_typeContext,0)

        def fixed_pointer_declarators(self):
            return self.getTypedRuleContext(CSharpParser.Fixed_pointer_declaratorsContext,0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)
        def embedded_statement(self):
            return self.getTypedRuleContext(CSharpParser.Embedded_statementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFixedStatement" ):
                listener.enterFixedStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFixedStatement" ):
                listener.exitFixedStatement(self)


    class WhileStatementContext(Simple_embedded_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Simple_embedded_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(CSharpParser.WHILE, 0)
        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)
        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)
        def embedded_statement(self):
            return self.getTypedRuleContext(CSharpParser.Embedded_statementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)


    class DoStatementContext(Simple_embedded_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Simple_embedded_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DO(self):
            return self.getToken(CSharpParser.DO, 0)
        def embedded_statement(self):
            return self.getTypedRuleContext(CSharpParser.Embedded_statementContext,0)

        def WHILE(self):
            return self.getToken(CSharpParser.WHILE, 0)
        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)
        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)
        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoStatement" ):
                listener.enterDoStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoStatement" ):
                listener.exitDoStatement(self)


    class ForeachStatementContext(Simple_embedded_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Simple_embedded_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FOREACH(self):
            return self.getToken(CSharpParser.FOREACH, 0)
        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)
        def local_variable_type(self):
            return self.getTypedRuleContext(CSharpParser.Local_variable_typeContext,0)

        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)

        def IN(self):
            return self.getToken(CSharpParser.IN, 0)
        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)
        def embedded_statement(self):
            return self.getTypedRuleContext(CSharpParser.Embedded_statementContext,0)

        def AWAIT(self):
            return self.getToken(CSharpParser.AWAIT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForeachStatement" ):
                listener.enterForeachStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForeachStatement" ):
                listener.exitForeachStatement(self)


    class UncheckedStatementContext(Simple_embedded_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Simple_embedded_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def UNCHECKED(self):
            return self.getToken(CSharpParser.UNCHECKED, 0)
        def block(self):
            return self.getTypedRuleContext(CSharpParser.BlockContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUncheckedStatement" ):
                listener.enterUncheckedStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUncheckedStatement" ):
                listener.exitUncheckedStatement(self)


    class ExpressionStatementContext(Simple_embedded_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Simple_embedded_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)

        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionStatement" ):
                listener.enterExpressionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionStatement" ):
                listener.exitExpressionStatement(self)


    class ContinueStatementContext(Simple_embedded_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Simple_embedded_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CONTINUE(self):
            return self.getToken(CSharpParser.CONTINUE, 0)
        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinueStatement" ):
                listener.enterContinueStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinueStatement" ):
                listener.exitContinueStatement(self)


    class UsingStatementContext(Simple_embedded_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Simple_embedded_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def USING(self):
            return self.getToken(CSharpParser.USING, 0)
        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)
        def resource_acquisition(self):
            return self.getTypedRuleContext(CSharpParser.Resource_acquisitionContext,0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)
        def embedded_statement(self):
            return self.getTypedRuleContext(CSharpParser.Embedded_statementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUsingStatement" ):
                listener.enterUsingStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUsingStatement" ):
                listener.exitUsingStatement(self)


    class LockStatementContext(Simple_embedded_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Simple_embedded_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LOCK(self):
            return self.getToken(CSharpParser.LOCK, 0)
        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)
        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)
        def embedded_statement(self):
            return self.getTypedRuleContext(CSharpParser.Embedded_statementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLockStatement" ):
                listener.enterLockStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLockStatement" ):
                listener.exitLockStatement(self)


    class YieldStatementContext(Simple_embedded_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Simple_embedded_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def YIELD(self):
            return self.getToken(CSharpParser.YIELD, 0)
        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)
        def RETURN(self):
            return self.getToken(CSharpParser.RETURN, 0)
        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)

        def BREAK(self):
            return self.getToken(CSharpParser.BREAK, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterYieldStatement" ):
                listener.enterYieldStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitYieldStatement" ):
                listener.exitYieldStatement(self)



    def simple_embedded_statement(self):

        localctx = CSharpParser.Simple_embedded_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 168, self.RULE_simple_embedded_statement)
        self._la = 0 # Token type
        try:
            self.state = 1411
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,142,self._ctx)
            if la_ == 1:
                localctx = CSharpParser.TheEmptyStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1281
                self.match(CSharpParser.SEMICOLON)
                pass

            elif la_ == 2:
                localctx = CSharpParser.ExpressionStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1282
                self.expression()
                self.state = 1283
                self.match(CSharpParser.SEMICOLON)
                pass

            elif la_ == 3:
                localctx = CSharpParser.IfStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1285
                self.match(CSharpParser.IF)
                self.state = 1286
                self.match(CSharpParser.OPEN_PARENS)
                self.state = 1287
                self.expression()
                self.state = 1288
                self.match(CSharpParser.CLOSE_PARENS)
                self.state = 1289
                self.if_body()
                self.state = 1292
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,130,self._ctx)
                if la_ == 1:
                    self.state = 1290
                    self.match(CSharpParser.ELSE)
                    self.state = 1291
                    self.if_body()


                pass

            elif la_ == 4:
                localctx = CSharpParser.SwitchStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1294
                self.match(CSharpParser.SWITCH)
                self.state = 1295
                self.match(CSharpParser.OPEN_PARENS)
                self.state = 1296
                self.expression()
                self.state = 1297
                self.match(CSharpParser.CLOSE_PARENS)
                self.state = 1298
                self.match(CSharpParser.OPEN_BRACE)
                self.state = 1302
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CSharpParser.CASE or _la==CSharpParser.DEFAULT:
                    self.state = 1299
                    self.switch_section()
                    self.state = 1304
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 1305
                self.match(CSharpParser.CLOSE_BRACE)
                pass

            elif la_ == 5:
                localctx = CSharpParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1307
                self.match(CSharpParser.WHILE)
                self.state = 1308
                self.match(CSharpParser.OPEN_PARENS)
                self.state = 1309
                self.expression()
                self.state = 1310
                self.match(CSharpParser.CLOSE_PARENS)
                self.state = 1311
                self.embedded_statement()
                pass

            elif la_ == 6:
                localctx = CSharpParser.DoStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1313
                self.match(CSharpParser.DO)
                self.state = 1314
                self.embedded_statement()
                self.state = 1315
                self.match(CSharpParser.WHILE)
                self.state = 1316
                self.match(CSharpParser.OPEN_PARENS)
                self.state = 1317
                self.expression()
                self.state = 1318
                self.match(CSharpParser.CLOSE_PARENS)
                self.state = 1319
                self.match(CSharpParser.SEMICOLON)
                pass

            elif la_ == 7:
                localctx = CSharpParser.ForStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 1321
                self.match(CSharpParser.FOR)
                self.state = 1322
                self.match(CSharpParser.OPEN_PARENS)
                self.state = 1324
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BASE) | (1 << CSharpParser.BOOL) | (1 << CSharpParser.BY) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.CHECKED) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DEFAULT) | (1 << CSharpParser.DELEGATE) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FALSE) | (1 << CSharpParser.FIXED) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.INT) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.LONG) | (1 << CSharpParser.NAMEOF))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (CSharpParser.NEW - 65)) | (1 << (CSharpParser.NULL - 65)) | (1 << (CSharpParser.OBJECT - 65)) | (1 << (CSharpParser.ON - 65)) | (1 << (CSharpParser.ORDERBY - 65)) | (1 << (CSharpParser.PARTIAL - 65)) | (1 << (CSharpParser.REF - 65)) | (1 << (CSharpParser.REMOVE - 65)) | (1 << (CSharpParser.SBYTE - 65)) | (1 << (CSharpParser.SELECT - 65)) | (1 << (CSharpParser.SET - 65)) | (1 << (CSharpParser.SHORT - 65)) | (1 << (CSharpParser.SIZEOF - 65)) | (1 << (CSharpParser.STRING - 65)) | (1 << (CSharpParser.THIS - 65)) | (1 << (CSharpParser.TRUE - 65)) | (1 << (CSharpParser.TYPEOF - 65)) | (1 << (CSharpParser.UINT - 65)) | (1 << (CSharpParser.ULONG - 65)) | (1 << (CSharpParser.UNCHECKED - 65)) | (1 << (CSharpParser.UNMANAGED - 65)) | (1 << (CSharpParser.USHORT - 65)) | (1 << (CSharpParser.USING - 65)) | (1 << (CSharpParser.VAR - 65)) | (1 << (CSharpParser.VOID - 65)) | (1 << (CSharpParser.WHEN - 65)) | (1 << (CSharpParser.WHERE - 65)) | (1 << (CSharpParser.YIELD - 65)) | (1 << (CSharpParser.IDENTIFIER - 65)) | (1 << (CSharpParser.LITERAL_ACCESS - 65)) | (1 << (CSharpParser.INTEGER_LITERAL - 65)) | (1 << (CSharpParser.HEX_INTEGER_LITERAL - 65)) | (1 << (CSharpParser.BIN_INTEGER_LITERAL - 65)) | (1 << (CSharpParser.REAL_LITERAL - 65)) | (1 << (CSharpParser.CHARACTER_LITERAL - 65)) | (1 << (CSharpParser.REGULAR_STRING - 65)) | (1 << (CSharpParser.VERBATIUM_STRING - 65)) | (1 << (CSharpParser.INTERPOLATED_REGULAR_STRING_START - 65)) | (1 << (CSharpParser.INTERPOLATED_VERBATIUM_STRING_START - 65)) | (1 << (CSharpParser.OPEN_PARENS - 65)))) != 0) or ((((_la - 134)) & ~0x3f) == 0 and ((1 << (_la - 134)) & ((1 << (CSharpParser.PLUS - 134)) | (1 << (CSharpParser.MINUS - 134)) | (1 << (CSharpParser.STAR - 134)) | (1 << (CSharpParser.AMP - 134)) | (1 << (CSharpParser.CARET - 134)) | (1 << (CSharpParser.BANG - 134)) | (1 << (CSharpParser.TILDE - 134)) | (1 << (CSharpParser.OP_INC - 134)) | (1 << (CSharpParser.OP_DEC - 134)) | (1 << (CSharpParser.OP_RANGE - 134)))) != 0):
                    self.state = 1323
                    self.for_initializer()


                self.state = 1326
                self.match(CSharpParser.SEMICOLON)
                self.state = 1328
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BASE) | (1 << CSharpParser.BOOL) | (1 << CSharpParser.BY) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.CHECKED) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DEFAULT) | (1 << CSharpParser.DELEGATE) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FALSE) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.INT) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.LONG) | (1 << CSharpParser.NAMEOF))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (CSharpParser.NEW - 65)) | (1 << (CSharpParser.NULL - 65)) | (1 << (CSharpParser.OBJECT - 65)) | (1 << (CSharpParser.ON - 65)) | (1 << (CSharpParser.ORDERBY - 65)) | (1 << (CSharpParser.PARTIAL - 65)) | (1 << (CSharpParser.REF - 65)) | (1 << (CSharpParser.REMOVE - 65)) | (1 << (CSharpParser.SBYTE - 65)) | (1 << (CSharpParser.SELECT - 65)) | (1 << (CSharpParser.SET - 65)) | (1 << (CSharpParser.SHORT - 65)) | (1 << (CSharpParser.SIZEOF - 65)) | (1 << (CSharpParser.STRING - 65)) | (1 << (CSharpParser.THIS - 65)) | (1 << (CSharpParser.TRUE - 65)) | (1 << (CSharpParser.TYPEOF - 65)) | (1 << (CSharpParser.UINT - 65)) | (1 << (CSharpParser.ULONG - 65)) | (1 << (CSharpParser.UNCHECKED - 65)) | (1 << (CSharpParser.UNMANAGED - 65)) | (1 << (CSharpParser.USHORT - 65)) | (1 << (CSharpParser.VAR - 65)) | (1 << (CSharpParser.WHEN - 65)) | (1 << (CSharpParser.WHERE - 65)) | (1 << (CSharpParser.YIELD - 65)) | (1 << (CSharpParser.IDENTIFIER - 65)) | (1 << (CSharpParser.LITERAL_ACCESS - 65)) | (1 << (CSharpParser.INTEGER_LITERAL - 65)) | (1 << (CSharpParser.HEX_INTEGER_LITERAL - 65)) | (1 << (CSharpParser.BIN_INTEGER_LITERAL - 65)) | (1 << (CSharpParser.REAL_LITERAL - 65)) | (1 << (CSharpParser.CHARACTER_LITERAL - 65)) | (1 << (CSharpParser.REGULAR_STRING - 65)) | (1 << (CSharpParser.VERBATIUM_STRING - 65)) | (1 << (CSharpParser.INTERPOLATED_REGULAR_STRING_START - 65)) | (1 << (CSharpParser.INTERPOLATED_VERBATIUM_STRING_START - 65)) | (1 << (CSharpParser.OPEN_PARENS - 65)))) != 0) or ((((_la - 134)) & ~0x3f) == 0 and ((1 << (_la - 134)) & ((1 << (CSharpParser.PLUS - 134)) | (1 << (CSharpParser.MINUS - 134)) | (1 << (CSharpParser.STAR - 134)) | (1 << (CSharpParser.AMP - 134)) | (1 << (CSharpParser.CARET - 134)) | (1 << (CSharpParser.BANG - 134)) | (1 << (CSharpParser.TILDE - 134)) | (1 << (CSharpParser.OP_INC - 134)) | (1 << (CSharpParser.OP_DEC - 134)) | (1 << (CSharpParser.OP_RANGE - 134)))) != 0):
                    self.state = 1327
                    self.expression()


                self.state = 1330
                self.match(CSharpParser.SEMICOLON)
                self.state = 1332
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BASE) | (1 << CSharpParser.BOOL) | (1 << CSharpParser.BY) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.CHECKED) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DEFAULT) | (1 << CSharpParser.DELEGATE) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FALSE) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.INT) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.LONG) | (1 << CSharpParser.NAMEOF))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (CSharpParser.NEW - 65)) | (1 << (CSharpParser.NULL - 65)) | (1 << (CSharpParser.OBJECT - 65)) | (1 << (CSharpParser.ON - 65)) | (1 << (CSharpParser.ORDERBY - 65)) | (1 << (CSharpParser.PARTIAL - 65)) | (1 << (CSharpParser.REF - 65)) | (1 << (CSharpParser.REMOVE - 65)) | (1 << (CSharpParser.SBYTE - 65)) | (1 << (CSharpParser.SELECT - 65)) | (1 << (CSharpParser.SET - 65)) | (1 << (CSharpParser.SHORT - 65)) | (1 << (CSharpParser.SIZEOF - 65)) | (1 << (CSharpParser.STRING - 65)) | (1 << (CSharpParser.THIS - 65)) | (1 << (CSharpParser.TRUE - 65)) | (1 << (CSharpParser.TYPEOF - 65)) | (1 << (CSharpParser.UINT - 65)) | (1 << (CSharpParser.ULONG - 65)) | (1 << (CSharpParser.UNCHECKED - 65)) | (1 << (CSharpParser.UNMANAGED - 65)) | (1 << (CSharpParser.USHORT - 65)) | (1 << (CSharpParser.VAR - 65)) | (1 << (CSharpParser.WHEN - 65)) | (1 << (CSharpParser.WHERE - 65)) | (1 << (CSharpParser.YIELD - 65)) | (1 << (CSharpParser.IDENTIFIER - 65)) | (1 << (CSharpParser.LITERAL_ACCESS - 65)) | (1 << (CSharpParser.INTEGER_LITERAL - 65)) | (1 << (CSharpParser.HEX_INTEGER_LITERAL - 65)) | (1 << (CSharpParser.BIN_INTEGER_LITERAL - 65)) | (1 << (CSharpParser.REAL_LITERAL - 65)) | (1 << (CSharpParser.CHARACTER_LITERAL - 65)) | (1 << (CSharpParser.REGULAR_STRING - 65)) | (1 << (CSharpParser.VERBATIUM_STRING - 65)) | (1 << (CSharpParser.INTERPOLATED_REGULAR_STRING_START - 65)) | (1 << (CSharpParser.INTERPOLATED_VERBATIUM_STRING_START - 65)) | (1 << (CSharpParser.OPEN_PARENS - 65)))) != 0) or ((((_la - 134)) & ~0x3f) == 0 and ((1 << (_la - 134)) & ((1 << (CSharpParser.PLUS - 134)) | (1 << (CSharpParser.MINUS - 134)) | (1 << (CSharpParser.STAR - 134)) | (1 << (CSharpParser.AMP - 134)) | (1 << (CSharpParser.CARET - 134)) | (1 << (CSharpParser.BANG - 134)) | (1 << (CSharpParser.TILDE - 134)) | (1 << (CSharpParser.OP_INC - 134)) | (1 << (CSharpParser.OP_DEC - 134)) | (1 << (CSharpParser.OP_RANGE - 134)))) != 0):
                    self.state = 1331
                    self.for_iterator()


                self.state = 1334
                self.match(CSharpParser.CLOSE_PARENS)
                self.state = 1335
                self.embedded_statement()
                pass

            elif la_ == 8:
                localctx = CSharpParser.ForeachStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 1337
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.AWAIT:
                    self.state = 1336
                    self.match(CSharpParser.AWAIT)


                self.state = 1339
                self.match(CSharpParser.FOREACH)
                self.state = 1340
                self.match(CSharpParser.OPEN_PARENS)
                self.state = 1341
                self.local_variable_type()
                self.state = 1342
                self.identifier()
                self.state = 1343
                self.match(CSharpParser.IN)
                self.state = 1344
                self.expression()
                self.state = 1345
                self.match(CSharpParser.CLOSE_PARENS)
                self.state = 1346
                self.embedded_statement()
                pass

            elif la_ == 9:
                localctx = CSharpParser.BreakStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 1348
                self.match(CSharpParser.BREAK)
                self.state = 1349
                self.match(CSharpParser.SEMICOLON)
                pass

            elif la_ == 10:
                localctx = CSharpParser.ContinueStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 1350
                self.match(CSharpParser.CONTINUE)
                self.state = 1351
                self.match(CSharpParser.SEMICOLON)
                pass

            elif la_ == 11:
                localctx = CSharpParser.GotoStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 1352
                self.match(CSharpParser.GOTO)
                self.state = 1357
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSharpParser.ADD, CSharpParser.ALIAS, CSharpParser.ARGLIST, CSharpParser.ASCENDING, CSharpParser.ASYNC, CSharpParser.AWAIT, CSharpParser.BY, CSharpParser.DESCENDING, CSharpParser.DYNAMIC, CSharpParser.EQUALS, CSharpParser.FROM, CSharpParser.GET, CSharpParser.GROUP, CSharpParser.INTO, CSharpParser.JOIN, CSharpParser.LET, CSharpParser.NAMEOF, CSharpParser.ON, CSharpParser.ORDERBY, CSharpParser.PARTIAL, CSharpParser.REMOVE, CSharpParser.SELECT, CSharpParser.SET, CSharpParser.UNMANAGED, CSharpParser.VAR, CSharpParser.WHEN, CSharpParser.WHERE, CSharpParser.YIELD, CSharpParser.IDENTIFIER]:
                    self.state = 1353
                    self.identifier()
                    pass
                elif token in [CSharpParser.CASE]:
                    self.state = 1354
                    self.match(CSharpParser.CASE)
                    self.state = 1355
                    self.expression()
                    pass
                elif token in [CSharpParser.DEFAULT]:
                    self.state = 1356
                    self.match(CSharpParser.DEFAULT)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 1359
                self.match(CSharpParser.SEMICOLON)
                pass

            elif la_ == 12:
                localctx = CSharpParser.ReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 1360
                self.match(CSharpParser.RETURN)
                self.state = 1362
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BASE) | (1 << CSharpParser.BOOL) | (1 << CSharpParser.BY) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.CHECKED) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DEFAULT) | (1 << CSharpParser.DELEGATE) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FALSE) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.INT) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.LONG) | (1 << CSharpParser.NAMEOF))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (CSharpParser.NEW - 65)) | (1 << (CSharpParser.NULL - 65)) | (1 << (CSharpParser.OBJECT - 65)) | (1 << (CSharpParser.ON - 65)) | (1 << (CSharpParser.ORDERBY - 65)) | (1 << (CSharpParser.PARTIAL - 65)) | (1 << (CSharpParser.REF - 65)) | (1 << (CSharpParser.REMOVE - 65)) | (1 << (CSharpParser.SBYTE - 65)) | (1 << (CSharpParser.SELECT - 65)) | (1 << (CSharpParser.SET - 65)) | (1 << (CSharpParser.SHORT - 65)) | (1 << (CSharpParser.SIZEOF - 65)) | (1 << (CSharpParser.STRING - 65)) | (1 << (CSharpParser.THIS - 65)) | (1 << (CSharpParser.TRUE - 65)) | (1 << (CSharpParser.TYPEOF - 65)) | (1 << (CSharpParser.UINT - 65)) | (1 << (CSharpParser.ULONG - 65)) | (1 << (CSharpParser.UNCHECKED - 65)) | (1 << (CSharpParser.UNMANAGED - 65)) | (1 << (CSharpParser.USHORT - 65)) | (1 << (CSharpParser.VAR - 65)) | (1 << (CSharpParser.WHEN - 65)) | (1 << (CSharpParser.WHERE - 65)) | (1 << (CSharpParser.YIELD - 65)) | (1 << (CSharpParser.IDENTIFIER - 65)) | (1 << (CSharpParser.LITERAL_ACCESS - 65)) | (1 << (CSharpParser.INTEGER_LITERAL - 65)) | (1 << (CSharpParser.HEX_INTEGER_LITERAL - 65)) | (1 << (CSharpParser.BIN_INTEGER_LITERAL - 65)) | (1 << (CSharpParser.REAL_LITERAL - 65)) | (1 << (CSharpParser.CHARACTER_LITERAL - 65)) | (1 << (CSharpParser.REGULAR_STRING - 65)) | (1 << (CSharpParser.VERBATIUM_STRING - 65)) | (1 << (CSharpParser.INTERPOLATED_REGULAR_STRING_START - 65)) | (1 << (CSharpParser.INTERPOLATED_VERBATIUM_STRING_START - 65)) | (1 << (CSharpParser.OPEN_PARENS - 65)))) != 0) or ((((_la - 134)) & ~0x3f) == 0 and ((1 << (_la - 134)) & ((1 << (CSharpParser.PLUS - 134)) | (1 << (CSharpParser.MINUS - 134)) | (1 << (CSharpParser.STAR - 134)) | (1 << (CSharpParser.AMP - 134)) | (1 << (CSharpParser.CARET - 134)) | (1 << (CSharpParser.BANG - 134)) | (1 << (CSharpParser.TILDE - 134)) | (1 << (CSharpParser.OP_INC - 134)) | (1 << (CSharpParser.OP_DEC - 134)) | (1 << (CSharpParser.OP_RANGE - 134)))) != 0):
                    self.state = 1361
                    self.expression()


                self.state = 1364
                self.match(CSharpParser.SEMICOLON)
                pass

            elif la_ == 13:
                localctx = CSharpParser.ThrowStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 1365
                self.match(CSharpParser.THROW)
                self.state = 1367
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BASE) | (1 << CSharpParser.BOOL) | (1 << CSharpParser.BY) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.CHECKED) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DEFAULT) | (1 << CSharpParser.DELEGATE) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FALSE) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.INT) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.LONG) | (1 << CSharpParser.NAMEOF))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (CSharpParser.NEW - 65)) | (1 << (CSharpParser.NULL - 65)) | (1 << (CSharpParser.OBJECT - 65)) | (1 << (CSharpParser.ON - 65)) | (1 << (CSharpParser.ORDERBY - 65)) | (1 << (CSharpParser.PARTIAL - 65)) | (1 << (CSharpParser.REF - 65)) | (1 << (CSharpParser.REMOVE - 65)) | (1 << (CSharpParser.SBYTE - 65)) | (1 << (CSharpParser.SELECT - 65)) | (1 << (CSharpParser.SET - 65)) | (1 << (CSharpParser.SHORT - 65)) | (1 << (CSharpParser.SIZEOF - 65)) | (1 << (CSharpParser.STRING - 65)) | (1 << (CSharpParser.THIS - 65)) | (1 << (CSharpParser.TRUE - 65)) | (1 << (CSharpParser.TYPEOF - 65)) | (1 << (CSharpParser.UINT - 65)) | (1 << (CSharpParser.ULONG - 65)) | (1 << (CSharpParser.UNCHECKED - 65)) | (1 << (CSharpParser.UNMANAGED - 65)) | (1 << (CSharpParser.USHORT - 65)) | (1 << (CSharpParser.VAR - 65)) | (1 << (CSharpParser.WHEN - 65)) | (1 << (CSharpParser.WHERE - 65)) | (1 << (CSharpParser.YIELD - 65)) | (1 << (CSharpParser.IDENTIFIER - 65)) | (1 << (CSharpParser.LITERAL_ACCESS - 65)) | (1 << (CSharpParser.INTEGER_LITERAL - 65)) | (1 << (CSharpParser.HEX_INTEGER_LITERAL - 65)) | (1 << (CSharpParser.BIN_INTEGER_LITERAL - 65)) | (1 << (CSharpParser.REAL_LITERAL - 65)) | (1 << (CSharpParser.CHARACTER_LITERAL - 65)) | (1 << (CSharpParser.REGULAR_STRING - 65)) | (1 << (CSharpParser.VERBATIUM_STRING - 65)) | (1 << (CSharpParser.INTERPOLATED_REGULAR_STRING_START - 65)) | (1 << (CSharpParser.INTERPOLATED_VERBATIUM_STRING_START - 65)) | (1 << (CSharpParser.OPEN_PARENS - 65)))) != 0) or ((((_la - 134)) & ~0x3f) == 0 and ((1 << (_la - 134)) & ((1 << (CSharpParser.PLUS - 134)) | (1 << (CSharpParser.MINUS - 134)) | (1 << (CSharpParser.STAR - 134)) | (1 << (CSharpParser.AMP - 134)) | (1 << (CSharpParser.CARET - 134)) | (1 << (CSharpParser.BANG - 134)) | (1 << (CSharpParser.TILDE - 134)) | (1 << (CSharpParser.OP_INC - 134)) | (1 << (CSharpParser.OP_DEC - 134)) | (1 << (CSharpParser.OP_RANGE - 134)))) != 0):
                    self.state = 1366
                    self.expression()


                self.state = 1369
                self.match(CSharpParser.SEMICOLON)
                pass

            elif la_ == 14:
                localctx = CSharpParser.TryStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 1370
                self.match(CSharpParser.TRY)
                self.state = 1371
                self.block()
                self.state = 1377
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSharpParser.CATCH]:
                    self.state = 1372
                    self.catch_clauses()
                    self.state = 1374
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==CSharpParser.FINALLY:
                        self.state = 1373
                        self.finally_clause()


                    pass
                elif token in [CSharpParser.FINALLY]:
                    self.state = 1376
                    self.finally_clause()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 15:
                localctx = CSharpParser.CheckedStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 1379
                self.match(CSharpParser.CHECKED)
                self.state = 1380
                self.block()
                pass

            elif la_ == 16:
                localctx = CSharpParser.UncheckedStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 16)
                self.state = 1381
                self.match(CSharpParser.UNCHECKED)
                self.state = 1382
                self.block()
                pass

            elif la_ == 17:
                localctx = CSharpParser.LockStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 17)
                self.state = 1383
                self.match(CSharpParser.LOCK)
                self.state = 1384
                self.match(CSharpParser.OPEN_PARENS)
                self.state = 1385
                self.expression()
                self.state = 1386
                self.match(CSharpParser.CLOSE_PARENS)
                self.state = 1387
                self.embedded_statement()
                pass

            elif la_ == 18:
                localctx = CSharpParser.UsingStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 18)
                self.state = 1389
                self.match(CSharpParser.USING)
                self.state = 1390
                self.match(CSharpParser.OPEN_PARENS)
                self.state = 1391
                self.resource_acquisition()
                self.state = 1392
                self.match(CSharpParser.CLOSE_PARENS)
                self.state = 1393
                self.embedded_statement()
                pass

            elif la_ == 19:
                localctx = CSharpParser.YieldStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 19)
                self.state = 1395
                self.match(CSharpParser.YIELD)
                self.state = 1399
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSharpParser.RETURN]:
                    self.state = 1396
                    self.match(CSharpParser.RETURN)
                    self.state = 1397
                    self.expression()
                    pass
                elif token in [CSharpParser.BREAK]:
                    self.state = 1398
                    self.match(CSharpParser.BREAK)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 1401
                self.match(CSharpParser.SEMICOLON)
                pass

            elif la_ == 20:
                localctx = CSharpParser.UnsafeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 20)
                self.state = 1402
                self.match(CSharpParser.UNSAFE)
                self.state = 1403
                self.block()
                pass

            elif la_ == 21:
                localctx = CSharpParser.FixedStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 21)
                self.state = 1404
                self.match(CSharpParser.FIXED)
                self.state = 1405
                self.match(CSharpParser.OPEN_PARENS)
                self.state = 1406
                self.pointer_type()
                self.state = 1407
                self.fixed_pointer_declarators()
                self.state = 1408
                self.match(CSharpParser.CLOSE_PARENS)
                self.state = 1409
                self.embedded_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACE(self):
            return self.getToken(CSharpParser.OPEN_BRACE, 0)

        def CLOSE_BRACE(self):
            return self.getToken(CSharpParser.CLOSE_BRACE, 0)

        def statement_list(self):
            return self.getTypedRuleContext(CSharpParser.Statement_listContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = CSharpParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 170, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1413
            self.match(CSharpParser.OPEN_BRACE)
            self.state = 1415
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BASE) | (1 << CSharpParser.BOOL) | (1 << CSharpParser.BREAK) | (1 << CSharpParser.BY) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.CHECKED) | (1 << CSharpParser.CONST) | (1 << CSharpParser.CONTINUE) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DEFAULT) | (1 << CSharpParser.DELEGATE) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DO) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FALSE) | (1 << CSharpParser.FIXED) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.FOR) | (1 << CSharpParser.FOREACH) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GOTO) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.IF) | (1 << CSharpParser.INT) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.LOCK) | (1 << CSharpParser.LONG) | (1 << CSharpParser.NAMEOF))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (CSharpParser.NEW - 65)) | (1 << (CSharpParser.NULL - 65)) | (1 << (CSharpParser.OBJECT - 65)) | (1 << (CSharpParser.ON - 65)) | (1 << (CSharpParser.ORDERBY - 65)) | (1 << (CSharpParser.PARTIAL - 65)) | (1 << (CSharpParser.REF - 65)) | (1 << (CSharpParser.REMOVE - 65)) | (1 << (CSharpParser.RETURN - 65)) | (1 << (CSharpParser.SBYTE - 65)) | (1 << (CSharpParser.SELECT - 65)) | (1 << (CSharpParser.SET - 65)) | (1 << (CSharpParser.SHORT - 65)) | (1 << (CSharpParser.SIZEOF - 65)) | (1 << (CSharpParser.STATIC - 65)) | (1 << (CSharpParser.STRING - 65)) | (1 << (CSharpParser.SWITCH - 65)) | (1 << (CSharpParser.THIS - 65)) | (1 << (CSharpParser.THROW - 65)) | (1 << (CSharpParser.TRUE - 65)) | (1 << (CSharpParser.TRY - 65)) | (1 << (CSharpParser.TYPEOF - 65)) | (1 << (CSharpParser.UINT - 65)) | (1 << (CSharpParser.ULONG - 65)) | (1 << (CSharpParser.UNCHECKED - 65)) | (1 << (CSharpParser.UNMANAGED - 65)) | (1 << (CSharpParser.UNSAFE - 65)) | (1 << (CSharpParser.USHORT - 65)) | (1 << (CSharpParser.USING - 65)) | (1 << (CSharpParser.VAR - 65)) | (1 << (CSharpParser.VOID - 65)) | (1 << (CSharpParser.WHEN - 65)) | (1 << (CSharpParser.WHERE - 65)) | (1 << (CSharpParser.WHILE - 65)) | (1 << (CSharpParser.YIELD - 65)) | (1 << (CSharpParser.IDENTIFIER - 65)) | (1 << (CSharpParser.LITERAL_ACCESS - 65)) | (1 << (CSharpParser.INTEGER_LITERAL - 65)) | (1 << (CSharpParser.HEX_INTEGER_LITERAL - 65)) | (1 << (CSharpParser.BIN_INTEGER_LITERAL - 65)) | (1 << (CSharpParser.REAL_LITERAL - 65)) | (1 << (CSharpParser.CHARACTER_LITERAL - 65)) | (1 << (CSharpParser.REGULAR_STRING - 65)) | (1 << (CSharpParser.VERBATIUM_STRING - 65)) | (1 << (CSharpParser.INTERPOLATED_REGULAR_STRING_START - 65)) | (1 << (CSharpParser.INTERPOLATED_VERBATIUM_STRING_START - 65)) | (1 << (CSharpParser.OPEN_BRACE - 65)) | (1 << (CSharpParser.OPEN_PARENS - 65)))) != 0) or ((((_la - 133)) & ~0x3f) == 0 and ((1 << (_la - 133)) & ((1 << (CSharpParser.SEMICOLON - 133)) | (1 << (CSharpParser.PLUS - 133)) | (1 << (CSharpParser.MINUS - 133)) | (1 << (CSharpParser.STAR - 133)) | (1 << (CSharpParser.AMP - 133)) | (1 << (CSharpParser.CARET - 133)) | (1 << (CSharpParser.BANG - 133)) | (1 << (CSharpParser.TILDE - 133)) | (1 << (CSharpParser.OP_INC - 133)) | (1 << (CSharpParser.OP_DEC - 133)) | (1 << (CSharpParser.OP_RANGE - 133)))) != 0):
                self.state = 1414
                self.statement_list()


            self.state = 1417
            self.match(CSharpParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Local_variable_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def local_variable_type(self):
            return self.getTypedRuleContext(CSharpParser.Local_variable_typeContext,0)


        def local_variable_declarator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Local_variable_declaratorContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Local_variable_declaratorContext,i)


        def USING(self):
            return self.getToken(CSharpParser.USING, 0)

        def REF(self):
            return self.getToken(CSharpParser.REF, 0)

        def READONLY(self):
            return self.getToken(CSharpParser.READONLY, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def FIXED(self):
            return self.getToken(CSharpParser.FIXED, 0)

        def pointer_type(self):
            return self.getTypedRuleContext(CSharpParser.Pointer_typeContext,0)


        def fixed_pointer_declarators(self):
            return self.getTypedRuleContext(CSharpParser.Fixed_pointer_declaratorsContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_local_variable_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocal_variable_declaration" ):
                listener.enterLocal_variable_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocal_variable_declaration" ):
                listener.exitLocal_variable_declaration(self)




    def local_variable_declaration(self):

        localctx = CSharpParser.Local_variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 172, self.RULE_local_variable_declaration)
        self._la = 0 # Token type
        try:
            self.state = 1438
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.ADD, CSharpParser.ALIAS, CSharpParser.ARGLIST, CSharpParser.ASCENDING, CSharpParser.ASYNC, CSharpParser.AWAIT, CSharpParser.BOOL, CSharpParser.BY, CSharpParser.BYTE, CSharpParser.CHAR, CSharpParser.DECIMAL, CSharpParser.DESCENDING, CSharpParser.DOUBLE, CSharpParser.DYNAMIC, CSharpParser.EQUALS, CSharpParser.FLOAT, CSharpParser.FROM, CSharpParser.GET, CSharpParser.GROUP, CSharpParser.INT, CSharpParser.INTO, CSharpParser.JOIN, CSharpParser.LET, CSharpParser.LONG, CSharpParser.NAMEOF, CSharpParser.OBJECT, CSharpParser.ON, CSharpParser.ORDERBY, CSharpParser.PARTIAL, CSharpParser.REF, CSharpParser.REMOVE, CSharpParser.SBYTE, CSharpParser.SELECT, CSharpParser.SET, CSharpParser.SHORT, CSharpParser.STRING, CSharpParser.UINT, CSharpParser.ULONG, CSharpParser.UNMANAGED, CSharpParser.USHORT, CSharpParser.USING, CSharpParser.VAR, CSharpParser.VOID, CSharpParser.WHEN, CSharpParser.WHERE, CSharpParser.YIELD, CSharpParser.IDENTIFIER, CSharpParser.OPEN_PARENS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1423
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,144,self._ctx)
                if la_ == 1:
                    self.state = 1419
                    self.match(CSharpParser.USING)

                elif la_ == 2:
                    self.state = 1420
                    self.match(CSharpParser.REF)

                elif la_ == 3:
                    self.state = 1421
                    self.match(CSharpParser.REF)
                    self.state = 1422
                    self.match(CSharpParser.READONLY)


                self.state = 1425
                self.local_variable_type()
                self.state = 1426
                self.local_variable_declarator()
                self.state = 1431
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CSharpParser.COMMA:
                    self.state = 1427
                    self.match(CSharpParser.COMMA)
                    self.state = 1428
                    self.local_variable_declarator()
                    self.state = 1433
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [CSharpParser.FIXED]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1434
                self.match(CSharpParser.FIXED)
                self.state = 1435
                self.pointer_type()
                self.state = 1436
                self.fixed_pointer_declarators()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Local_variable_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(CSharpParser.VAR, 0)

        def type_(self):
            return self.getTypedRuleContext(CSharpParser.Type_Context,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_local_variable_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocal_variable_type" ):
                listener.enterLocal_variable_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocal_variable_type" ):
                listener.exitLocal_variable_type(self)




    def local_variable_type(self):

        localctx = CSharpParser.Local_variable_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 174, self.RULE_local_variable_type)
        try:
            self.state = 1442
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,147,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1440
                self.match(CSharpParser.VAR)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1441
                self.type_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Local_variable_declaratorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def ASSIGNMENT(self):
            return self.getToken(CSharpParser.ASSIGNMENT, 0)

        def local_variable_initializer(self):
            return self.getTypedRuleContext(CSharpParser.Local_variable_initializerContext,0)


        def REF(self):
            return self.getToken(CSharpParser.REF, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_local_variable_declarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocal_variable_declarator" ):
                listener.enterLocal_variable_declarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocal_variable_declarator" ):
                listener.exitLocal_variable_declarator(self)




    def local_variable_declarator(self):

        localctx = CSharpParser.Local_variable_declaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 176, self.RULE_local_variable_declarator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1444
            self.identifier()
            self.state = 1450
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.ASSIGNMENT:
                self.state = 1445
                self.match(CSharpParser.ASSIGNMENT)
                self.state = 1447
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,148,self._ctx)
                if la_ == 1:
                    self.state = 1446
                    self.match(CSharpParser.REF)


                self.state = 1449
                self.local_variable_initializer()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Local_variable_initializerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def array_initializer(self):
            return self.getTypedRuleContext(CSharpParser.Array_initializerContext,0)


        def stackalloc_initializer(self):
            return self.getTypedRuleContext(CSharpParser.Stackalloc_initializerContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_local_variable_initializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocal_variable_initializer" ):
                listener.enterLocal_variable_initializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocal_variable_initializer" ):
                listener.exitLocal_variable_initializer(self)




    def local_variable_initializer(self):

        localctx = CSharpParser.Local_variable_initializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 178, self.RULE_local_variable_initializer)
        try:
            self.state = 1455
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.ADD, CSharpParser.ALIAS, CSharpParser.ARGLIST, CSharpParser.ASCENDING, CSharpParser.ASYNC, CSharpParser.AWAIT, CSharpParser.BASE, CSharpParser.BOOL, CSharpParser.BY, CSharpParser.BYTE, CSharpParser.CHAR, CSharpParser.CHECKED, CSharpParser.DECIMAL, CSharpParser.DEFAULT, CSharpParser.DELEGATE, CSharpParser.DESCENDING, CSharpParser.DOUBLE, CSharpParser.DYNAMIC, CSharpParser.EQUALS, CSharpParser.FALSE, CSharpParser.FLOAT, CSharpParser.FROM, CSharpParser.GET, CSharpParser.GROUP, CSharpParser.INT, CSharpParser.INTO, CSharpParser.JOIN, CSharpParser.LET, CSharpParser.LONG, CSharpParser.NAMEOF, CSharpParser.NEW, CSharpParser.NULL, CSharpParser.OBJECT, CSharpParser.ON, CSharpParser.ORDERBY, CSharpParser.PARTIAL, CSharpParser.REF, CSharpParser.REMOVE, CSharpParser.SBYTE, CSharpParser.SELECT, CSharpParser.SET, CSharpParser.SHORT, CSharpParser.SIZEOF, CSharpParser.STRING, CSharpParser.THIS, CSharpParser.TRUE, CSharpParser.TYPEOF, CSharpParser.UINT, CSharpParser.ULONG, CSharpParser.UNCHECKED, CSharpParser.UNMANAGED, CSharpParser.USHORT, CSharpParser.VAR, CSharpParser.WHEN, CSharpParser.WHERE, CSharpParser.YIELD, CSharpParser.IDENTIFIER, CSharpParser.LITERAL_ACCESS, CSharpParser.INTEGER_LITERAL, CSharpParser.HEX_INTEGER_LITERAL, CSharpParser.BIN_INTEGER_LITERAL, CSharpParser.REAL_LITERAL, CSharpParser.CHARACTER_LITERAL, CSharpParser.REGULAR_STRING, CSharpParser.VERBATIUM_STRING, CSharpParser.INTERPOLATED_REGULAR_STRING_START, CSharpParser.INTERPOLATED_VERBATIUM_STRING_START, CSharpParser.OPEN_PARENS, CSharpParser.PLUS, CSharpParser.MINUS, CSharpParser.STAR, CSharpParser.AMP, CSharpParser.CARET, CSharpParser.BANG, CSharpParser.TILDE, CSharpParser.OP_INC, CSharpParser.OP_DEC, CSharpParser.OP_RANGE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1452
                self.expression()
                pass
            elif token in [CSharpParser.OPEN_BRACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1453
                self.array_initializer()
                pass
            elif token in [CSharpParser.STACKALLOC]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1454
                self.stackalloc_initializer()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Local_constant_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(CSharpParser.CONST, 0)

        def type_(self):
            return self.getTypedRuleContext(CSharpParser.Type_Context,0)


        def constant_declarators(self):
            return self.getTypedRuleContext(CSharpParser.Constant_declaratorsContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_local_constant_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocal_constant_declaration" ):
                listener.enterLocal_constant_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocal_constant_declaration" ):
                listener.exitLocal_constant_declaration(self)




    def local_constant_declaration(self):

        localctx = CSharpParser.Local_constant_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 180, self.RULE_local_constant_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1457
            self.match(CSharpParser.CONST)
            self.state = 1458
            self.type_()
            self.state = 1459
            self.constant_declarators()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(CSharpParser.BlockContext,0)


        def simple_embedded_statement(self):
            return self.getTypedRuleContext(CSharpParser.Simple_embedded_statementContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_if_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_body" ):
                listener.enterIf_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_body" ):
                listener.exitIf_body(self)




    def if_body(self):

        localctx = CSharpParser.If_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 182, self.RULE_if_body)
        try:
            self.state = 1463
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.OPEN_BRACE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1461
                self.block()
                pass
            elif token in [CSharpParser.ADD, CSharpParser.ALIAS, CSharpParser.ARGLIST, CSharpParser.ASCENDING, CSharpParser.ASYNC, CSharpParser.AWAIT, CSharpParser.BASE, CSharpParser.BOOL, CSharpParser.BREAK, CSharpParser.BY, CSharpParser.BYTE, CSharpParser.CHAR, CSharpParser.CHECKED, CSharpParser.CONTINUE, CSharpParser.DECIMAL, CSharpParser.DEFAULT, CSharpParser.DELEGATE, CSharpParser.DESCENDING, CSharpParser.DO, CSharpParser.DOUBLE, CSharpParser.DYNAMIC, CSharpParser.EQUALS, CSharpParser.FALSE, CSharpParser.FIXED, CSharpParser.FLOAT, CSharpParser.FOR, CSharpParser.FOREACH, CSharpParser.FROM, CSharpParser.GET, CSharpParser.GOTO, CSharpParser.GROUP, CSharpParser.IF, CSharpParser.INT, CSharpParser.INTO, CSharpParser.JOIN, CSharpParser.LET, CSharpParser.LOCK, CSharpParser.LONG, CSharpParser.NAMEOF, CSharpParser.NEW, CSharpParser.NULL, CSharpParser.OBJECT, CSharpParser.ON, CSharpParser.ORDERBY, CSharpParser.PARTIAL, CSharpParser.REF, CSharpParser.REMOVE, CSharpParser.RETURN, CSharpParser.SBYTE, CSharpParser.SELECT, CSharpParser.SET, CSharpParser.SHORT, CSharpParser.SIZEOF, CSharpParser.STRING, CSharpParser.SWITCH, CSharpParser.THIS, CSharpParser.THROW, CSharpParser.TRUE, CSharpParser.TRY, CSharpParser.TYPEOF, CSharpParser.UINT, CSharpParser.ULONG, CSharpParser.UNCHECKED, CSharpParser.UNMANAGED, CSharpParser.UNSAFE, CSharpParser.USHORT, CSharpParser.USING, CSharpParser.VAR, CSharpParser.WHEN, CSharpParser.WHERE, CSharpParser.WHILE, CSharpParser.YIELD, CSharpParser.IDENTIFIER, CSharpParser.LITERAL_ACCESS, CSharpParser.INTEGER_LITERAL, CSharpParser.HEX_INTEGER_LITERAL, CSharpParser.BIN_INTEGER_LITERAL, CSharpParser.REAL_LITERAL, CSharpParser.CHARACTER_LITERAL, CSharpParser.REGULAR_STRING, CSharpParser.VERBATIUM_STRING, CSharpParser.INTERPOLATED_REGULAR_STRING_START, CSharpParser.INTERPOLATED_VERBATIUM_STRING_START, CSharpParser.OPEN_PARENS, CSharpParser.SEMICOLON, CSharpParser.PLUS, CSharpParser.MINUS, CSharpParser.STAR, CSharpParser.AMP, CSharpParser.CARET, CSharpParser.BANG, CSharpParser.TILDE, CSharpParser.OP_INC, CSharpParser.OP_DEC, CSharpParser.OP_RANGE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1462
                self.simple_embedded_statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Switch_sectionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement_list(self):
            return self.getTypedRuleContext(CSharpParser.Statement_listContext,0)


        def switch_label(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Switch_labelContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Switch_labelContext,i)


        def getRuleIndex(self):
            return CSharpParser.RULE_switch_section

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitch_section" ):
                listener.enterSwitch_section(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitch_section" ):
                listener.exitSwitch_section(self)




    def switch_section(self):

        localctx = CSharpParser.Switch_sectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 184, self.RULE_switch_section)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1466 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 1465
                    self.switch_label()

                else:
                    raise NoViableAltException(self)
                self.state = 1468 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,152,self._ctx)

            self.state = 1470
            self.statement_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Switch_labelContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASE(self):
            return self.getToken(CSharpParser.CASE, 0)

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def COLON(self):
            return self.getToken(CSharpParser.COLON, 0)

        def case_guard(self):
            return self.getTypedRuleContext(CSharpParser.Case_guardContext,0)


        def DEFAULT(self):
            return self.getToken(CSharpParser.DEFAULT, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_switch_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitch_label" ):
                listener.enterSwitch_label(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitch_label" ):
                listener.exitSwitch_label(self)




    def switch_label(self):

        localctx = CSharpParser.Switch_labelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 186, self.RULE_switch_label)
        self._la = 0 # Token type
        try:
            self.state = 1481
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.CASE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1472
                self.match(CSharpParser.CASE)
                self.state = 1473
                self.expression()
                self.state = 1475
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.WHEN:
                    self.state = 1474
                    self.case_guard()


                self.state = 1477
                self.match(CSharpParser.COLON)
                pass
            elif token in [CSharpParser.DEFAULT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1479
                self.match(CSharpParser.DEFAULT)
                self.state = 1480
                self.match(CSharpParser.COLON)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Case_guardContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHEN(self):
            return self.getToken(CSharpParser.WHEN, 0)

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_case_guard

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCase_guard" ):
                listener.enterCase_guard(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCase_guard" ):
                listener.exitCase_guard(self)




    def case_guard(self):

        localctx = CSharpParser.Case_guardContext(self, self._ctx, self.state)
        self.enterRule(localctx, 188, self.RULE_case_guard)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1483
            self.match(CSharpParser.WHEN)
            self.state = 1484
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.StatementContext)
            else:
                return self.getTypedRuleContext(CSharpParser.StatementContext,i)


        def getRuleIndex(self):
            return CSharpParser.RULE_statement_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement_list" ):
                listener.enterStatement_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement_list" ):
                listener.exitStatement_list(self)




    def statement_list(self):

        localctx = CSharpParser.Statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 190, self.RULE_statement_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1487 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 1486
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 1489 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,155,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_initializerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def local_variable_declaration(self):
            return self.getTypedRuleContext(CSharpParser.Local_variable_declarationContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CSharpParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_for_initializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_initializer" ):
                listener.enterFor_initializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_initializer" ):
                listener.exitFor_initializer(self)




    def for_initializer(self):

        localctx = CSharpParser.For_initializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 192, self.RULE_for_initializer)
        self._la = 0 # Token type
        try:
            self.state = 1500
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,157,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1491
                self.local_variable_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1492
                self.expression()
                self.state = 1497
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CSharpParser.COMMA:
                    self.state = 1493
                    self.match(CSharpParser.COMMA)
                    self.state = 1494
                    self.expression()
                    self.state = 1499
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_iteratorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CSharpParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_for_iterator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_iterator" ):
                listener.enterFor_iterator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_iterator" ):
                listener.exitFor_iterator(self)




    def for_iterator(self):

        localctx = CSharpParser.For_iteratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 194, self.RULE_for_iterator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1502
            self.expression()
            self.state = 1507
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.COMMA:
                self.state = 1503
                self.match(CSharpParser.COMMA)
                self.state = 1504
                self.expression()
                self.state = 1509
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Catch_clausesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def specific_catch_clause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Specific_catch_clauseContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Specific_catch_clauseContext,i)


        def general_catch_clause(self):
            return self.getTypedRuleContext(CSharpParser.General_catch_clauseContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_catch_clauses

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCatch_clauses" ):
                listener.enterCatch_clauses(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCatch_clauses" ):
                listener.exitCatch_clauses(self)




    def catch_clauses(self):

        localctx = CSharpParser.Catch_clausesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 196, self.RULE_catch_clauses)
        self._la = 0 # Token type
        try:
            self.state = 1521
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,161,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1510
                self.specific_catch_clause()
                self.state = 1514
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,159,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 1511
                        self.specific_catch_clause() 
                    self.state = 1516
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,159,self._ctx)

                self.state = 1518
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.CATCH:
                    self.state = 1517
                    self.general_catch_clause()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1520
                self.general_catch_clause()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Specific_catch_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CATCH(self):
            return self.getToken(CSharpParser.CATCH, 0)

        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)

        def class_type(self):
            return self.getTypedRuleContext(CSharpParser.Class_typeContext,0)


        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)

        def block(self):
            return self.getTypedRuleContext(CSharpParser.BlockContext,0)


        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def exception_filter(self):
            return self.getTypedRuleContext(CSharpParser.Exception_filterContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_specific_catch_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpecific_catch_clause" ):
                listener.enterSpecific_catch_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpecific_catch_clause" ):
                listener.exitSpecific_catch_clause(self)




    def specific_catch_clause(self):

        localctx = CSharpParser.Specific_catch_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 198, self.RULE_specific_catch_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1523
            self.match(CSharpParser.CATCH)
            self.state = 1524
            self.match(CSharpParser.OPEN_PARENS)
            self.state = 1525
            self.class_type()
            self.state = 1527
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BY) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.NAMEOF))) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & ((1 << (CSharpParser.ON - 68)) | (1 << (CSharpParser.ORDERBY - 68)) | (1 << (CSharpParser.PARTIAL - 68)) | (1 << (CSharpParser.REMOVE - 68)) | (1 << (CSharpParser.SELECT - 68)) | (1 << (CSharpParser.SET - 68)) | (1 << (CSharpParser.UNMANAGED - 68)) | (1 << (CSharpParser.VAR - 68)) | (1 << (CSharpParser.WHEN - 68)) | (1 << (CSharpParser.WHERE - 68)) | (1 << (CSharpParser.YIELD - 68)) | (1 << (CSharpParser.IDENTIFIER - 68)))) != 0):
                self.state = 1526
                self.identifier()


            self.state = 1529
            self.match(CSharpParser.CLOSE_PARENS)
            self.state = 1531
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.WHEN:
                self.state = 1530
                self.exception_filter()


            self.state = 1533
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class General_catch_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CATCH(self):
            return self.getToken(CSharpParser.CATCH, 0)

        def block(self):
            return self.getTypedRuleContext(CSharpParser.BlockContext,0)


        def exception_filter(self):
            return self.getTypedRuleContext(CSharpParser.Exception_filterContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_general_catch_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGeneral_catch_clause" ):
                listener.enterGeneral_catch_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGeneral_catch_clause" ):
                listener.exitGeneral_catch_clause(self)




    def general_catch_clause(self):

        localctx = CSharpParser.General_catch_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 200, self.RULE_general_catch_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1535
            self.match(CSharpParser.CATCH)
            self.state = 1537
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.WHEN:
                self.state = 1536
                self.exception_filter()


            self.state = 1539
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exception_filterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHEN(self):
            return self.getToken(CSharpParser.WHEN, 0)

        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_exception_filter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterException_filter" ):
                listener.enterException_filter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitException_filter" ):
                listener.exitException_filter(self)




    def exception_filter(self):

        localctx = CSharpParser.Exception_filterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 202, self.RULE_exception_filter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1541
            self.match(CSharpParser.WHEN)
            self.state = 1542
            self.match(CSharpParser.OPEN_PARENS)
            self.state = 1543
            self.expression()
            self.state = 1544
            self.match(CSharpParser.CLOSE_PARENS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Finally_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FINALLY(self):
            return self.getToken(CSharpParser.FINALLY, 0)

        def block(self):
            return self.getTypedRuleContext(CSharpParser.BlockContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_finally_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFinally_clause" ):
                listener.enterFinally_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFinally_clause" ):
                listener.exitFinally_clause(self)




    def finally_clause(self):

        localctx = CSharpParser.Finally_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 204, self.RULE_finally_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1546
            self.match(CSharpParser.FINALLY)
            self.state = 1547
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Resource_acquisitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def local_variable_declaration(self):
            return self.getTypedRuleContext(CSharpParser.Local_variable_declarationContext,0)


        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_resource_acquisition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterResource_acquisition" ):
                listener.enterResource_acquisition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitResource_acquisition" ):
                listener.exitResource_acquisition(self)




    def resource_acquisition(self):

        localctx = CSharpParser.Resource_acquisitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 206, self.RULE_resource_acquisition)
        try:
            self.state = 1551
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,165,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1549
                self.local_variable_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1550
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Namespace_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.qi = None # Qualified_identifierContext

        def NAMESPACE(self):
            return self.getToken(CSharpParser.NAMESPACE, 0)

        def namespace_body(self):
            return self.getTypedRuleContext(CSharpParser.Namespace_bodyContext,0)


        def qualified_identifier(self):
            return self.getTypedRuleContext(CSharpParser.Qualified_identifierContext,0)


        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_namespace_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamespace_declaration" ):
                listener.enterNamespace_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamespace_declaration" ):
                listener.exitNamespace_declaration(self)




    def namespace_declaration(self):

        localctx = CSharpParser.Namespace_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 208, self.RULE_namespace_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1553
            self.match(CSharpParser.NAMESPACE)
            self.state = 1554
            localctx.qi = self.qualified_identifier()
            self.state = 1555
            self.namespace_body()
            self.state = 1557
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.SEMICOLON:
                self.state = 1556
                self.match(CSharpParser.SEMICOLON)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Qualified_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(CSharpParser.IdentifierContext,i)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.DOT)
            else:
                return self.getToken(CSharpParser.DOT, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_qualified_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQualified_identifier" ):
                listener.enterQualified_identifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQualified_identifier" ):
                listener.exitQualified_identifier(self)




    def qualified_identifier(self):

        localctx = CSharpParser.Qualified_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 210, self.RULE_qualified_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1559
            self.identifier()
            self.state = 1564
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.DOT:
                self.state = 1560
                self.match(CSharpParser.DOT)
                self.state = 1561
                self.identifier()
                self.state = 1566
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Namespace_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACE(self):
            return self.getToken(CSharpParser.OPEN_BRACE, 0)

        def CLOSE_BRACE(self):
            return self.getToken(CSharpParser.CLOSE_BRACE, 0)

        def extern_alias_directives(self):
            return self.getTypedRuleContext(CSharpParser.Extern_alias_directivesContext,0)


        def using_directives(self):
            return self.getTypedRuleContext(CSharpParser.Using_directivesContext,0)


        def namespace_member_declarations(self):
            return self.getTypedRuleContext(CSharpParser.Namespace_member_declarationsContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_namespace_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamespace_body" ):
                listener.enterNamespace_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamespace_body" ):
                listener.exitNamespace_body(self)




    def namespace_body(self):

        localctx = CSharpParser.Namespace_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 212, self.RULE_namespace_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1567
            self.match(CSharpParser.OPEN_BRACE)
            self.state = 1569
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,168,self._ctx)
            if la_ == 1:
                self.state = 1568
                self.extern_alias_directives()


            self.state = 1572
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.USING:
                self.state = 1571
                self.using_directives()


            self.state = 1575
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ABSTRACT) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.CLASS) | (1 << CSharpParser.DELEGATE) | (1 << CSharpParser.ENUM) | (1 << CSharpParser.EXTERN) | (1 << CSharpParser.INTERFACE) | (1 << CSharpParser.INTERNAL))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CSharpParser.NAMESPACE - 64)) | (1 << (CSharpParser.NEW - 64)) | (1 << (CSharpParser.OVERRIDE - 64)) | (1 << (CSharpParser.PARTIAL - 64)) | (1 << (CSharpParser.PRIVATE - 64)) | (1 << (CSharpParser.PROTECTED - 64)) | (1 << (CSharpParser.PUBLIC - 64)) | (1 << (CSharpParser.READONLY - 64)) | (1 << (CSharpParser.REF - 64)) | (1 << (CSharpParser.SEALED - 64)) | (1 << (CSharpParser.STATIC - 64)) | (1 << (CSharpParser.STRUCT - 64)) | (1 << (CSharpParser.UNSAFE - 64)) | (1 << (CSharpParser.VIRTUAL - 64)) | (1 << (CSharpParser.VOLATILE - 64)) | (1 << (CSharpParser.OPEN_BRACKET - 64)))) != 0):
                self.state = 1574
                self.namespace_member_declarations()


            self.state = 1577
            self.match(CSharpParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Extern_alias_directivesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def extern_alias_directive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Extern_alias_directiveContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Extern_alias_directiveContext,i)


        def getRuleIndex(self):
            return CSharpParser.RULE_extern_alias_directives

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExtern_alias_directives" ):
                listener.enterExtern_alias_directives(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExtern_alias_directives" ):
                listener.exitExtern_alias_directives(self)




    def extern_alias_directives(self):

        localctx = CSharpParser.Extern_alias_directivesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 214, self.RULE_extern_alias_directives)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1580 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 1579
                    self.extern_alias_directive()

                else:
                    raise NoViableAltException(self)
                self.state = 1582 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,171,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Extern_alias_directiveContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXTERN(self):
            return self.getToken(CSharpParser.EXTERN, 0)

        def ALIAS(self):
            return self.getToken(CSharpParser.ALIAS, 0)

        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_extern_alias_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExtern_alias_directive" ):
                listener.enterExtern_alias_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExtern_alias_directive" ):
                listener.exitExtern_alias_directive(self)




    def extern_alias_directive(self):

        localctx = CSharpParser.Extern_alias_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 216, self.RULE_extern_alias_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1584
            self.match(CSharpParser.EXTERN)
            self.state = 1585
            self.match(CSharpParser.ALIAS)
            self.state = 1586
            self.identifier()
            self.state = 1587
            self.match(CSharpParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Using_directivesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def using_directive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Using_directiveContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Using_directiveContext,i)


        def getRuleIndex(self):
            return CSharpParser.RULE_using_directives

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUsing_directives" ):
                listener.enterUsing_directives(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUsing_directives" ):
                listener.exitUsing_directives(self)




    def using_directives(self):

        localctx = CSharpParser.Using_directivesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 218, self.RULE_using_directives)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1590 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1589
                self.using_directive()
                self.state = 1592 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CSharpParser.USING):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Using_directiveContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CSharpParser.RULE_using_directive

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class UsingAliasDirectiveContext(Using_directiveContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Using_directiveContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def USING(self):
            return self.getToken(CSharpParser.USING, 0)
        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)

        def ASSIGNMENT(self):
            return self.getToken(CSharpParser.ASSIGNMENT, 0)
        def namespace_or_type_name(self):
            return self.getTypedRuleContext(CSharpParser.Namespace_or_type_nameContext,0)

        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUsingAliasDirective" ):
                listener.enterUsingAliasDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUsingAliasDirective" ):
                listener.exitUsingAliasDirective(self)


    class UsingNamespaceDirectiveContext(Using_directiveContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Using_directiveContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def USING(self):
            return self.getToken(CSharpParser.USING, 0)
        def namespace_or_type_name(self):
            return self.getTypedRuleContext(CSharpParser.Namespace_or_type_nameContext,0)

        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUsingNamespaceDirective" ):
                listener.enterUsingNamespaceDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUsingNamespaceDirective" ):
                listener.exitUsingNamespaceDirective(self)


    class UsingStaticDirectiveContext(Using_directiveContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpParser.Using_directiveContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def USING(self):
            return self.getToken(CSharpParser.USING, 0)
        def STATIC(self):
            return self.getToken(CSharpParser.STATIC, 0)
        def namespace_or_type_name(self):
            return self.getTypedRuleContext(CSharpParser.Namespace_or_type_nameContext,0)

        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUsingStaticDirective" ):
                listener.enterUsingStaticDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUsingStaticDirective" ):
                listener.exitUsingStaticDirective(self)



    def using_directive(self):

        localctx = CSharpParser.Using_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 220, self.RULE_using_directive)
        try:
            self.state = 1609
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,173,self._ctx)
            if la_ == 1:
                localctx = CSharpParser.UsingAliasDirectiveContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1594
                self.match(CSharpParser.USING)
                self.state = 1595
                self.identifier()
                self.state = 1596
                self.match(CSharpParser.ASSIGNMENT)
                self.state = 1597
                self.namespace_or_type_name()
                self.state = 1598
                self.match(CSharpParser.SEMICOLON)
                pass

            elif la_ == 2:
                localctx = CSharpParser.UsingNamespaceDirectiveContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1600
                self.match(CSharpParser.USING)
                self.state = 1601
                self.namespace_or_type_name()
                self.state = 1602
                self.match(CSharpParser.SEMICOLON)
                pass

            elif la_ == 3:
                localctx = CSharpParser.UsingStaticDirectiveContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1604
                self.match(CSharpParser.USING)
                self.state = 1605
                self.match(CSharpParser.STATIC)
                self.state = 1606
                self.namespace_or_type_name()
                self.state = 1607
                self.match(CSharpParser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Namespace_member_declarationsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def namespace_member_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Namespace_member_declarationContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Namespace_member_declarationContext,i)


        def getRuleIndex(self):
            return CSharpParser.RULE_namespace_member_declarations

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamespace_member_declarations" ):
                listener.enterNamespace_member_declarations(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamespace_member_declarations" ):
                listener.exitNamespace_member_declarations(self)




    def namespace_member_declarations(self):

        localctx = CSharpParser.Namespace_member_declarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 222, self.RULE_namespace_member_declarations)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1612 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1611
                self.namespace_member_declaration()
                self.state = 1614 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ABSTRACT) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.CLASS) | (1 << CSharpParser.DELEGATE) | (1 << CSharpParser.ENUM) | (1 << CSharpParser.EXTERN) | (1 << CSharpParser.INTERFACE) | (1 << CSharpParser.INTERNAL))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CSharpParser.NAMESPACE - 64)) | (1 << (CSharpParser.NEW - 64)) | (1 << (CSharpParser.OVERRIDE - 64)) | (1 << (CSharpParser.PARTIAL - 64)) | (1 << (CSharpParser.PRIVATE - 64)) | (1 << (CSharpParser.PROTECTED - 64)) | (1 << (CSharpParser.PUBLIC - 64)) | (1 << (CSharpParser.READONLY - 64)) | (1 << (CSharpParser.REF - 64)) | (1 << (CSharpParser.SEALED - 64)) | (1 << (CSharpParser.STATIC - 64)) | (1 << (CSharpParser.STRUCT - 64)) | (1 << (CSharpParser.UNSAFE - 64)) | (1 << (CSharpParser.VIRTUAL - 64)) | (1 << (CSharpParser.VOLATILE - 64)) | (1 << (CSharpParser.OPEN_BRACKET - 64)))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Namespace_member_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def namespace_declaration(self):
            return self.getTypedRuleContext(CSharpParser.Namespace_declarationContext,0)


        def type_declaration(self):
            return self.getTypedRuleContext(CSharpParser.Type_declarationContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_namespace_member_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamespace_member_declaration" ):
                listener.enterNamespace_member_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamespace_member_declaration" ):
                listener.exitNamespace_member_declaration(self)




    def namespace_member_declaration(self):

        localctx = CSharpParser.Namespace_member_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 224, self.RULE_namespace_member_declaration)
        try:
            self.state = 1618
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.NAMESPACE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1616
                self.namespace_declaration()
                pass
            elif token in [CSharpParser.ABSTRACT, CSharpParser.ASYNC, CSharpParser.CLASS, CSharpParser.DELEGATE, CSharpParser.ENUM, CSharpParser.EXTERN, CSharpParser.INTERFACE, CSharpParser.INTERNAL, CSharpParser.NEW, CSharpParser.OVERRIDE, CSharpParser.PARTIAL, CSharpParser.PRIVATE, CSharpParser.PROTECTED, CSharpParser.PUBLIC, CSharpParser.READONLY, CSharpParser.REF, CSharpParser.SEALED, CSharpParser.STATIC, CSharpParser.STRUCT, CSharpParser.UNSAFE, CSharpParser.VIRTUAL, CSharpParser.VOLATILE, CSharpParser.OPEN_BRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1617
                self.type_declaration()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_definition(self):
            return self.getTypedRuleContext(CSharpParser.Class_definitionContext,0)


        def struct_definition(self):
            return self.getTypedRuleContext(CSharpParser.Struct_definitionContext,0)


        def interface_definition(self):
            return self.getTypedRuleContext(CSharpParser.Interface_definitionContext,0)


        def enum_definition(self):
            return self.getTypedRuleContext(CSharpParser.Enum_definitionContext,0)


        def delegate_definition(self):
            return self.getTypedRuleContext(CSharpParser.Delegate_definitionContext,0)


        def attributes(self):
            return self.getTypedRuleContext(CSharpParser.AttributesContext,0)


        def all_member_modifiers(self):
            return self.getTypedRuleContext(CSharpParser.All_member_modifiersContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_type_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_declaration" ):
                listener.enterType_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_declaration" ):
                listener.exitType_declaration(self)




    def type_declaration(self):

        localctx = CSharpParser.Type_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 226, self.RULE_type_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1621
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.OPEN_BRACKET:
                self.state = 1620
                self.attributes()


            self.state = 1624
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,177,self._ctx)
            if la_ == 1:
                self.state = 1623
                self.all_member_modifiers()


            self.state = 1631
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.CLASS]:
                self.state = 1626
                self.class_definition()
                pass
            elif token in [CSharpParser.READONLY, CSharpParser.REF, CSharpParser.STRUCT]:
                self.state = 1627
                self.struct_definition()
                pass
            elif token in [CSharpParser.INTERFACE]:
                self.state = 1628
                self.interface_definition()
                pass
            elif token in [CSharpParser.ENUM]:
                self.state = 1629
                self.enum_definition()
                pass
            elif token in [CSharpParser.DELEGATE]:
                self.state = 1630
                self.delegate_definition()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Qualified_alias_memberContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(CSharpParser.IdentifierContext,i)


        def DOUBLE_COLON(self):
            return self.getToken(CSharpParser.DOUBLE_COLON, 0)

        def type_argument_list(self):
            return self.getTypedRuleContext(CSharpParser.Type_argument_listContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_qualified_alias_member

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQualified_alias_member" ):
                listener.enterQualified_alias_member(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQualified_alias_member" ):
                listener.exitQualified_alias_member(self)




    def qualified_alias_member(self):

        localctx = CSharpParser.Qualified_alias_memberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 228, self.RULE_qualified_alias_member)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1633
            self.identifier()
            self.state = 1634
            self.match(CSharpParser.DOUBLE_COLON)
            self.state = 1635
            self.identifier()
            self.state = 1637
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,179,self._ctx)
            if la_ == 1:
                self.state = 1636
                self.type_argument_list()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_parameter_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(CSharpParser.LT, 0)

        def type_parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Type_parameterContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Type_parameterContext,i)


        def GT(self):
            return self.getToken(CSharpParser.GT, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_type_parameter_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_parameter_list" ):
                listener.enterType_parameter_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_parameter_list" ):
                listener.exitType_parameter_list(self)




    def type_parameter_list(self):

        localctx = CSharpParser.Type_parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 230, self.RULE_type_parameter_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1639
            self.match(CSharpParser.LT)
            self.state = 1640
            self.type_parameter()
            self.state = 1645
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.COMMA:
                self.state = 1641
                self.match(CSharpParser.COMMA)
                self.state = 1642
                self.type_parameter()
                self.state = 1647
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1648
            self.match(CSharpParser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_parameterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def attributes(self):
            return self.getTypedRuleContext(CSharpParser.AttributesContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_type_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_parameter" ):
                listener.enterType_parameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_parameter" ):
                listener.exitType_parameter(self)




    def type_parameter(self):

        localctx = CSharpParser.Type_parameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 232, self.RULE_type_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1651
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.OPEN_BRACKET:
                self.state = 1650
                self.attributes()


            self.state = 1653
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_baseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(CSharpParser.COLON, 0)

        def class_type(self):
            return self.getTypedRuleContext(CSharpParser.Class_typeContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def namespace_or_type_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Namespace_or_type_nameContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Namespace_or_type_nameContext,i)


        def getRuleIndex(self):
            return CSharpParser.RULE_class_base

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_base" ):
                listener.enterClass_base(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_base" ):
                listener.exitClass_base(self)




    def class_base(self):

        localctx = CSharpParser.Class_baseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 234, self.RULE_class_base)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1655
            self.match(CSharpParser.COLON)
            self.state = 1656
            self.class_type()
            self.state = 1661
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.COMMA:
                self.state = 1657
                self.match(CSharpParser.COMMA)
                self.state = 1658
                self.namespace_or_type_name()
                self.state = 1663
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_type_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def namespace_or_type_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Namespace_or_type_nameContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Namespace_or_type_nameContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_interface_type_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterface_type_list" ):
                listener.enterInterface_type_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterface_type_list" ):
                listener.exitInterface_type_list(self)




    def interface_type_list(self):

        localctx = CSharpParser.Interface_type_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 236, self.RULE_interface_type_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1664
            self.namespace_or_type_name()
            self.state = 1669
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.COMMA:
                self.state = 1665
                self.match(CSharpParser.COMMA)
                self.state = 1666
                self.namespace_or_type_name()
                self.state = 1671
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_parameter_constraints_clausesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_parameter_constraints_clause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Type_parameter_constraints_clauseContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Type_parameter_constraints_clauseContext,i)


        def getRuleIndex(self):
            return CSharpParser.RULE_type_parameter_constraints_clauses

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_parameter_constraints_clauses" ):
                listener.enterType_parameter_constraints_clauses(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_parameter_constraints_clauses" ):
                listener.exitType_parameter_constraints_clauses(self)




    def type_parameter_constraints_clauses(self):

        localctx = CSharpParser.Type_parameter_constraints_clausesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 238, self.RULE_type_parameter_constraints_clauses)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1673 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1672
                self.type_parameter_constraints_clause()
                self.state = 1675 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CSharpParser.WHERE):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_parameter_constraints_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHERE(self):
            return self.getToken(CSharpParser.WHERE, 0)

        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def COLON(self):
            return self.getToken(CSharpParser.COLON, 0)

        def type_parameter_constraints(self):
            return self.getTypedRuleContext(CSharpParser.Type_parameter_constraintsContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_type_parameter_constraints_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_parameter_constraints_clause" ):
                listener.enterType_parameter_constraints_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_parameter_constraints_clause" ):
                listener.exitType_parameter_constraints_clause(self)




    def type_parameter_constraints_clause(self):

        localctx = CSharpParser.Type_parameter_constraints_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 240, self.RULE_type_parameter_constraints_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1677
            self.match(CSharpParser.WHERE)
            self.state = 1678
            self.identifier()
            self.state = 1679
            self.match(CSharpParser.COLON)
            self.state = 1680
            self.type_parameter_constraints()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_parameter_constraintsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constructor_constraint(self):
            return self.getTypedRuleContext(CSharpParser.Constructor_constraintContext,0)


        def primary_constraint(self):
            return self.getTypedRuleContext(CSharpParser.Primary_constraintContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def secondary_constraints(self):
            return self.getTypedRuleContext(CSharpParser.Secondary_constraintsContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_type_parameter_constraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_parameter_constraints" ):
                listener.enterType_parameter_constraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_parameter_constraints" ):
                listener.exitType_parameter_constraints(self)




    def type_parameter_constraints(self):

        localctx = CSharpParser.Type_parameter_constraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 242, self.RULE_type_parameter_constraints)
        self._la = 0 # Token type
        try:
            self.state = 1692
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1682
                self.constructor_constraint()
                pass
            elif token in [CSharpParser.ADD, CSharpParser.ALIAS, CSharpParser.ARGLIST, CSharpParser.ASCENDING, CSharpParser.ASYNC, CSharpParser.AWAIT, CSharpParser.BY, CSharpParser.CLASS, CSharpParser.DESCENDING, CSharpParser.DYNAMIC, CSharpParser.EQUALS, CSharpParser.FROM, CSharpParser.GET, CSharpParser.GROUP, CSharpParser.INTO, CSharpParser.JOIN, CSharpParser.LET, CSharpParser.NAMEOF, CSharpParser.OBJECT, CSharpParser.ON, CSharpParser.ORDERBY, CSharpParser.PARTIAL, CSharpParser.REMOVE, CSharpParser.SELECT, CSharpParser.SET, CSharpParser.STRING, CSharpParser.STRUCT, CSharpParser.UNMANAGED, CSharpParser.VAR, CSharpParser.WHEN, CSharpParser.WHERE, CSharpParser.YIELD, CSharpParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1683
                self.primary_constraint()
                self.state = 1686
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,185,self._ctx)
                if la_ == 1:
                    self.state = 1684
                    self.match(CSharpParser.COMMA)
                    self.state = 1685
                    self.secondary_constraints()


                self.state = 1690
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.COMMA:
                    self.state = 1688
                    self.match(CSharpParser.COMMA)
                    self.state = 1689
                    self.constructor_constraint()


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primary_constraintContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_type(self):
            return self.getTypedRuleContext(CSharpParser.Class_typeContext,0)


        def CLASS(self):
            return self.getToken(CSharpParser.CLASS, 0)

        def INTERR(self):
            return self.getToken(CSharpParser.INTERR, 0)

        def STRUCT(self):
            return self.getToken(CSharpParser.STRUCT, 0)

        def UNMANAGED(self):
            return self.getToken(CSharpParser.UNMANAGED, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_primary_constraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary_constraint" ):
                listener.enterPrimary_constraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary_constraint" ):
                listener.exitPrimary_constraint(self)




    def primary_constraint(self):

        localctx = CSharpParser.Primary_constraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 244, self.RULE_primary_constraint)
        self._la = 0 # Token type
        try:
            self.state = 1701
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,189,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1694
                self.class_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1695
                self.match(CSharpParser.CLASS)
                self.state = 1697
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.INTERR:
                    self.state = 1696
                    self.match(CSharpParser.INTERR)


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1699
                self.match(CSharpParser.STRUCT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1700
                self.match(CSharpParser.UNMANAGED)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Secondary_constraintsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def namespace_or_type_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Namespace_or_type_nameContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Namespace_or_type_nameContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_secondary_constraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSecondary_constraints" ):
                listener.enterSecondary_constraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSecondary_constraints" ):
                listener.exitSecondary_constraints(self)




    def secondary_constraints(self):

        localctx = CSharpParser.Secondary_constraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 246, self.RULE_secondary_constraints)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1703
            self.namespace_or_type_name()
            self.state = 1708
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,190,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1704
                    self.match(CSharpParser.COMMA)
                    self.state = 1705
                    self.namespace_or_type_name() 
                self.state = 1710
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,190,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constructor_constraintContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(CSharpParser.NEW, 0)

        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_constructor_constraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstructor_constraint" ):
                listener.enterConstructor_constraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstructor_constraint" ):
                listener.exitConstructor_constraint(self)




    def constructor_constraint(self):

        localctx = CSharpParser.Constructor_constraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 248, self.RULE_constructor_constraint)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1711
            self.match(CSharpParser.NEW)
            self.state = 1712
            self.match(CSharpParser.OPEN_PARENS)
            self.state = 1713
            self.match(CSharpParser.CLOSE_PARENS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACE(self):
            return self.getToken(CSharpParser.OPEN_BRACE, 0)

        def CLOSE_BRACE(self):
            return self.getToken(CSharpParser.CLOSE_BRACE, 0)

        def class_member_declarations(self):
            return self.getTypedRuleContext(CSharpParser.Class_member_declarationsContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_class_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_body" ):
                listener.enterClass_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_body" ):
                listener.exitClass_body(self)




    def class_body(self):

        localctx = CSharpParser.Class_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 250, self.RULE_class_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1715
            self.match(CSharpParser.OPEN_BRACE)
            self.state = 1717
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ABSTRACT) | (1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BOOL) | (1 << CSharpParser.BY) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.CLASS) | (1 << CSharpParser.CONST) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DELEGATE) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.ENUM) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.EVENT) | (1 << CSharpParser.EXPLICIT) | (1 << CSharpParser.EXTERN) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.IMPLICIT) | (1 << CSharpParser.INT) | (1 << CSharpParser.INTERFACE) | (1 << CSharpParser.INTERNAL) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.LONG) | (1 << CSharpParser.NAMEOF))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (CSharpParser.NEW - 65)) | (1 << (CSharpParser.OBJECT - 65)) | (1 << (CSharpParser.ON - 65)) | (1 << (CSharpParser.ORDERBY - 65)) | (1 << (CSharpParser.OVERRIDE - 65)) | (1 << (CSharpParser.PARTIAL - 65)) | (1 << (CSharpParser.PRIVATE - 65)) | (1 << (CSharpParser.PROTECTED - 65)) | (1 << (CSharpParser.PUBLIC - 65)) | (1 << (CSharpParser.READONLY - 65)) | (1 << (CSharpParser.REF - 65)) | (1 << (CSharpParser.REMOVE - 65)) | (1 << (CSharpParser.SBYTE - 65)) | (1 << (CSharpParser.SEALED - 65)) | (1 << (CSharpParser.SELECT - 65)) | (1 << (CSharpParser.SET - 65)) | (1 << (CSharpParser.SHORT - 65)) | (1 << (CSharpParser.STATIC - 65)) | (1 << (CSharpParser.STRING - 65)) | (1 << (CSharpParser.STRUCT - 65)) | (1 << (CSharpParser.UINT - 65)) | (1 << (CSharpParser.ULONG - 65)) | (1 << (CSharpParser.UNMANAGED - 65)) | (1 << (CSharpParser.UNSAFE - 65)) | (1 << (CSharpParser.USHORT - 65)) | (1 << (CSharpParser.VAR - 65)) | (1 << (CSharpParser.VIRTUAL - 65)) | (1 << (CSharpParser.VOID - 65)) | (1 << (CSharpParser.VOLATILE - 65)) | (1 << (CSharpParser.WHEN - 65)) | (1 << (CSharpParser.WHERE - 65)) | (1 << (CSharpParser.YIELD - 65)) | (1 << (CSharpParser.IDENTIFIER - 65)) | (1 << (CSharpParser.OPEN_BRACKET - 65)) | (1 << (CSharpParser.OPEN_PARENS - 65)))) != 0) or _la==CSharpParser.TILDE:
                self.state = 1716
                self.class_member_declarations()


            self.state = 1719
            self.match(CSharpParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_member_declarationsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_member_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Class_member_declarationContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Class_member_declarationContext,i)


        def getRuleIndex(self):
            return CSharpParser.RULE_class_member_declarations

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_member_declarations" ):
                listener.enterClass_member_declarations(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_member_declarations" ):
                listener.exitClass_member_declarations(self)




    def class_member_declarations(self):

        localctx = CSharpParser.Class_member_declarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 252, self.RULE_class_member_declarations)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1722 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1721
                self.class_member_declaration()
                self.state = 1724 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ABSTRACT) | (1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BOOL) | (1 << CSharpParser.BY) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.CLASS) | (1 << CSharpParser.CONST) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DELEGATE) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.ENUM) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.EVENT) | (1 << CSharpParser.EXPLICIT) | (1 << CSharpParser.EXTERN) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.IMPLICIT) | (1 << CSharpParser.INT) | (1 << CSharpParser.INTERFACE) | (1 << CSharpParser.INTERNAL) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.LONG) | (1 << CSharpParser.NAMEOF))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (CSharpParser.NEW - 65)) | (1 << (CSharpParser.OBJECT - 65)) | (1 << (CSharpParser.ON - 65)) | (1 << (CSharpParser.ORDERBY - 65)) | (1 << (CSharpParser.OVERRIDE - 65)) | (1 << (CSharpParser.PARTIAL - 65)) | (1 << (CSharpParser.PRIVATE - 65)) | (1 << (CSharpParser.PROTECTED - 65)) | (1 << (CSharpParser.PUBLIC - 65)) | (1 << (CSharpParser.READONLY - 65)) | (1 << (CSharpParser.REF - 65)) | (1 << (CSharpParser.REMOVE - 65)) | (1 << (CSharpParser.SBYTE - 65)) | (1 << (CSharpParser.SEALED - 65)) | (1 << (CSharpParser.SELECT - 65)) | (1 << (CSharpParser.SET - 65)) | (1 << (CSharpParser.SHORT - 65)) | (1 << (CSharpParser.STATIC - 65)) | (1 << (CSharpParser.STRING - 65)) | (1 << (CSharpParser.STRUCT - 65)) | (1 << (CSharpParser.UINT - 65)) | (1 << (CSharpParser.ULONG - 65)) | (1 << (CSharpParser.UNMANAGED - 65)) | (1 << (CSharpParser.UNSAFE - 65)) | (1 << (CSharpParser.USHORT - 65)) | (1 << (CSharpParser.VAR - 65)) | (1 << (CSharpParser.VIRTUAL - 65)) | (1 << (CSharpParser.VOID - 65)) | (1 << (CSharpParser.VOLATILE - 65)) | (1 << (CSharpParser.WHEN - 65)) | (1 << (CSharpParser.WHERE - 65)) | (1 << (CSharpParser.YIELD - 65)) | (1 << (CSharpParser.IDENTIFIER - 65)) | (1 << (CSharpParser.OPEN_BRACKET - 65)) | (1 << (CSharpParser.OPEN_PARENS - 65)))) != 0) or _la==CSharpParser.TILDE):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_member_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def common_member_declaration(self):
            return self.getTypedRuleContext(CSharpParser.Common_member_declarationContext,0)


        def destructor_definition(self):
            return self.getTypedRuleContext(CSharpParser.Destructor_definitionContext,0)


        def attributes(self):
            return self.getTypedRuleContext(CSharpParser.AttributesContext,0)


        def all_member_modifiers(self):
            return self.getTypedRuleContext(CSharpParser.All_member_modifiersContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_class_member_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_member_declaration" ):
                listener.enterClass_member_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_member_declaration" ):
                listener.exitClass_member_declaration(self)




    def class_member_declaration(self):

        localctx = CSharpParser.Class_member_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 254, self.RULE_class_member_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1727
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.OPEN_BRACKET:
                self.state = 1726
                self.attributes()


            self.state = 1730
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,194,self._ctx)
            if la_ == 1:
                self.state = 1729
                self.all_member_modifiers()


            self.state = 1734
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.ADD, CSharpParser.ALIAS, CSharpParser.ARGLIST, CSharpParser.ASCENDING, CSharpParser.ASYNC, CSharpParser.AWAIT, CSharpParser.BOOL, CSharpParser.BY, CSharpParser.BYTE, CSharpParser.CHAR, CSharpParser.CLASS, CSharpParser.CONST, CSharpParser.DECIMAL, CSharpParser.DELEGATE, CSharpParser.DESCENDING, CSharpParser.DOUBLE, CSharpParser.DYNAMIC, CSharpParser.ENUM, CSharpParser.EQUALS, CSharpParser.EVENT, CSharpParser.EXPLICIT, CSharpParser.FLOAT, CSharpParser.FROM, CSharpParser.GET, CSharpParser.GROUP, CSharpParser.IMPLICIT, CSharpParser.INT, CSharpParser.INTERFACE, CSharpParser.INTO, CSharpParser.JOIN, CSharpParser.LET, CSharpParser.LONG, CSharpParser.NAMEOF, CSharpParser.OBJECT, CSharpParser.ON, CSharpParser.ORDERBY, CSharpParser.PARTIAL, CSharpParser.READONLY, CSharpParser.REF, CSharpParser.REMOVE, CSharpParser.SBYTE, CSharpParser.SELECT, CSharpParser.SET, CSharpParser.SHORT, CSharpParser.STRING, CSharpParser.STRUCT, CSharpParser.UINT, CSharpParser.ULONG, CSharpParser.UNMANAGED, CSharpParser.USHORT, CSharpParser.VAR, CSharpParser.VOID, CSharpParser.WHEN, CSharpParser.WHERE, CSharpParser.YIELD, CSharpParser.IDENTIFIER, CSharpParser.OPEN_PARENS]:
                self.state = 1732
                self.common_member_declaration()
                pass
            elif token in [CSharpParser.TILDE]:
                self.state = 1733
                self.destructor_definition()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class All_member_modifiersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def all_member_modifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.All_member_modifierContext)
            else:
                return self.getTypedRuleContext(CSharpParser.All_member_modifierContext,i)


        def getRuleIndex(self):
            return CSharpParser.RULE_all_member_modifiers

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAll_member_modifiers" ):
                listener.enterAll_member_modifiers(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAll_member_modifiers" ):
                listener.exitAll_member_modifiers(self)




    def all_member_modifiers(self):

        localctx = CSharpParser.All_member_modifiersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 256, self.RULE_all_member_modifiers)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1737 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 1736
                    self.all_member_modifier()

                else:
                    raise NoViableAltException(self)
                self.state = 1739 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,196,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class All_member_modifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(CSharpParser.NEW, 0)

        def PUBLIC(self):
            return self.getToken(CSharpParser.PUBLIC, 0)

        def PROTECTED(self):
            return self.getToken(CSharpParser.PROTECTED, 0)

        def INTERNAL(self):
            return self.getToken(CSharpParser.INTERNAL, 0)

        def PRIVATE(self):
            return self.getToken(CSharpParser.PRIVATE, 0)

        def READONLY(self):
            return self.getToken(CSharpParser.READONLY, 0)

        def VOLATILE(self):
            return self.getToken(CSharpParser.VOLATILE, 0)

        def VIRTUAL(self):
            return self.getToken(CSharpParser.VIRTUAL, 0)

        def SEALED(self):
            return self.getToken(CSharpParser.SEALED, 0)

        def OVERRIDE(self):
            return self.getToken(CSharpParser.OVERRIDE, 0)

        def ABSTRACT(self):
            return self.getToken(CSharpParser.ABSTRACT, 0)

        def STATIC(self):
            return self.getToken(CSharpParser.STATIC, 0)

        def UNSAFE(self):
            return self.getToken(CSharpParser.UNSAFE, 0)

        def EXTERN(self):
            return self.getToken(CSharpParser.EXTERN, 0)

        def PARTIAL(self):
            return self.getToken(CSharpParser.PARTIAL, 0)

        def ASYNC(self):
            return self.getToken(CSharpParser.ASYNC, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_all_member_modifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAll_member_modifier" ):
                listener.enterAll_member_modifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAll_member_modifier" ):
                listener.exitAll_member_modifier(self)




    def all_member_modifier(self):

        localctx = CSharpParser.All_member_modifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 258, self.RULE_all_member_modifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1741
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ABSTRACT) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.EXTERN) | (1 << CSharpParser.INTERNAL))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (CSharpParser.NEW - 65)) | (1 << (CSharpParser.OVERRIDE - 65)) | (1 << (CSharpParser.PARTIAL - 65)) | (1 << (CSharpParser.PRIVATE - 65)) | (1 << (CSharpParser.PROTECTED - 65)) | (1 << (CSharpParser.PUBLIC - 65)) | (1 << (CSharpParser.READONLY - 65)) | (1 << (CSharpParser.SEALED - 65)) | (1 << (CSharpParser.STATIC - 65)) | (1 << (CSharpParser.UNSAFE - 65)) | (1 << (CSharpParser.VIRTUAL - 65)) | (1 << (CSharpParser.VOLATILE - 65)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Common_member_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constant_declaration(self):
            return self.getTypedRuleContext(CSharpParser.Constant_declarationContext,0)


        def typed_member_declaration(self):
            return self.getTypedRuleContext(CSharpParser.Typed_member_declarationContext,0)


        def event_declaration(self):
            return self.getTypedRuleContext(CSharpParser.Event_declarationContext,0)


        def conversion_operator_declarator(self):
            return self.getTypedRuleContext(CSharpParser.Conversion_operator_declaratorContext,0)


        def body(self):
            return self.getTypedRuleContext(CSharpParser.BodyContext,0)


        def right_arrow(self):
            return self.getTypedRuleContext(CSharpParser.Right_arrowContext,0)


        def throwable_expression(self):
            return self.getTypedRuleContext(CSharpParser.Throwable_expressionContext,0)


        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def constructor_declaration(self):
            return self.getTypedRuleContext(CSharpParser.Constructor_declarationContext,0)


        def VOID(self):
            return self.getToken(CSharpParser.VOID, 0)

        def method_declaration(self):
            return self.getTypedRuleContext(CSharpParser.Method_declarationContext,0)


        def class_definition(self):
            return self.getTypedRuleContext(CSharpParser.Class_definitionContext,0)


        def struct_definition(self):
            return self.getTypedRuleContext(CSharpParser.Struct_definitionContext,0)


        def interface_definition(self):
            return self.getTypedRuleContext(CSharpParser.Interface_definitionContext,0)


        def enum_definition(self):
            return self.getTypedRuleContext(CSharpParser.Enum_definitionContext,0)


        def delegate_definition(self):
            return self.getTypedRuleContext(CSharpParser.Delegate_definitionContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_common_member_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommon_member_declaration" ):
                listener.enterCommon_member_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommon_member_declaration" ):
                listener.exitCommon_member_declaration(self)




    def common_member_declaration(self):

        localctx = CSharpParser.Common_member_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 260, self.RULE_common_member_declaration)
        try:
            self.state = 1762
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,198,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1743
                self.constant_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1744
                self.typed_member_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1745
                self.event_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1746
                self.conversion_operator_declarator()
                self.state = 1752
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSharpParser.OPEN_BRACE, CSharpParser.SEMICOLON]:
                    self.state = 1747
                    self.body()
                    pass
                elif token in [CSharpParser.ASSIGNMENT]:
                    self.state = 1748
                    self.right_arrow()
                    self.state = 1749
                    self.throwable_expression()
                    self.state = 1750
                    self.match(CSharpParser.SEMICOLON)
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1754
                self.constructor_declaration()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 1755
                self.match(CSharpParser.VOID)
                self.state = 1756
                self.method_declaration()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 1757
                self.class_definition()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 1758
                self.struct_definition()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 1759
                self.interface_definition()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 1760
                self.enum_definition()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 1761
                self.delegate_definition()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Typed_member_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(CSharpParser.Type_Context,0)


        def namespace_or_type_name(self):
            return self.getTypedRuleContext(CSharpParser.Namespace_or_type_nameContext,0)


        def DOT(self):
            return self.getToken(CSharpParser.DOT, 0)

        def indexer_declaration(self):
            return self.getTypedRuleContext(CSharpParser.Indexer_declarationContext,0)


        def method_declaration(self):
            return self.getTypedRuleContext(CSharpParser.Method_declarationContext,0)


        def property_declaration(self):
            return self.getTypedRuleContext(CSharpParser.Property_declarationContext,0)


        def operator_declaration(self):
            return self.getTypedRuleContext(CSharpParser.Operator_declarationContext,0)


        def field_declaration(self):
            return self.getTypedRuleContext(CSharpParser.Field_declarationContext,0)


        def REF(self):
            return self.getToken(CSharpParser.REF, 0)

        def READONLY(self):
            return self.getToken(CSharpParser.READONLY, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_typed_member_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTyped_member_declaration" ):
                listener.enterTyped_member_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTyped_member_declaration" ):
                listener.exitTyped_member_declaration(self)




    def typed_member_declaration(self):

        localctx = CSharpParser.Typed_member_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 262, self.RULE_typed_member_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1769
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,199,self._ctx)
            if la_ == 1:
                self.state = 1764
                self.match(CSharpParser.REF)

            elif la_ == 2:
                self.state = 1765
                self.match(CSharpParser.READONLY)
                self.state = 1766
                self.match(CSharpParser.REF)

            elif la_ == 3:
                self.state = 1767
                self.match(CSharpParser.REF)
                self.state = 1768
                self.match(CSharpParser.READONLY)


            self.state = 1771
            self.type_()
            self.state = 1781
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,200,self._ctx)
            if la_ == 1:
                self.state = 1772
                self.namespace_or_type_name()
                self.state = 1773
                self.match(CSharpParser.DOT)
                self.state = 1774
                self.indexer_declaration()
                pass

            elif la_ == 2:
                self.state = 1776
                self.method_declaration()
                pass

            elif la_ == 3:
                self.state = 1777
                self.property_declaration()
                pass

            elif la_ == 4:
                self.state = 1778
                self.indexer_declaration()
                pass

            elif la_ == 5:
                self.state = 1779
                self.operator_declaration()
                pass

            elif la_ == 6:
                self.state = 1780
                self.field_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constant_declaratorsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constant_declarator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Constant_declaratorContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Constant_declaratorContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_constant_declarators

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant_declarators" ):
                listener.enterConstant_declarators(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant_declarators" ):
                listener.exitConstant_declarators(self)




    def constant_declarators(self):

        localctx = CSharpParser.Constant_declaratorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 264, self.RULE_constant_declarators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1783
            self.constant_declarator()
            self.state = 1788
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.COMMA:
                self.state = 1784
                self.match(CSharpParser.COMMA)
                self.state = 1785
                self.constant_declarator()
                self.state = 1790
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constant_declaratorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def ASSIGNMENT(self):
            return self.getToken(CSharpParser.ASSIGNMENT, 0)

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_constant_declarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant_declarator" ):
                listener.enterConstant_declarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant_declarator" ):
                listener.exitConstant_declarator(self)




    def constant_declarator(self):

        localctx = CSharpParser.Constant_declaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 266, self.RULE_constant_declarator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1791
            self.identifier()
            self.state = 1792
            self.match(CSharpParser.ASSIGNMENT)
            self.state = 1793
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declaratorsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_declarator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Variable_declaratorContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Variable_declaratorContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_variable_declarators

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_declarators" ):
                listener.enterVariable_declarators(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_declarators" ):
                listener.exitVariable_declarators(self)




    def variable_declarators(self):

        localctx = CSharpParser.Variable_declaratorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 268, self.RULE_variable_declarators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1795
            self.variable_declarator()
            self.state = 1800
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.COMMA:
                self.state = 1796
                self.match(CSharpParser.COMMA)
                self.state = 1797
                self.variable_declarator()
                self.state = 1802
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declaratorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def ASSIGNMENT(self):
            return self.getToken(CSharpParser.ASSIGNMENT, 0)

        def variable_initializer(self):
            return self.getTypedRuleContext(CSharpParser.Variable_initializerContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_variable_declarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_declarator" ):
                listener.enterVariable_declarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_declarator" ):
                listener.exitVariable_declarator(self)




    def variable_declarator(self):

        localctx = CSharpParser.Variable_declaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 270, self.RULE_variable_declarator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1803
            self.identifier()
            self.state = 1806
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.ASSIGNMENT:
                self.state = 1804
                self.match(CSharpParser.ASSIGNMENT)
                self.state = 1805
                self.variable_initializer()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_initializerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def array_initializer(self):
            return self.getTypedRuleContext(CSharpParser.Array_initializerContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_variable_initializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_initializer" ):
                listener.enterVariable_initializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_initializer" ):
                listener.exitVariable_initializer(self)




    def variable_initializer(self):

        localctx = CSharpParser.Variable_initializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 272, self.RULE_variable_initializer)
        try:
            self.state = 1810
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.ADD, CSharpParser.ALIAS, CSharpParser.ARGLIST, CSharpParser.ASCENDING, CSharpParser.ASYNC, CSharpParser.AWAIT, CSharpParser.BASE, CSharpParser.BOOL, CSharpParser.BY, CSharpParser.BYTE, CSharpParser.CHAR, CSharpParser.CHECKED, CSharpParser.DECIMAL, CSharpParser.DEFAULT, CSharpParser.DELEGATE, CSharpParser.DESCENDING, CSharpParser.DOUBLE, CSharpParser.DYNAMIC, CSharpParser.EQUALS, CSharpParser.FALSE, CSharpParser.FLOAT, CSharpParser.FROM, CSharpParser.GET, CSharpParser.GROUP, CSharpParser.INT, CSharpParser.INTO, CSharpParser.JOIN, CSharpParser.LET, CSharpParser.LONG, CSharpParser.NAMEOF, CSharpParser.NEW, CSharpParser.NULL, CSharpParser.OBJECT, CSharpParser.ON, CSharpParser.ORDERBY, CSharpParser.PARTIAL, CSharpParser.REF, CSharpParser.REMOVE, CSharpParser.SBYTE, CSharpParser.SELECT, CSharpParser.SET, CSharpParser.SHORT, CSharpParser.SIZEOF, CSharpParser.STRING, CSharpParser.THIS, CSharpParser.TRUE, CSharpParser.TYPEOF, CSharpParser.UINT, CSharpParser.ULONG, CSharpParser.UNCHECKED, CSharpParser.UNMANAGED, CSharpParser.USHORT, CSharpParser.VAR, CSharpParser.WHEN, CSharpParser.WHERE, CSharpParser.YIELD, CSharpParser.IDENTIFIER, CSharpParser.LITERAL_ACCESS, CSharpParser.INTEGER_LITERAL, CSharpParser.HEX_INTEGER_LITERAL, CSharpParser.BIN_INTEGER_LITERAL, CSharpParser.REAL_LITERAL, CSharpParser.CHARACTER_LITERAL, CSharpParser.REGULAR_STRING, CSharpParser.VERBATIUM_STRING, CSharpParser.INTERPOLATED_REGULAR_STRING_START, CSharpParser.INTERPOLATED_VERBATIUM_STRING_START, CSharpParser.OPEN_PARENS, CSharpParser.PLUS, CSharpParser.MINUS, CSharpParser.STAR, CSharpParser.AMP, CSharpParser.CARET, CSharpParser.BANG, CSharpParser.TILDE, CSharpParser.OP_INC, CSharpParser.OP_DEC, CSharpParser.OP_RANGE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1808
                self.expression()
                pass
            elif token in [CSharpParser.OPEN_BRACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1809
                self.array_initializer()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(CSharpParser.Type_Context,0)


        def VOID(self):
            return self.getToken(CSharpParser.VOID, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_return_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_type" ):
                listener.enterReturn_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_type" ):
                listener.exitReturn_type(self)




    def return_type(self):

        localctx = CSharpParser.Return_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 274, self.RULE_return_type)
        try:
            self.state = 1814
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,205,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1812
                self.type_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1813
                self.match(CSharpParser.VOID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Member_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def namespace_or_type_name(self):
            return self.getTypedRuleContext(CSharpParser.Namespace_or_type_nameContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_member_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMember_name" ):
                listener.enterMember_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMember_name" ):
                listener.exitMember_name(self)




    def member_name(self):

        localctx = CSharpParser.Member_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 276, self.RULE_member_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1816
            self.namespace_or_type_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(CSharpParser.BlockContext,0)


        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_method_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod_body" ):
                listener.enterMethod_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod_body" ):
                listener.exitMethod_body(self)




    def method_body(self):

        localctx = CSharpParser.Method_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 278, self.RULE_method_body)
        try:
            self.state = 1820
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.OPEN_BRACE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1818
                self.block()
                pass
            elif token in [CSharpParser.SEMICOLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1819
                self.match(CSharpParser.SEMICOLON)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Formal_parameter_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter_array(self):
            return self.getTypedRuleContext(CSharpParser.Parameter_arrayContext,0)


        def fixed_parameters(self):
            return self.getTypedRuleContext(CSharpParser.Fixed_parametersContext,0)


        def COMMA(self):
            return self.getToken(CSharpParser.COMMA, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_formal_parameter_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormal_parameter_list" ):
                listener.enterFormal_parameter_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormal_parameter_list" ):
                listener.exitFormal_parameter_list(self)




    def formal_parameter_list(self):

        localctx = CSharpParser.Formal_parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 280, self.RULE_formal_parameter_list)
        self._la = 0 # Token type
        try:
            self.state = 1828
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,208,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1822
                self.parameter_array()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1823
                self.fixed_parameters()
                self.state = 1826
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.COMMA:
                    self.state = 1824
                    self.match(CSharpParser.COMMA)
                    self.state = 1825
                    self.parameter_array()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fixed_parametersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fixed_parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Fixed_parameterContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Fixed_parameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_fixed_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFixed_parameters" ):
                listener.enterFixed_parameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFixed_parameters" ):
                listener.exitFixed_parameters(self)




    def fixed_parameters(self):

        localctx = CSharpParser.Fixed_parametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 282, self.RULE_fixed_parameters)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1830
            self.fixed_parameter()
            self.state = 1835
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,209,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1831
                    self.match(CSharpParser.COMMA)
                    self.state = 1832
                    self.fixed_parameter() 
                self.state = 1837
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,209,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fixed_parameterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arg_declaration(self):
            return self.getTypedRuleContext(CSharpParser.Arg_declarationContext,0)


        def attributes(self):
            return self.getTypedRuleContext(CSharpParser.AttributesContext,0)


        def parameter_modifier(self):
            return self.getTypedRuleContext(CSharpParser.Parameter_modifierContext,0)


        def ARGLIST(self):
            return self.getToken(CSharpParser.ARGLIST, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_fixed_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFixed_parameter" ):
                listener.enterFixed_parameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFixed_parameter" ):
                listener.exitFixed_parameter(self)




    def fixed_parameter(self):

        localctx = CSharpParser.Fixed_parameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 284, self.RULE_fixed_parameter)
        self._la = 0 # Token type
        try:
            self.state = 1846
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,212,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1839
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.OPEN_BRACKET:
                    self.state = 1838
                    self.attributes()


                self.state = 1842
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 53)) & ~0x3f) == 0 and ((1 << (_la - 53)) & ((1 << (CSharpParser.IN - 53)) | (1 << (CSharpParser.OUT - 53)) | (1 << (CSharpParser.REF - 53)) | (1 << (CSharpParser.THIS - 53)))) != 0):
                    self.state = 1841
                    self.parameter_modifier()


                self.state = 1844
                self.arg_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1845
                self.match(CSharpParser.ARGLIST)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_modifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REF(self):
            return self.getToken(CSharpParser.REF, 0)

        def OUT(self):
            return self.getToken(CSharpParser.OUT, 0)

        def IN(self):
            return self.getToken(CSharpParser.IN, 0)

        def THIS(self):
            return self.getToken(CSharpParser.THIS, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_parameter_modifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter_modifier" ):
                listener.enterParameter_modifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter_modifier" ):
                listener.exitParameter_modifier(self)




    def parameter_modifier(self):

        localctx = CSharpParser.Parameter_modifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 286, self.RULE_parameter_modifier)
        try:
            self.state = 1856
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,213,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1848
                self.match(CSharpParser.REF)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1849
                self.match(CSharpParser.OUT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1850
                self.match(CSharpParser.IN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1851
                self.match(CSharpParser.REF)
                self.state = 1852
                self.match(CSharpParser.THIS)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1853
                self.match(CSharpParser.IN)
                self.state = 1854
                self.match(CSharpParser.THIS)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 1855
                self.match(CSharpParser.THIS)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_arrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARAMS(self):
            return self.getToken(CSharpParser.PARAMS, 0)

        def array_type(self):
            return self.getTypedRuleContext(CSharpParser.Array_typeContext,0)


        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def attributes(self):
            return self.getTypedRuleContext(CSharpParser.AttributesContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_parameter_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter_array" ):
                listener.enterParameter_array(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter_array" ):
                listener.exitParameter_array(self)




    def parameter_array(self):

        localctx = CSharpParser.Parameter_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 288, self.RULE_parameter_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1859
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.OPEN_BRACKET:
                self.state = 1858
                self.attributes()


            self.state = 1861
            self.match(CSharpParser.PARAMS)
            self.state = 1862
            self.array_type()
            self.state = 1863
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Accessor_declarationsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.attrs = None # AttributesContext
            self.mods = None # Accessor_modifierContext

        def GET(self):
            return self.getToken(CSharpParser.GET, 0)

        def accessor_body(self):
            return self.getTypedRuleContext(CSharpParser.Accessor_bodyContext,0)


        def SET(self):
            return self.getToken(CSharpParser.SET, 0)

        def attributes(self):
            return self.getTypedRuleContext(CSharpParser.AttributesContext,0)


        def accessor_modifier(self):
            return self.getTypedRuleContext(CSharpParser.Accessor_modifierContext,0)


        def set_accessor_declaration(self):
            return self.getTypedRuleContext(CSharpParser.Set_accessor_declarationContext,0)


        def get_accessor_declaration(self):
            return self.getTypedRuleContext(CSharpParser.Get_accessor_declarationContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_accessor_declarations

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAccessor_declarations" ):
                listener.enterAccessor_declarations(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAccessor_declarations" ):
                listener.exitAccessor_declarations(self)




    def accessor_declarations(self):

        localctx = CSharpParser.Accessor_declarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 290, self.RULE_accessor_declarations)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1866
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.OPEN_BRACKET:
                self.state = 1865
                localctx.attrs = self.attributes()


            self.state = 1869
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 56)) & ~0x3f) == 0 and ((1 << (_la - 56)) & ((1 << (CSharpParser.INTERNAL - 56)) | (1 << (CSharpParser.PRIVATE - 56)) | (1 << (CSharpParser.PROTECTED - 56)))) != 0):
                self.state = 1868
                localctx.mods = self.accessor_modifier()


            self.state = 1881
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.GET]:
                self.state = 1871
                self.match(CSharpParser.GET)
                self.state = 1872
                self.accessor_body()
                self.state = 1874
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.INTERNAL or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (CSharpParser.PRIVATE - 75)) | (1 << (CSharpParser.PROTECTED - 75)) | (1 << (CSharpParser.SET - 75)) | (1 << (CSharpParser.OPEN_BRACKET - 75)))) != 0):
                    self.state = 1873
                    self.set_accessor_declaration()


                pass
            elif token in [CSharpParser.SET]:
                self.state = 1876
                self.match(CSharpParser.SET)
                self.state = 1877
                self.accessor_body()
                self.state = 1879
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.GET or _la==CSharpParser.INTERNAL or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (CSharpParser.PRIVATE - 75)) | (1 << (CSharpParser.PROTECTED - 75)) | (1 << (CSharpParser.OPEN_BRACKET - 75)))) != 0):
                    self.state = 1878
                    self.get_accessor_declaration()


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Get_accessor_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GET(self):
            return self.getToken(CSharpParser.GET, 0)

        def accessor_body(self):
            return self.getTypedRuleContext(CSharpParser.Accessor_bodyContext,0)


        def attributes(self):
            return self.getTypedRuleContext(CSharpParser.AttributesContext,0)


        def accessor_modifier(self):
            return self.getTypedRuleContext(CSharpParser.Accessor_modifierContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_get_accessor_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGet_accessor_declaration" ):
                listener.enterGet_accessor_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGet_accessor_declaration" ):
                listener.exitGet_accessor_declaration(self)




    def get_accessor_declaration(self):

        localctx = CSharpParser.Get_accessor_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 292, self.RULE_get_accessor_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1884
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.OPEN_BRACKET:
                self.state = 1883
                self.attributes()


            self.state = 1887
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 56)) & ~0x3f) == 0 and ((1 << (_la - 56)) & ((1 << (CSharpParser.INTERNAL - 56)) | (1 << (CSharpParser.PRIVATE - 56)) | (1 << (CSharpParser.PROTECTED - 56)))) != 0):
                self.state = 1886
                self.accessor_modifier()


            self.state = 1889
            self.match(CSharpParser.GET)
            self.state = 1890
            self.accessor_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Set_accessor_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SET(self):
            return self.getToken(CSharpParser.SET, 0)

        def accessor_body(self):
            return self.getTypedRuleContext(CSharpParser.Accessor_bodyContext,0)


        def attributes(self):
            return self.getTypedRuleContext(CSharpParser.AttributesContext,0)


        def accessor_modifier(self):
            return self.getTypedRuleContext(CSharpParser.Accessor_modifierContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_set_accessor_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSet_accessor_declaration" ):
                listener.enterSet_accessor_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSet_accessor_declaration" ):
                listener.exitSet_accessor_declaration(self)




    def set_accessor_declaration(self):

        localctx = CSharpParser.Set_accessor_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 294, self.RULE_set_accessor_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1893
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.OPEN_BRACKET:
                self.state = 1892
                self.attributes()


            self.state = 1896
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 56)) & ~0x3f) == 0 and ((1 << (_la - 56)) & ((1 << (CSharpParser.INTERNAL - 56)) | (1 << (CSharpParser.PRIVATE - 56)) | (1 << (CSharpParser.PROTECTED - 56)))) != 0):
                self.state = 1895
                self.accessor_modifier()


            self.state = 1898
            self.match(CSharpParser.SET)
            self.state = 1899
            self.accessor_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Accessor_modifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROTECTED(self):
            return self.getToken(CSharpParser.PROTECTED, 0)

        def INTERNAL(self):
            return self.getToken(CSharpParser.INTERNAL, 0)

        def PRIVATE(self):
            return self.getToken(CSharpParser.PRIVATE, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_accessor_modifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAccessor_modifier" ):
                listener.enterAccessor_modifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAccessor_modifier" ):
                listener.exitAccessor_modifier(self)




    def accessor_modifier(self):

        localctx = CSharpParser.Accessor_modifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 296, self.RULE_accessor_modifier)
        try:
            self.state = 1908
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,224,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1901
                self.match(CSharpParser.PROTECTED)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1902
                self.match(CSharpParser.INTERNAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1903
                self.match(CSharpParser.PRIVATE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1904
                self.match(CSharpParser.PROTECTED)
                self.state = 1905
                self.match(CSharpParser.INTERNAL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1906
                self.match(CSharpParser.INTERNAL)
                self.state = 1907
                self.match(CSharpParser.PROTECTED)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Accessor_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(CSharpParser.BlockContext,0)


        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_accessor_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAccessor_body" ):
                listener.enterAccessor_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAccessor_body" ):
                listener.exitAccessor_body(self)




    def accessor_body(self):

        localctx = CSharpParser.Accessor_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 298, self.RULE_accessor_body)
        try:
            self.state = 1912
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.OPEN_BRACE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1910
                self.block()
                pass
            elif token in [CSharpParser.SEMICOLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1911
                self.match(CSharpParser.SEMICOLON)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Event_accessor_declarationsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(CSharpParser.ADD, 0)

        def block(self):
            return self.getTypedRuleContext(CSharpParser.BlockContext,0)


        def remove_accessor_declaration(self):
            return self.getTypedRuleContext(CSharpParser.Remove_accessor_declarationContext,0)


        def REMOVE(self):
            return self.getToken(CSharpParser.REMOVE, 0)

        def add_accessor_declaration(self):
            return self.getTypedRuleContext(CSharpParser.Add_accessor_declarationContext,0)


        def attributes(self):
            return self.getTypedRuleContext(CSharpParser.AttributesContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_event_accessor_declarations

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEvent_accessor_declarations" ):
                listener.enterEvent_accessor_declarations(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEvent_accessor_declarations" ):
                listener.exitEvent_accessor_declarations(self)




    def event_accessor_declarations(self):

        localctx = CSharpParser.Event_accessor_declarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 300, self.RULE_event_accessor_declarations)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1915
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.OPEN_BRACKET:
                self.state = 1914
                self.attributes()


            self.state = 1925
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.ADD]:
                self.state = 1917
                self.match(CSharpParser.ADD)
                self.state = 1918
                self.block()
                self.state = 1919
                self.remove_accessor_declaration()
                pass
            elif token in [CSharpParser.REMOVE]:
                self.state = 1921
                self.match(CSharpParser.REMOVE)
                self.state = 1922
                self.block()
                self.state = 1923
                self.add_accessor_declaration()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Add_accessor_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(CSharpParser.ADD, 0)

        def block(self):
            return self.getTypedRuleContext(CSharpParser.BlockContext,0)


        def attributes(self):
            return self.getTypedRuleContext(CSharpParser.AttributesContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_add_accessor_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd_accessor_declaration" ):
                listener.enterAdd_accessor_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd_accessor_declaration" ):
                listener.exitAdd_accessor_declaration(self)




    def add_accessor_declaration(self):

        localctx = CSharpParser.Add_accessor_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 302, self.RULE_add_accessor_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1928
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.OPEN_BRACKET:
                self.state = 1927
                self.attributes()


            self.state = 1930
            self.match(CSharpParser.ADD)
            self.state = 1931
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Remove_accessor_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REMOVE(self):
            return self.getToken(CSharpParser.REMOVE, 0)

        def block(self):
            return self.getTypedRuleContext(CSharpParser.BlockContext,0)


        def attributes(self):
            return self.getTypedRuleContext(CSharpParser.AttributesContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_remove_accessor_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRemove_accessor_declaration" ):
                listener.enterRemove_accessor_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRemove_accessor_declaration" ):
                listener.exitRemove_accessor_declaration(self)




    def remove_accessor_declaration(self):

        localctx = CSharpParser.Remove_accessor_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 304, self.RULE_remove_accessor_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1934
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.OPEN_BRACKET:
                self.state = 1933
                self.attributes()


            self.state = 1936
            self.match(CSharpParser.REMOVE)
            self.state = 1937
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Overloadable_operatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(CSharpParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(CSharpParser.MINUS, 0)

        def BANG(self):
            return self.getToken(CSharpParser.BANG, 0)

        def TILDE(self):
            return self.getToken(CSharpParser.TILDE, 0)

        def OP_INC(self):
            return self.getToken(CSharpParser.OP_INC, 0)

        def OP_DEC(self):
            return self.getToken(CSharpParser.OP_DEC, 0)

        def TRUE(self):
            return self.getToken(CSharpParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(CSharpParser.FALSE, 0)

        def STAR(self):
            return self.getToken(CSharpParser.STAR, 0)

        def DIV(self):
            return self.getToken(CSharpParser.DIV, 0)

        def PERCENT(self):
            return self.getToken(CSharpParser.PERCENT, 0)

        def AMP(self):
            return self.getToken(CSharpParser.AMP, 0)

        def BITWISE_OR(self):
            return self.getToken(CSharpParser.BITWISE_OR, 0)

        def CARET(self):
            return self.getToken(CSharpParser.CARET, 0)

        def OP_LEFT_SHIFT(self):
            return self.getToken(CSharpParser.OP_LEFT_SHIFT, 0)

        def right_shift(self):
            return self.getTypedRuleContext(CSharpParser.Right_shiftContext,0)


        def OP_EQ(self):
            return self.getToken(CSharpParser.OP_EQ, 0)

        def OP_NE(self):
            return self.getToken(CSharpParser.OP_NE, 0)

        def GT(self):
            return self.getToken(CSharpParser.GT, 0)

        def LT(self):
            return self.getToken(CSharpParser.LT, 0)

        def OP_GE(self):
            return self.getToken(CSharpParser.OP_GE, 0)

        def OP_LE(self):
            return self.getToken(CSharpParser.OP_LE, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_overloadable_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOverloadable_operator" ):
                listener.enterOverloadable_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOverloadable_operator" ):
                listener.exitOverloadable_operator(self)




    def overloadable_operator(self):

        localctx = CSharpParser.Overloadable_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 306, self.RULE_overloadable_operator)
        try:
            self.state = 1961
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,230,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1939
                self.match(CSharpParser.PLUS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1940
                self.match(CSharpParser.MINUS)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1941
                self.match(CSharpParser.BANG)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1942
                self.match(CSharpParser.TILDE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1943
                self.match(CSharpParser.OP_INC)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 1944
                self.match(CSharpParser.OP_DEC)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 1945
                self.match(CSharpParser.TRUE)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 1946
                self.match(CSharpParser.FALSE)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 1947
                self.match(CSharpParser.STAR)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 1948
                self.match(CSharpParser.DIV)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 1949
                self.match(CSharpParser.PERCENT)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 1950
                self.match(CSharpParser.AMP)
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 1951
                self.match(CSharpParser.BITWISE_OR)
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 1952
                self.match(CSharpParser.CARET)
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 1953
                self.match(CSharpParser.OP_LEFT_SHIFT)
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 1954
                self.right_shift()
                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 1955
                self.match(CSharpParser.OP_EQ)
                pass

            elif la_ == 18:
                self.enterOuterAlt(localctx, 18)
                self.state = 1956
                self.match(CSharpParser.OP_NE)
                pass

            elif la_ == 19:
                self.enterOuterAlt(localctx, 19)
                self.state = 1957
                self.match(CSharpParser.GT)
                pass

            elif la_ == 20:
                self.enterOuterAlt(localctx, 20)
                self.state = 1958
                self.match(CSharpParser.LT)
                pass

            elif la_ == 21:
                self.enterOuterAlt(localctx, 21)
                self.state = 1959
                self.match(CSharpParser.OP_GE)
                pass

            elif la_ == 22:
                self.enterOuterAlt(localctx, 22)
                self.state = 1960
                self.match(CSharpParser.OP_LE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Conversion_operator_declaratorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPERATOR(self):
            return self.getToken(CSharpParser.OPERATOR, 0)

        def type_(self):
            return self.getTypedRuleContext(CSharpParser.Type_Context,0)


        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)

        def arg_declaration(self):
            return self.getTypedRuleContext(CSharpParser.Arg_declarationContext,0)


        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)

        def IMPLICIT(self):
            return self.getToken(CSharpParser.IMPLICIT, 0)

        def EXPLICIT(self):
            return self.getToken(CSharpParser.EXPLICIT, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_conversion_operator_declarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConversion_operator_declarator" ):
                listener.enterConversion_operator_declarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConversion_operator_declarator" ):
                listener.exitConversion_operator_declarator(self)




    def conversion_operator_declarator(self):

        localctx = CSharpParser.Conversion_operator_declaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 308, self.RULE_conversion_operator_declarator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1963
            _la = self._input.LA(1)
            if not(_la==CSharpParser.EXPLICIT or _la==CSharpParser.IMPLICIT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 1964
            self.match(CSharpParser.OPERATOR)
            self.state = 1965
            self.type_()
            self.state = 1966
            self.match(CSharpParser.OPEN_PARENS)
            self.state = 1967
            self.arg_declaration()
            self.state = 1968
            self.match(CSharpParser.CLOSE_PARENS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constructor_initializerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(CSharpParser.COLON, 0)

        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)

        def BASE(self):
            return self.getToken(CSharpParser.BASE, 0)

        def THIS(self):
            return self.getToken(CSharpParser.THIS, 0)

        def argument_list(self):
            return self.getTypedRuleContext(CSharpParser.Argument_listContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_constructor_initializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstructor_initializer" ):
                listener.enterConstructor_initializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstructor_initializer" ):
                listener.exitConstructor_initializer(self)




    def constructor_initializer(self):

        localctx = CSharpParser.Constructor_initializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 310, self.RULE_constructor_initializer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1970
            self.match(CSharpParser.COLON)
            self.state = 1971
            _la = self._input.LA(1)
            if not(_la==CSharpParser.BASE or _la==CSharpParser.THIS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 1972
            self.match(CSharpParser.OPEN_PARENS)
            self.state = 1974
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BASE) | (1 << CSharpParser.BOOL) | (1 << CSharpParser.BY) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.CHECKED) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DEFAULT) | (1 << CSharpParser.DELEGATE) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FALSE) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.IN) | (1 << CSharpParser.INT) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.LONG) | (1 << CSharpParser.NAMEOF))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (CSharpParser.NEW - 65)) | (1 << (CSharpParser.NULL - 65)) | (1 << (CSharpParser.OBJECT - 65)) | (1 << (CSharpParser.ON - 65)) | (1 << (CSharpParser.ORDERBY - 65)) | (1 << (CSharpParser.OUT - 65)) | (1 << (CSharpParser.PARTIAL - 65)) | (1 << (CSharpParser.REF - 65)) | (1 << (CSharpParser.REMOVE - 65)) | (1 << (CSharpParser.SBYTE - 65)) | (1 << (CSharpParser.SELECT - 65)) | (1 << (CSharpParser.SET - 65)) | (1 << (CSharpParser.SHORT - 65)) | (1 << (CSharpParser.SIZEOF - 65)) | (1 << (CSharpParser.STRING - 65)) | (1 << (CSharpParser.THIS - 65)) | (1 << (CSharpParser.TRUE - 65)) | (1 << (CSharpParser.TYPEOF - 65)) | (1 << (CSharpParser.UINT - 65)) | (1 << (CSharpParser.ULONG - 65)) | (1 << (CSharpParser.UNCHECKED - 65)) | (1 << (CSharpParser.UNMANAGED - 65)) | (1 << (CSharpParser.USHORT - 65)) | (1 << (CSharpParser.VAR - 65)) | (1 << (CSharpParser.WHEN - 65)) | (1 << (CSharpParser.WHERE - 65)) | (1 << (CSharpParser.YIELD - 65)) | (1 << (CSharpParser.IDENTIFIER - 65)) | (1 << (CSharpParser.LITERAL_ACCESS - 65)) | (1 << (CSharpParser.INTEGER_LITERAL - 65)) | (1 << (CSharpParser.HEX_INTEGER_LITERAL - 65)) | (1 << (CSharpParser.BIN_INTEGER_LITERAL - 65)) | (1 << (CSharpParser.REAL_LITERAL - 65)) | (1 << (CSharpParser.CHARACTER_LITERAL - 65)) | (1 << (CSharpParser.REGULAR_STRING - 65)) | (1 << (CSharpParser.VERBATIUM_STRING - 65)) | (1 << (CSharpParser.INTERPOLATED_REGULAR_STRING_START - 65)) | (1 << (CSharpParser.INTERPOLATED_VERBATIUM_STRING_START - 65)) | (1 << (CSharpParser.OPEN_PARENS - 65)))) != 0) or ((((_la - 134)) & ~0x3f) == 0 and ((1 << (_la - 134)) & ((1 << (CSharpParser.PLUS - 134)) | (1 << (CSharpParser.MINUS - 134)) | (1 << (CSharpParser.STAR - 134)) | (1 << (CSharpParser.AMP - 134)) | (1 << (CSharpParser.CARET - 134)) | (1 << (CSharpParser.BANG - 134)) | (1 << (CSharpParser.TILDE - 134)) | (1 << (CSharpParser.OP_INC - 134)) | (1 << (CSharpParser.OP_DEC - 134)) | (1 << (CSharpParser.OP_RANGE - 134)))) != 0):
                self.state = 1973
                self.argument_list()


            self.state = 1976
            self.match(CSharpParser.CLOSE_PARENS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(CSharpParser.BlockContext,0)


        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)




    def body(self):

        localctx = CSharpParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 312, self.RULE_body)
        try:
            self.state = 1980
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.OPEN_BRACE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1978
                self.block()
                pass
            elif token in [CSharpParser.SEMICOLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1979
                self.match(CSharpParser.SEMICOLON)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_interfacesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(CSharpParser.COLON, 0)

        def interface_type_list(self):
            return self.getTypedRuleContext(CSharpParser.Interface_type_listContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_struct_interfaces

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStruct_interfaces" ):
                listener.enterStruct_interfaces(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStruct_interfaces" ):
                listener.exitStruct_interfaces(self)




    def struct_interfaces(self):

        localctx = CSharpParser.Struct_interfacesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 314, self.RULE_struct_interfaces)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1982
            self.match(CSharpParser.COLON)
            self.state = 1983
            self.interface_type_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACE(self):
            return self.getToken(CSharpParser.OPEN_BRACE, 0)

        def CLOSE_BRACE(self):
            return self.getToken(CSharpParser.CLOSE_BRACE, 0)

        def struct_member_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Struct_member_declarationContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Struct_member_declarationContext,i)


        def getRuleIndex(self):
            return CSharpParser.RULE_struct_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStruct_body" ):
                listener.enterStruct_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStruct_body" ):
                listener.exitStruct_body(self)




    def struct_body(self):

        localctx = CSharpParser.Struct_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 316, self.RULE_struct_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1985
            self.match(CSharpParser.OPEN_BRACE)
            self.state = 1989
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ABSTRACT) | (1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BOOL) | (1 << CSharpParser.BY) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.CLASS) | (1 << CSharpParser.CONST) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DELEGATE) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.ENUM) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.EVENT) | (1 << CSharpParser.EXPLICIT) | (1 << CSharpParser.EXTERN) | (1 << CSharpParser.FIXED) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.IMPLICIT) | (1 << CSharpParser.INT) | (1 << CSharpParser.INTERFACE) | (1 << CSharpParser.INTERNAL) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.LONG) | (1 << CSharpParser.NAMEOF))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (CSharpParser.NEW - 65)) | (1 << (CSharpParser.OBJECT - 65)) | (1 << (CSharpParser.ON - 65)) | (1 << (CSharpParser.ORDERBY - 65)) | (1 << (CSharpParser.OVERRIDE - 65)) | (1 << (CSharpParser.PARTIAL - 65)) | (1 << (CSharpParser.PRIVATE - 65)) | (1 << (CSharpParser.PROTECTED - 65)) | (1 << (CSharpParser.PUBLIC - 65)) | (1 << (CSharpParser.READONLY - 65)) | (1 << (CSharpParser.REF - 65)) | (1 << (CSharpParser.REMOVE - 65)) | (1 << (CSharpParser.SBYTE - 65)) | (1 << (CSharpParser.SEALED - 65)) | (1 << (CSharpParser.SELECT - 65)) | (1 << (CSharpParser.SET - 65)) | (1 << (CSharpParser.SHORT - 65)) | (1 << (CSharpParser.STATIC - 65)) | (1 << (CSharpParser.STRING - 65)) | (1 << (CSharpParser.STRUCT - 65)) | (1 << (CSharpParser.UINT - 65)) | (1 << (CSharpParser.ULONG - 65)) | (1 << (CSharpParser.UNMANAGED - 65)) | (1 << (CSharpParser.UNSAFE - 65)) | (1 << (CSharpParser.USHORT - 65)) | (1 << (CSharpParser.VAR - 65)) | (1 << (CSharpParser.VIRTUAL - 65)) | (1 << (CSharpParser.VOID - 65)) | (1 << (CSharpParser.VOLATILE - 65)) | (1 << (CSharpParser.WHEN - 65)) | (1 << (CSharpParser.WHERE - 65)) | (1 << (CSharpParser.YIELD - 65)) | (1 << (CSharpParser.IDENTIFIER - 65)) | (1 << (CSharpParser.OPEN_BRACKET - 65)) | (1 << (CSharpParser.OPEN_PARENS - 65)))) != 0):
                self.state = 1986
                self.struct_member_declaration()
                self.state = 1991
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1992
            self.match(CSharpParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_member_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def common_member_declaration(self):
            return self.getTypedRuleContext(CSharpParser.Common_member_declarationContext,0)


        def FIXED(self):
            return self.getToken(CSharpParser.FIXED, 0)

        def type_(self):
            return self.getTypedRuleContext(CSharpParser.Type_Context,0)


        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def attributes(self):
            return self.getTypedRuleContext(CSharpParser.AttributesContext,0)


        def all_member_modifiers(self):
            return self.getTypedRuleContext(CSharpParser.All_member_modifiersContext,0)


        def fixed_size_buffer_declarator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Fixed_size_buffer_declaratorContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Fixed_size_buffer_declaratorContext,i)


        def getRuleIndex(self):
            return CSharpParser.RULE_struct_member_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStruct_member_declaration" ):
                listener.enterStruct_member_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStruct_member_declaration" ):
                listener.exitStruct_member_declaration(self)




    def struct_member_declaration(self):

        localctx = CSharpParser.Struct_member_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 318, self.RULE_struct_member_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1995
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.OPEN_BRACKET:
                self.state = 1994
                self.attributes()


            self.state = 1998
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,235,self._ctx)
            if la_ == 1:
                self.state = 1997
                self.all_member_modifiers()


            self.state = 2010
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.ADD, CSharpParser.ALIAS, CSharpParser.ARGLIST, CSharpParser.ASCENDING, CSharpParser.ASYNC, CSharpParser.AWAIT, CSharpParser.BOOL, CSharpParser.BY, CSharpParser.BYTE, CSharpParser.CHAR, CSharpParser.CLASS, CSharpParser.CONST, CSharpParser.DECIMAL, CSharpParser.DELEGATE, CSharpParser.DESCENDING, CSharpParser.DOUBLE, CSharpParser.DYNAMIC, CSharpParser.ENUM, CSharpParser.EQUALS, CSharpParser.EVENT, CSharpParser.EXPLICIT, CSharpParser.FLOAT, CSharpParser.FROM, CSharpParser.GET, CSharpParser.GROUP, CSharpParser.IMPLICIT, CSharpParser.INT, CSharpParser.INTERFACE, CSharpParser.INTO, CSharpParser.JOIN, CSharpParser.LET, CSharpParser.LONG, CSharpParser.NAMEOF, CSharpParser.OBJECT, CSharpParser.ON, CSharpParser.ORDERBY, CSharpParser.PARTIAL, CSharpParser.READONLY, CSharpParser.REF, CSharpParser.REMOVE, CSharpParser.SBYTE, CSharpParser.SELECT, CSharpParser.SET, CSharpParser.SHORT, CSharpParser.STRING, CSharpParser.STRUCT, CSharpParser.UINT, CSharpParser.ULONG, CSharpParser.UNMANAGED, CSharpParser.USHORT, CSharpParser.VAR, CSharpParser.VOID, CSharpParser.WHEN, CSharpParser.WHERE, CSharpParser.YIELD, CSharpParser.IDENTIFIER, CSharpParser.OPEN_PARENS]:
                self.state = 2000
                self.common_member_declaration()
                pass
            elif token in [CSharpParser.FIXED]:
                self.state = 2001
                self.match(CSharpParser.FIXED)
                self.state = 2002
                self.type_()
                self.state = 2004 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 2003
                    self.fixed_size_buffer_declarator()
                    self.state = 2006 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BY) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.NAMEOF))) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & ((1 << (CSharpParser.ON - 68)) | (1 << (CSharpParser.ORDERBY - 68)) | (1 << (CSharpParser.PARTIAL - 68)) | (1 << (CSharpParser.REMOVE - 68)) | (1 << (CSharpParser.SELECT - 68)) | (1 << (CSharpParser.SET - 68)) | (1 << (CSharpParser.UNMANAGED - 68)) | (1 << (CSharpParser.VAR - 68)) | (1 << (CSharpParser.WHEN - 68)) | (1 << (CSharpParser.WHERE - 68)) | (1 << (CSharpParser.YIELD - 68)) | (1 << (CSharpParser.IDENTIFIER - 68)))) != 0)):
                        break

                self.state = 2008
                self.match(CSharpParser.SEMICOLON)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def base_type(self):
            return self.getTypedRuleContext(CSharpParser.Base_typeContext,0)


        def rank_specifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Rank_specifierContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Rank_specifierContext,i)


        def STAR(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.STAR)
            else:
                return self.getToken(CSharpParser.STAR, i)

        def INTERR(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.INTERR)
            else:
                return self.getToken(CSharpParser.INTERR, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_array_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_type" ):
                listener.enterArray_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_type" ):
                listener.exitArray_type(self)




    def array_type(self):

        localctx = CSharpParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 320, self.RULE_array_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2012
            self.base_type()
            self.state = 2020 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 2016
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CSharpParser.STAR or _la==CSharpParser.INTERR:
                    self.state = 2013
                    _la = self._input.LA(1)
                    if not(_la==CSharpParser.STAR or _la==CSharpParser.INTERR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 2018
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 2019
                self.rank_specifier()
                self.state = 2022 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((((_la - 126)) & ~0x3f) == 0 and ((1 << (_la - 126)) & ((1 << (CSharpParser.OPEN_BRACKET - 126)) | (1 << (CSharpParser.STAR - 126)) | (1 << (CSharpParser.INTERR - 126)))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rank_specifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACKET(self):
            return self.getToken(CSharpParser.OPEN_BRACKET, 0)

        def CLOSE_BRACKET(self):
            return self.getToken(CSharpParser.CLOSE_BRACKET, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_rank_specifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRank_specifier" ):
                listener.enterRank_specifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRank_specifier" ):
                listener.exitRank_specifier(self)




    def rank_specifier(self):

        localctx = CSharpParser.Rank_specifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 322, self.RULE_rank_specifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2024
            self.match(CSharpParser.OPEN_BRACKET)
            self.state = 2028
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.COMMA:
                self.state = 2025
                self.match(CSharpParser.COMMA)
                self.state = 2030
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2031
            self.match(CSharpParser.CLOSE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_initializerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACE(self):
            return self.getToken(CSharpParser.OPEN_BRACE, 0)

        def CLOSE_BRACE(self):
            return self.getToken(CSharpParser.CLOSE_BRACE, 0)

        def variable_initializer(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Variable_initializerContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Variable_initializerContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_array_initializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_initializer" ):
                listener.enterArray_initializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_initializer" ):
                listener.exitArray_initializer(self)




    def array_initializer(self):

        localctx = CSharpParser.Array_initializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 324, self.RULE_array_initializer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2033
            self.match(CSharpParser.OPEN_BRACE)
            self.state = 2045
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BASE) | (1 << CSharpParser.BOOL) | (1 << CSharpParser.BY) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.CHECKED) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DEFAULT) | (1 << CSharpParser.DELEGATE) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FALSE) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.INT) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.LONG) | (1 << CSharpParser.NAMEOF))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (CSharpParser.NEW - 65)) | (1 << (CSharpParser.NULL - 65)) | (1 << (CSharpParser.OBJECT - 65)) | (1 << (CSharpParser.ON - 65)) | (1 << (CSharpParser.ORDERBY - 65)) | (1 << (CSharpParser.PARTIAL - 65)) | (1 << (CSharpParser.REF - 65)) | (1 << (CSharpParser.REMOVE - 65)) | (1 << (CSharpParser.SBYTE - 65)) | (1 << (CSharpParser.SELECT - 65)) | (1 << (CSharpParser.SET - 65)) | (1 << (CSharpParser.SHORT - 65)) | (1 << (CSharpParser.SIZEOF - 65)) | (1 << (CSharpParser.STRING - 65)) | (1 << (CSharpParser.THIS - 65)) | (1 << (CSharpParser.TRUE - 65)) | (1 << (CSharpParser.TYPEOF - 65)) | (1 << (CSharpParser.UINT - 65)) | (1 << (CSharpParser.ULONG - 65)) | (1 << (CSharpParser.UNCHECKED - 65)) | (1 << (CSharpParser.UNMANAGED - 65)) | (1 << (CSharpParser.USHORT - 65)) | (1 << (CSharpParser.VAR - 65)) | (1 << (CSharpParser.WHEN - 65)) | (1 << (CSharpParser.WHERE - 65)) | (1 << (CSharpParser.YIELD - 65)) | (1 << (CSharpParser.IDENTIFIER - 65)) | (1 << (CSharpParser.LITERAL_ACCESS - 65)) | (1 << (CSharpParser.INTEGER_LITERAL - 65)) | (1 << (CSharpParser.HEX_INTEGER_LITERAL - 65)) | (1 << (CSharpParser.BIN_INTEGER_LITERAL - 65)) | (1 << (CSharpParser.REAL_LITERAL - 65)) | (1 << (CSharpParser.CHARACTER_LITERAL - 65)) | (1 << (CSharpParser.REGULAR_STRING - 65)) | (1 << (CSharpParser.VERBATIUM_STRING - 65)) | (1 << (CSharpParser.INTERPOLATED_REGULAR_STRING_START - 65)) | (1 << (CSharpParser.INTERPOLATED_VERBATIUM_STRING_START - 65)) | (1 << (CSharpParser.OPEN_BRACE - 65)) | (1 << (CSharpParser.OPEN_PARENS - 65)))) != 0) or ((((_la - 134)) & ~0x3f) == 0 and ((1 << (_la - 134)) & ((1 << (CSharpParser.PLUS - 134)) | (1 << (CSharpParser.MINUS - 134)) | (1 << (CSharpParser.STAR - 134)) | (1 << (CSharpParser.AMP - 134)) | (1 << (CSharpParser.CARET - 134)) | (1 << (CSharpParser.BANG - 134)) | (1 << (CSharpParser.TILDE - 134)) | (1 << (CSharpParser.OP_INC - 134)) | (1 << (CSharpParser.OP_DEC - 134)) | (1 << (CSharpParser.OP_RANGE - 134)))) != 0):
                self.state = 2034
                self.variable_initializer()
                self.state = 2039
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,241,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 2035
                        self.match(CSharpParser.COMMA)
                        self.state = 2036
                        self.variable_initializer() 
                    self.state = 2041
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,241,self._ctx)

                self.state = 2043
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.COMMA:
                    self.state = 2042
                    self.match(CSharpParser.COMMA)




            self.state = 2047
            self.match(CSharpParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variant_type_parameter_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(CSharpParser.LT, 0)

        def variant_type_parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Variant_type_parameterContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Variant_type_parameterContext,i)


        def GT(self):
            return self.getToken(CSharpParser.GT, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_variant_type_parameter_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariant_type_parameter_list" ):
                listener.enterVariant_type_parameter_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariant_type_parameter_list" ):
                listener.exitVariant_type_parameter_list(self)




    def variant_type_parameter_list(self):

        localctx = CSharpParser.Variant_type_parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 326, self.RULE_variant_type_parameter_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2049
            self.match(CSharpParser.LT)
            self.state = 2050
            self.variant_type_parameter()
            self.state = 2055
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.COMMA:
                self.state = 2051
                self.match(CSharpParser.COMMA)
                self.state = 2052
                self.variant_type_parameter()
                self.state = 2057
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2058
            self.match(CSharpParser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variant_type_parameterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def attributes(self):
            return self.getTypedRuleContext(CSharpParser.AttributesContext,0)


        def variance_annotation(self):
            return self.getTypedRuleContext(CSharpParser.Variance_annotationContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_variant_type_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariant_type_parameter" ):
                listener.enterVariant_type_parameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariant_type_parameter" ):
                listener.exitVariant_type_parameter(self)




    def variant_type_parameter(self):

        localctx = CSharpParser.Variant_type_parameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 328, self.RULE_variant_type_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2061
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.OPEN_BRACKET:
                self.state = 2060
                self.attributes()


            self.state = 2064
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.IN or _la==CSharpParser.OUT:
                self.state = 2063
                self.variance_annotation()


            self.state = 2066
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variance_annotationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IN(self):
            return self.getToken(CSharpParser.IN, 0)

        def OUT(self):
            return self.getToken(CSharpParser.OUT, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_variance_annotation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariance_annotation" ):
                listener.enterVariance_annotation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariance_annotation" ):
                listener.exitVariance_annotation(self)




    def variance_annotation(self):

        localctx = CSharpParser.Variance_annotationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 330, self.RULE_variance_annotation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2068
            _la = self._input.LA(1)
            if not(_la==CSharpParser.IN or _la==CSharpParser.OUT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_baseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(CSharpParser.COLON, 0)

        def interface_type_list(self):
            return self.getTypedRuleContext(CSharpParser.Interface_type_listContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_interface_base

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterface_base" ):
                listener.enterInterface_base(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterface_base" ):
                listener.exitInterface_base(self)




    def interface_base(self):

        localctx = CSharpParser.Interface_baseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 332, self.RULE_interface_base)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2070
            self.match(CSharpParser.COLON)
            self.state = 2071
            self.interface_type_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACE(self):
            return self.getToken(CSharpParser.OPEN_BRACE, 0)

        def CLOSE_BRACE(self):
            return self.getToken(CSharpParser.CLOSE_BRACE, 0)

        def interface_member_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Interface_member_declarationContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Interface_member_declarationContext,i)


        def getRuleIndex(self):
            return CSharpParser.RULE_interface_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterface_body" ):
                listener.enterInterface_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterface_body" ):
                listener.exitInterface_body(self)




    def interface_body(self):

        localctx = CSharpParser.Interface_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 334, self.RULE_interface_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2073
            self.match(CSharpParser.OPEN_BRACE)
            self.state = 2077
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BOOL) | (1 << CSharpParser.BY) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.EVENT) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.INT) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.LONG) | (1 << CSharpParser.NAMEOF))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (CSharpParser.NEW - 65)) | (1 << (CSharpParser.OBJECT - 65)) | (1 << (CSharpParser.ON - 65)) | (1 << (CSharpParser.ORDERBY - 65)) | (1 << (CSharpParser.PARTIAL - 65)) | (1 << (CSharpParser.READONLY - 65)) | (1 << (CSharpParser.REF - 65)) | (1 << (CSharpParser.REMOVE - 65)) | (1 << (CSharpParser.SBYTE - 65)) | (1 << (CSharpParser.SELECT - 65)) | (1 << (CSharpParser.SET - 65)) | (1 << (CSharpParser.SHORT - 65)) | (1 << (CSharpParser.STRING - 65)) | (1 << (CSharpParser.UINT - 65)) | (1 << (CSharpParser.ULONG - 65)) | (1 << (CSharpParser.UNMANAGED - 65)) | (1 << (CSharpParser.UNSAFE - 65)) | (1 << (CSharpParser.USHORT - 65)) | (1 << (CSharpParser.VAR - 65)) | (1 << (CSharpParser.VOID - 65)) | (1 << (CSharpParser.WHEN - 65)) | (1 << (CSharpParser.WHERE - 65)) | (1 << (CSharpParser.YIELD - 65)) | (1 << (CSharpParser.IDENTIFIER - 65)) | (1 << (CSharpParser.OPEN_BRACKET - 65)) | (1 << (CSharpParser.OPEN_PARENS - 65)))) != 0):
                self.state = 2074
                self.interface_member_declaration()
                self.state = 2079
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2080
            self.match(CSharpParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_member_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(CSharpParser.Type_Context,0)


        def VOID(self):
            return self.getToken(CSharpParser.VOID, 0)

        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)

        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def EVENT(self):
            return self.getToken(CSharpParser.EVENT, 0)

        def attributes(self):
            return self.getTypedRuleContext(CSharpParser.AttributesContext,0)


        def NEW(self):
            return self.getToken(CSharpParser.NEW, 0)

        def OPEN_BRACE(self):
            return self.getToken(CSharpParser.OPEN_BRACE, 0)

        def interface_accessors(self):
            return self.getTypedRuleContext(CSharpParser.Interface_accessorsContext,0)


        def CLOSE_BRACE(self):
            return self.getToken(CSharpParser.CLOSE_BRACE, 0)

        def THIS(self):
            return self.getToken(CSharpParser.THIS, 0)

        def OPEN_BRACKET(self):
            return self.getToken(CSharpParser.OPEN_BRACKET, 0)

        def formal_parameter_list(self):
            return self.getTypedRuleContext(CSharpParser.Formal_parameter_listContext,0)


        def CLOSE_BRACKET(self):
            return self.getToken(CSharpParser.CLOSE_BRACKET, 0)

        def UNSAFE(self):
            return self.getToken(CSharpParser.UNSAFE, 0)

        def REF(self):
            return self.getToken(CSharpParser.REF, 0)

        def READONLY(self):
            return self.getToken(CSharpParser.READONLY, 0)

        def type_parameter_list(self):
            return self.getTypedRuleContext(CSharpParser.Type_parameter_listContext,0)


        def type_parameter_constraints_clauses(self):
            return self.getTypedRuleContext(CSharpParser.Type_parameter_constraints_clausesContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_interface_member_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterface_member_declaration" ):
                listener.enterInterface_member_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterface_member_declaration" ):
                listener.exitInterface_member_declaration(self)




    def interface_member_declaration(self):

        localctx = CSharpParser.Interface_member_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 336, self.RULE_interface_member_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2083
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.OPEN_BRACKET:
                self.state = 2082
                self.attributes()


            self.state = 2086
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.NEW:
                self.state = 2085
                self.match(CSharpParser.NEW)


            self.state = 2151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,260,self._ctx)
            if la_ == 1:
                self.state = 2089
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.UNSAFE:
                    self.state = 2088
                    self.match(CSharpParser.UNSAFE)


                self.state = 2096
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,251,self._ctx)
                if la_ == 1:
                    self.state = 2091
                    self.match(CSharpParser.REF)

                elif la_ == 2:
                    self.state = 2092
                    self.match(CSharpParser.REF)
                    self.state = 2093
                    self.match(CSharpParser.READONLY)

                elif la_ == 3:
                    self.state = 2094
                    self.match(CSharpParser.READONLY)
                    self.state = 2095
                    self.match(CSharpParser.REF)


                self.state = 2098
                self.type_()
                self.state = 2126
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,255,self._ctx)
                if la_ == 1:
                    self.state = 2099
                    self.identifier()
                    self.state = 2101
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==CSharpParser.LT:
                        self.state = 2100
                        self.type_parameter_list()


                    self.state = 2103
                    self.match(CSharpParser.OPEN_PARENS)
                    self.state = 2105
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BOOL) | (1 << CSharpParser.BY) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.IN) | (1 << CSharpParser.INT) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.LONG) | (1 << CSharpParser.NAMEOF))) != 0) or ((((_la - 67)) & ~0x3f) == 0 and ((1 << (_la - 67)) & ((1 << (CSharpParser.OBJECT - 67)) | (1 << (CSharpParser.ON - 67)) | (1 << (CSharpParser.ORDERBY - 67)) | (1 << (CSharpParser.OUT - 67)) | (1 << (CSharpParser.PARAMS - 67)) | (1 << (CSharpParser.PARTIAL - 67)) | (1 << (CSharpParser.REF - 67)) | (1 << (CSharpParser.REMOVE - 67)) | (1 << (CSharpParser.SBYTE - 67)) | (1 << (CSharpParser.SELECT - 67)) | (1 << (CSharpParser.SET - 67)) | (1 << (CSharpParser.SHORT - 67)) | (1 << (CSharpParser.STRING - 67)) | (1 << (CSharpParser.THIS - 67)) | (1 << (CSharpParser.UINT - 67)) | (1 << (CSharpParser.ULONG - 67)) | (1 << (CSharpParser.UNMANAGED - 67)) | (1 << (CSharpParser.USHORT - 67)) | (1 << (CSharpParser.VAR - 67)) | (1 << (CSharpParser.VOID - 67)) | (1 << (CSharpParser.WHEN - 67)) | (1 << (CSharpParser.WHERE - 67)) | (1 << (CSharpParser.YIELD - 67)) | (1 << (CSharpParser.IDENTIFIER - 67)) | (1 << (CSharpParser.OPEN_BRACKET - 67)) | (1 << (CSharpParser.OPEN_PARENS - 67)))) != 0):
                        self.state = 2104
                        self.formal_parameter_list()


                    self.state = 2107
                    self.match(CSharpParser.CLOSE_PARENS)
                    self.state = 2109
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==CSharpParser.WHERE:
                        self.state = 2108
                        self.type_parameter_constraints_clauses()


                    self.state = 2111
                    self.match(CSharpParser.SEMICOLON)
                    pass

                elif la_ == 2:
                    self.state = 2113
                    self.identifier()
                    self.state = 2114
                    self.match(CSharpParser.OPEN_BRACE)
                    self.state = 2115
                    self.interface_accessors()
                    self.state = 2116
                    self.match(CSharpParser.CLOSE_BRACE)
                    pass

                elif la_ == 3:
                    self.state = 2118
                    self.match(CSharpParser.THIS)
                    self.state = 2119
                    self.match(CSharpParser.OPEN_BRACKET)
                    self.state = 2120
                    self.formal_parameter_list()
                    self.state = 2121
                    self.match(CSharpParser.CLOSE_BRACKET)
                    self.state = 2122
                    self.match(CSharpParser.OPEN_BRACE)
                    self.state = 2123
                    self.interface_accessors()
                    self.state = 2124
                    self.match(CSharpParser.CLOSE_BRACE)
                    pass


                pass

            elif la_ == 2:
                self.state = 2129
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.UNSAFE:
                    self.state = 2128
                    self.match(CSharpParser.UNSAFE)


                self.state = 2131
                self.match(CSharpParser.VOID)
                self.state = 2132
                self.identifier()
                self.state = 2134
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.LT:
                    self.state = 2133
                    self.type_parameter_list()


                self.state = 2136
                self.match(CSharpParser.OPEN_PARENS)
                self.state = 2138
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BOOL) | (1 << CSharpParser.BY) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.IN) | (1 << CSharpParser.INT) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.LONG) | (1 << CSharpParser.NAMEOF))) != 0) or ((((_la - 67)) & ~0x3f) == 0 and ((1 << (_la - 67)) & ((1 << (CSharpParser.OBJECT - 67)) | (1 << (CSharpParser.ON - 67)) | (1 << (CSharpParser.ORDERBY - 67)) | (1 << (CSharpParser.OUT - 67)) | (1 << (CSharpParser.PARAMS - 67)) | (1 << (CSharpParser.PARTIAL - 67)) | (1 << (CSharpParser.REF - 67)) | (1 << (CSharpParser.REMOVE - 67)) | (1 << (CSharpParser.SBYTE - 67)) | (1 << (CSharpParser.SELECT - 67)) | (1 << (CSharpParser.SET - 67)) | (1 << (CSharpParser.SHORT - 67)) | (1 << (CSharpParser.STRING - 67)) | (1 << (CSharpParser.THIS - 67)) | (1 << (CSharpParser.UINT - 67)) | (1 << (CSharpParser.ULONG - 67)) | (1 << (CSharpParser.UNMANAGED - 67)) | (1 << (CSharpParser.USHORT - 67)) | (1 << (CSharpParser.VAR - 67)) | (1 << (CSharpParser.VOID - 67)) | (1 << (CSharpParser.WHEN - 67)) | (1 << (CSharpParser.WHERE - 67)) | (1 << (CSharpParser.YIELD - 67)) | (1 << (CSharpParser.IDENTIFIER - 67)) | (1 << (CSharpParser.OPEN_BRACKET - 67)) | (1 << (CSharpParser.OPEN_PARENS - 67)))) != 0):
                    self.state = 2137
                    self.formal_parameter_list()


                self.state = 2140
                self.match(CSharpParser.CLOSE_PARENS)
                self.state = 2142
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.WHERE:
                    self.state = 2141
                    self.type_parameter_constraints_clauses()


                self.state = 2144
                self.match(CSharpParser.SEMICOLON)
                pass

            elif la_ == 3:
                self.state = 2146
                self.match(CSharpParser.EVENT)
                self.state = 2147
                self.type_()
                self.state = 2148
                self.identifier()
                self.state = 2149
                self.match(CSharpParser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_accessorsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GET(self):
            return self.getToken(CSharpParser.GET, 0)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.SEMICOLON)
            else:
                return self.getToken(CSharpParser.SEMICOLON, i)

        def SET(self):
            return self.getToken(CSharpParser.SET, 0)

        def attributes(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.AttributesContext)
            else:
                return self.getTypedRuleContext(CSharpParser.AttributesContext,i)


        def getRuleIndex(self):
            return CSharpParser.RULE_interface_accessors

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterface_accessors" ):
                listener.enterInterface_accessors(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterface_accessors" ):
                listener.exitInterface_accessors(self)




    def interface_accessors(self):

        localctx = CSharpParser.Interface_accessorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 338, self.RULE_interface_accessors)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.OPEN_BRACKET:
                self.state = 2153
                self.attributes()


            self.state = 2174
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.GET]:
                self.state = 2156
                self.match(CSharpParser.GET)
                self.state = 2157
                self.match(CSharpParser.SEMICOLON)
                self.state = 2163
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.SET or _la==CSharpParser.OPEN_BRACKET:
                    self.state = 2159
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==CSharpParser.OPEN_BRACKET:
                        self.state = 2158
                        self.attributes()


                    self.state = 2161
                    self.match(CSharpParser.SET)
                    self.state = 2162
                    self.match(CSharpParser.SEMICOLON)


                pass
            elif token in [CSharpParser.SET]:
                self.state = 2165
                self.match(CSharpParser.SET)
                self.state = 2166
                self.match(CSharpParser.SEMICOLON)
                self.state = 2172
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.GET or _la==CSharpParser.OPEN_BRACKET:
                    self.state = 2168
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==CSharpParser.OPEN_BRACKET:
                        self.state = 2167
                        self.attributes()


                    self.state = 2170
                    self.match(CSharpParser.GET)
                    self.state = 2171
                    self.match(CSharpParser.SEMICOLON)


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Enum_baseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(CSharpParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(CSharpParser.Type_Context,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_enum_base

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnum_base" ):
                listener.enterEnum_base(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnum_base" ):
                listener.exitEnum_base(self)




    def enum_base(self):

        localctx = CSharpParser.Enum_baseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 340, self.RULE_enum_base)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2176
            self.match(CSharpParser.COLON)
            self.state = 2177
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Enum_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACE(self):
            return self.getToken(CSharpParser.OPEN_BRACE, 0)

        def CLOSE_BRACE(self):
            return self.getToken(CSharpParser.CLOSE_BRACE, 0)

        def enum_member_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Enum_member_declarationContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Enum_member_declarationContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_enum_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnum_body" ):
                listener.enterEnum_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnum_body" ):
                listener.exitEnum_body(self)




    def enum_body(self):

        localctx = CSharpParser.Enum_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 342, self.RULE_enum_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2179
            self.match(CSharpParser.OPEN_BRACE)
            self.state = 2191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BY) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.NAMEOF))) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & ((1 << (CSharpParser.ON - 68)) | (1 << (CSharpParser.ORDERBY - 68)) | (1 << (CSharpParser.PARTIAL - 68)) | (1 << (CSharpParser.REMOVE - 68)) | (1 << (CSharpParser.SELECT - 68)) | (1 << (CSharpParser.SET - 68)) | (1 << (CSharpParser.UNMANAGED - 68)) | (1 << (CSharpParser.VAR - 68)) | (1 << (CSharpParser.WHEN - 68)) | (1 << (CSharpParser.WHERE - 68)) | (1 << (CSharpParser.YIELD - 68)) | (1 << (CSharpParser.IDENTIFIER - 68)) | (1 << (CSharpParser.OPEN_BRACKET - 68)))) != 0):
                self.state = 2180
                self.enum_member_declaration()
                self.state = 2185
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,267,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 2181
                        self.match(CSharpParser.COMMA)
                        self.state = 2182
                        self.enum_member_declaration() 
                    self.state = 2187
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,267,self._ctx)

                self.state = 2189
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.COMMA:
                    self.state = 2188
                    self.match(CSharpParser.COMMA)




            self.state = 2193
            self.match(CSharpParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Enum_member_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def attributes(self):
            return self.getTypedRuleContext(CSharpParser.AttributesContext,0)


        def ASSIGNMENT(self):
            return self.getToken(CSharpParser.ASSIGNMENT, 0)

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_enum_member_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnum_member_declaration" ):
                listener.enterEnum_member_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnum_member_declaration" ):
                listener.exitEnum_member_declaration(self)




    def enum_member_declaration(self):

        localctx = CSharpParser.Enum_member_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 344, self.RULE_enum_member_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.OPEN_BRACKET:
                self.state = 2195
                self.attributes()


            self.state = 2198
            self.identifier()
            self.state = 2201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.ASSIGNMENT:
                self.state = 2199
                self.match(CSharpParser.ASSIGNMENT)
                self.state = 2200
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Global_attribute_sectionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACKET(self):
            return self.getToken(CSharpParser.OPEN_BRACKET, 0)

        def global_attribute_target(self):
            return self.getTypedRuleContext(CSharpParser.Global_attribute_targetContext,0)


        def COLON(self):
            return self.getToken(CSharpParser.COLON, 0)

        def attribute_list(self):
            return self.getTypedRuleContext(CSharpParser.Attribute_listContext,0)


        def CLOSE_BRACKET(self):
            return self.getToken(CSharpParser.CLOSE_BRACKET, 0)

        def COMMA(self):
            return self.getToken(CSharpParser.COMMA, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_global_attribute_section

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGlobal_attribute_section" ):
                listener.enterGlobal_attribute_section(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGlobal_attribute_section" ):
                listener.exitGlobal_attribute_section(self)




    def global_attribute_section(self):

        localctx = CSharpParser.Global_attribute_sectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 346, self.RULE_global_attribute_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2203
            self.match(CSharpParser.OPEN_BRACKET)
            self.state = 2204
            self.global_attribute_target()
            self.state = 2205
            self.match(CSharpParser.COLON)
            self.state = 2206
            self.attribute_list()
            self.state = 2208
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.COMMA:
                self.state = 2207
                self.match(CSharpParser.COMMA)


            self.state = 2210
            self.match(CSharpParser.CLOSE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Global_attribute_targetContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def keyword(self):
            return self.getTypedRuleContext(CSharpParser.KeywordContext,0)


        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_global_attribute_target

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGlobal_attribute_target" ):
                listener.enterGlobal_attribute_target(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGlobal_attribute_target" ):
                listener.exitGlobal_attribute_target(self)




    def global_attribute_target(self):

        localctx = CSharpParser.Global_attribute_targetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 348, self.RULE_global_attribute_target)
        try:
            self.state = 2214
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,273,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2212
                self.keyword()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2213
                self.identifier()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_section(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Attribute_sectionContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Attribute_sectionContext,i)


        def getRuleIndex(self):
            return CSharpParser.RULE_attributes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttributes" ):
                listener.enterAttributes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttributes" ):
                listener.exitAttributes(self)




    def attributes(self):

        localctx = CSharpParser.AttributesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 350, self.RULE_attributes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2217 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 2216
                self.attribute_section()
                self.state = 2219 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CSharpParser.OPEN_BRACKET):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_sectionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACKET(self):
            return self.getToken(CSharpParser.OPEN_BRACKET, 0)

        def attribute_list(self):
            return self.getTypedRuleContext(CSharpParser.Attribute_listContext,0)


        def CLOSE_BRACKET(self):
            return self.getToken(CSharpParser.CLOSE_BRACKET, 0)

        def attribute_target(self):
            return self.getTypedRuleContext(CSharpParser.Attribute_targetContext,0)


        def COLON(self):
            return self.getToken(CSharpParser.COLON, 0)

        def COMMA(self):
            return self.getToken(CSharpParser.COMMA, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_attribute_section

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute_section" ):
                listener.enterAttribute_section(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute_section" ):
                listener.exitAttribute_section(self)




    def attribute_section(self):

        localctx = CSharpParser.Attribute_sectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 352, self.RULE_attribute_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2221
            self.match(CSharpParser.OPEN_BRACKET)
            self.state = 2225
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,275,self._ctx)
            if la_ == 1:
                self.state = 2222
                self.attribute_target()
                self.state = 2223
                self.match(CSharpParser.COLON)


            self.state = 2227
            self.attribute_list()
            self.state = 2229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.COMMA:
                self.state = 2228
                self.match(CSharpParser.COMMA)


            self.state = 2231
            self.match(CSharpParser.CLOSE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_targetContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def keyword(self):
            return self.getTypedRuleContext(CSharpParser.KeywordContext,0)


        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_attribute_target

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute_target" ):
                listener.enterAttribute_target(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute_target" ):
                listener.exitAttribute_target(self)




    def attribute_target(self):

        localctx = CSharpParser.Attribute_targetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 354, self.RULE_attribute_target)
        try:
            self.state = 2235
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,277,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2233
                self.keyword()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2234
                self.identifier()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.AttributeContext)
            else:
                return self.getTypedRuleContext(CSharpParser.AttributeContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_attribute_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute_list" ):
                listener.enterAttribute_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute_list" ):
                listener.exitAttribute_list(self)




    def attribute_list(self):

        localctx = CSharpParser.Attribute_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 356, self.RULE_attribute_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2237
            self.attribute()
            self.state = 2242
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,278,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2238
                    self.match(CSharpParser.COMMA)
                    self.state = 2239
                    self.attribute() 
                self.state = 2244
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,278,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def namespace_or_type_name(self):
            return self.getTypedRuleContext(CSharpParser.Namespace_or_type_nameContext,0)


        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)

        def attribute_argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Attribute_argumentContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Attribute_argumentContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_attribute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute" ):
                listener.enterAttribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute" ):
                listener.exitAttribute(self)




    def attribute(self):

        localctx = CSharpParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 358, self.RULE_attribute)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2245
            self.namespace_or_type_name()
            self.state = 2258
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.OPEN_PARENS:
                self.state = 2246
                self.match(CSharpParser.OPEN_PARENS)
                self.state = 2255
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BASE) | (1 << CSharpParser.BOOL) | (1 << CSharpParser.BY) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.CHECKED) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DEFAULT) | (1 << CSharpParser.DELEGATE) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FALSE) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.INT) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.LONG) | (1 << CSharpParser.NAMEOF))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (CSharpParser.NEW - 65)) | (1 << (CSharpParser.NULL - 65)) | (1 << (CSharpParser.OBJECT - 65)) | (1 << (CSharpParser.ON - 65)) | (1 << (CSharpParser.ORDERBY - 65)) | (1 << (CSharpParser.PARTIAL - 65)) | (1 << (CSharpParser.REF - 65)) | (1 << (CSharpParser.REMOVE - 65)) | (1 << (CSharpParser.SBYTE - 65)) | (1 << (CSharpParser.SELECT - 65)) | (1 << (CSharpParser.SET - 65)) | (1 << (CSharpParser.SHORT - 65)) | (1 << (CSharpParser.SIZEOF - 65)) | (1 << (CSharpParser.STRING - 65)) | (1 << (CSharpParser.THIS - 65)) | (1 << (CSharpParser.TRUE - 65)) | (1 << (CSharpParser.TYPEOF - 65)) | (1 << (CSharpParser.UINT - 65)) | (1 << (CSharpParser.ULONG - 65)) | (1 << (CSharpParser.UNCHECKED - 65)) | (1 << (CSharpParser.UNMANAGED - 65)) | (1 << (CSharpParser.USHORT - 65)) | (1 << (CSharpParser.VAR - 65)) | (1 << (CSharpParser.WHEN - 65)) | (1 << (CSharpParser.WHERE - 65)) | (1 << (CSharpParser.YIELD - 65)) | (1 << (CSharpParser.IDENTIFIER - 65)) | (1 << (CSharpParser.LITERAL_ACCESS - 65)) | (1 << (CSharpParser.INTEGER_LITERAL - 65)) | (1 << (CSharpParser.HEX_INTEGER_LITERAL - 65)) | (1 << (CSharpParser.BIN_INTEGER_LITERAL - 65)) | (1 << (CSharpParser.REAL_LITERAL - 65)) | (1 << (CSharpParser.CHARACTER_LITERAL - 65)) | (1 << (CSharpParser.REGULAR_STRING - 65)) | (1 << (CSharpParser.VERBATIUM_STRING - 65)) | (1 << (CSharpParser.INTERPOLATED_REGULAR_STRING_START - 65)) | (1 << (CSharpParser.INTERPOLATED_VERBATIUM_STRING_START - 65)) | (1 << (CSharpParser.OPEN_PARENS - 65)))) != 0) or ((((_la - 134)) & ~0x3f) == 0 and ((1 << (_la - 134)) & ((1 << (CSharpParser.PLUS - 134)) | (1 << (CSharpParser.MINUS - 134)) | (1 << (CSharpParser.STAR - 134)) | (1 << (CSharpParser.AMP - 134)) | (1 << (CSharpParser.CARET - 134)) | (1 << (CSharpParser.BANG - 134)) | (1 << (CSharpParser.TILDE - 134)) | (1 << (CSharpParser.OP_INC - 134)) | (1 << (CSharpParser.OP_DEC - 134)) | (1 << (CSharpParser.OP_RANGE - 134)))) != 0):
                    self.state = 2247
                    self.attribute_argument()
                    self.state = 2252
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==CSharpParser.COMMA:
                        self.state = 2248
                        self.match(CSharpParser.COMMA)
                        self.state = 2249
                        self.attribute_argument()
                        self.state = 2254
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 2257
                self.match(CSharpParser.CLOSE_PARENS)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_argumentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def COLON(self):
            return self.getToken(CSharpParser.COLON, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_attribute_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute_argument" ):
                listener.enterAttribute_argument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute_argument" ):
                listener.exitAttribute_argument(self)




    def attribute_argument(self):

        localctx = CSharpParser.Attribute_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 360, self.RULE_attribute_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2263
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,282,self._ctx)
            if la_ == 1:
                self.state = 2260
                self.identifier()
                self.state = 2261
                self.match(CSharpParser.COLON)


            self.state = 2265
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pointer_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(CSharpParser.STAR, 0)

        def simple_type(self):
            return self.getTypedRuleContext(CSharpParser.Simple_typeContext,0)


        def class_type(self):
            return self.getTypedRuleContext(CSharpParser.Class_typeContext,0)


        def rank_specifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Rank_specifierContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Rank_specifierContext,i)


        def INTERR(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.INTERR)
            else:
                return self.getToken(CSharpParser.INTERR, i)

        def VOID(self):
            return self.getToken(CSharpParser.VOID, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_pointer_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPointer_type" ):
                listener.enterPointer_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPointer_type" ):
                listener.exitPointer_type(self)




    def pointer_type(self):

        localctx = CSharpParser.Pointer_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 362, self.RULE_pointer_type)
        self._la = 0 # Token type
        try:
            self.state = 2282
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.ADD, CSharpParser.ALIAS, CSharpParser.ARGLIST, CSharpParser.ASCENDING, CSharpParser.ASYNC, CSharpParser.AWAIT, CSharpParser.BOOL, CSharpParser.BY, CSharpParser.BYTE, CSharpParser.CHAR, CSharpParser.DECIMAL, CSharpParser.DESCENDING, CSharpParser.DOUBLE, CSharpParser.DYNAMIC, CSharpParser.EQUALS, CSharpParser.FLOAT, CSharpParser.FROM, CSharpParser.GET, CSharpParser.GROUP, CSharpParser.INT, CSharpParser.INTO, CSharpParser.JOIN, CSharpParser.LET, CSharpParser.LONG, CSharpParser.NAMEOF, CSharpParser.OBJECT, CSharpParser.ON, CSharpParser.ORDERBY, CSharpParser.PARTIAL, CSharpParser.REMOVE, CSharpParser.SBYTE, CSharpParser.SELECT, CSharpParser.SET, CSharpParser.SHORT, CSharpParser.STRING, CSharpParser.UINT, CSharpParser.ULONG, CSharpParser.UNMANAGED, CSharpParser.USHORT, CSharpParser.VAR, CSharpParser.WHEN, CSharpParser.WHERE, CSharpParser.YIELD, CSharpParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2269
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSharpParser.BOOL, CSharpParser.BYTE, CSharpParser.CHAR, CSharpParser.DECIMAL, CSharpParser.DOUBLE, CSharpParser.FLOAT, CSharpParser.INT, CSharpParser.LONG, CSharpParser.SBYTE, CSharpParser.SHORT, CSharpParser.UINT, CSharpParser.ULONG, CSharpParser.USHORT]:
                    self.state = 2267
                    self.simple_type()
                    pass
                elif token in [CSharpParser.ADD, CSharpParser.ALIAS, CSharpParser.ARGLIST, CSharpParser.ASCENDING, CSharpParser.ASYNC, CSharpParser.AWAIT, CSharpParser.BY, CSharpParser.DESCENDING, CSharpParser.DYNAMIC, CSharpParser.EQUALS, CSharpParser.FROM, CSharpParser.GET, CSharpParser.GROUP, CSharpParser.INTO, CSharpParser.JOIN, CSharpParser.LET, CSharpParser.NAMEOF, CSharpParser.OBJECT, CSharpParser.ON, CSharpParser.ORDERBY, CSharpParser.PARTIAL, CSharpParser.REMOVE, CSharpParser.SELECT, CSharpParser.SET, CSharpParser.STRING, CSharpParser.UNMANAGED, CSharpParser.VAR, CSharpParser.WHEN, CSharpParser.WHERE, CSharpParser.YIELD, CSharpParser.IDENTIFIER]:
                    self.state = 2268
                    self.class_type()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 2275
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CSharpParser.OPEN_BRACKET or _la==CSharpParser.INTERR:
                    self.state = 2273
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [CSharpParser.OPEN_BRACKET]:
                        self.state = 2271
                        self.rank_specifier()
                        pass
                    elif token in [CSharpParser.INTERR]:
                        self.state = 2272
                        self.match(CSharpParser.INTERR)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 2277
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 2278
                self.match(CSharpParser.STAR)
                pass
            elif token in [CSharpParser.VOID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2280
                self.match(CSharpParser.VOID)
                self.state = 2281
                self.match(CSharpParser.STAR)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fixed_pointer_declaratorsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fixed_pointer_declarator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Fixed_pointer_declaratorContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Fixed_pointer_declaratorContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_fixed_pointer_declarators

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFixed_pointer_declarators" ):
                listener.enterFixed_pointer_declarators(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFixed_pointer_declarators" ):
                listener.exitFixed_pointer_declarators(self)




    def fixed_pointer_declarators(self):

        localctx = CSharpParser.Fixed_pointer_declaratorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 364, self.RULE_fixed_pointer_declarators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2284
            self.fixed_pointer_declarator()
            self.state = 2289
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.COMMA:
                self.state = 2285
                self.match(CSharpParser.COMMA)
                self.state = 2286
                self.fixed_pointer_declarator()
                self.state = 2291
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fixed_pointer_declaratorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def ASSIGNMENT(self):
            return self.getToken(CSharpParser.ASSIGNMENT, 0)

        def fixed_pointer_initializer(self):
            return self.getTypedRuleContext(CSharpParser.Fixed_pointer_initializerContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_fixed_pointer_declarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFixed_pointer_declarator" ):
                listener.enterFixed_pointer_declarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFixed_pointer_declarator" ):
                listener.exitFixed_pointer_declarator(self)




    def fixed_pointer_declarator(self):

        localctx = CSharpParser.Fixed_pointer_declaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 366, self.RULE_fixed_pointer_declarator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2292
            self.identifier()
            self.state = 2293
            self.match(CSharpParser.ASSIGNMENT)
            self.state = 2294
            self.fixed_pointer_initializer()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fixed_pointer_initializerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def AMP(self):
            return self.getToken(CSharpParser.AMP, 0)

        def stackalloc_initializer(self):
            return self.getTypedRuleContext(CSharpParser.Stackalloc_initializerContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_fixed_pointer_initializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFixed_pointer_initializer" ):
                listener.enterFixed_pointer_initializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFixed_pointer_initializer" ):
                listener.exitFixed_pointer_initializer(self)




    def fixed_pointer_initializer(self):

        localctx = CSharpParser.Fixed_pointer_initializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 368, self.RULE_fixed_pointer_initializer)
        try:
            self.state = 2301
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.ADD, CSharpParser.ALIAS, CSharpParser.ARGLIST, CSharpParser.ASCENDING, CSharpParser.ASYNC, CSharpParser.AWAIT, CSharpParser.BASE, CSharpParser.BOOL, CSharpParser.BY, CSharpParser.BYTE, CSharpParser.CHAR, CSharpParser.CHECKED, CSharpParser.DECIMAL, CSharpParser.DEFAULT, CSharpParser.DELEGATE, CSharpParser.DESCENDING, CSharpParser.DOUBLE, CSharpParser.DYNAMIC, CSharpParser.EQUALS, CSharpParser.FALSE, CSharpParser.FLOAT, CSharpParser.FROM, CSharpParser.GET, CSharpParser.GROUP, CSharpParser.INT, CSharpParser.INTO, CSharpParser.JOIN, CSharpParser.LET, CSharpParser.LONG, CSharpParser.NAMEOF, CSharpParser.NEW, CSharpParser.NULL, CSharpParser.OBJECT, CSharpParser.ON, CSharpParser.ORDERBY, CSharpParser.PARTIAL, CSharpParser.REF, CSharpParser.REMOVE, CSharpParser.SBYTE, CSharpParser.SELECT, CSharpParser.SET, CSharpParser.SHORT, CSharpParser.SIZEOF, CSharpParser.STRING, CSharpParser.THIS, CSharpParser.TRUE, CSharpParser.TYPEOF, CSharpParser.UINT, CSharpParser.ULONG, CSharpParser.UNCHECKED, CSharpParser.UNMANAGED, CSharpParser.USHORT, CSharpParser.VAR, CSharpParser.WHEN, CSharpParser.WHERE, CSharpParser.YIELD, CSharpParser.IDENTIFIER, CSharpParser.LITERAL_ACCESS, CSharpParser.INTEGER_LITERAL, CSharpParser.HEX_INTEGER_LITERAL, CSharpParser.BIN_INTEGER_LITERAL, CSharpParser.REAL_LITERAL, CSharpParser.CHARACTER_LITERAL, CSharpParser.REGULAR_STRING, CSharpParser.VERBATIUM_STRING, CSharpParser.INTERPOLATED_REGULAR_STRING_START, CSharpParser.INTERPOLATED_VERBATIUM_STRING_START, CSharpParser.OPEN_PARENS, CSharpParser.PLUS, CSharpParser.MINUS, CSharpParser.STAR, CSharpParser.AMP, CSharpParser.CARET, CSharpParser.BANG, CSharpParser.TILDE, CSharpParser.OP_INC, CSharpParser.OP_DEC, CSharpParser.OP_RANGE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2297
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,288,self._ctx)
                if la_ == 1:
                    self.state = 2296
                    self.match(CSharpParser.AMP)


                self.state = 2299
                self.expression()
                pass
            elif token in [CSharpParser.STACKALLOC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2300
                self.stackalloc_initializer()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fixed_size_buffer_declaratorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def OPEN_BRACKET(self):
            return self.getToken(CSharpParser.OPEN_BRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def CLOSE_BRACKET(self):
            return self.getToken(CSharpParser.CLOSE_BRACKET, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_fixed_size_buffer_declarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFixed_size_buffer_declarator" ):
                listener.enterFixed_size_buffer_declarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFixed_size_buffer_declarator" ):
                listener.exitFixed_size_buffer_declarator(self)




    def fixed_size_buffer_declarator(self):

        localctx = CSharpParser.Fixed_size_buffer_declaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 370, self.RULE_fixed_size_buffer_declarator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2303
            self.identifier()
            self.state = 2304
            self.match(CSharpParser.OPEN_BRACKET)
            self.state = 2305
            self.expression()
            self.state = 2306
            self.match(CSharpParser.CLOSE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stackalloc_initializerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STACKALLOC(self):
            return self.getToken(CSharpParser.STACKALLOC, 0)

        def type_(self):
            return self.getTypedRuleContext(CSharpParser.Type_Context,0)


        def OPEN_BRACKET(self):
            return self.getToken(CSharpParser.OPEN_BRACKET, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CSharpParser.ExpressionContext,i)


        def CLOSE_BRACKET(self):
            return self.getToken(CSharpParser.CLOSE_BRACKET, 0)

        def OPEN_BRACE(self):
            return self.getToken(CSharpParser.OPEN_BRACE, 0)

        def CLOSE_BRACE(self):
            return self.getToken(CSharpParser.CLOSE_BRACE, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_stackalloc_initializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStackalloc_initializer" ):
                listener.enterStackalloc_initializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStackalloc_initializer" ):
                listener.exitStackalloc_initializer(self)




    def stackalloc_initializer(self):

        localctx = CSharpParser.Stackalloc_initializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 372, self.RULE_stackalloc_initializer)
        self._la = 0 # Token type
        try:
            self.state = 2337
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,294,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2308
                self.match(CSharpParser.STACKALLOC)
                self.state = 2309
                self.type_()
                self.state = 2310
                self.match(CSharpParser.OPEN_BRACKET)
                self.state = 2311
                self.expression()
                self.state = 2312
                self.match(CSharpParser.CLOSE_BRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2314
                self.match(CSharpParser.STACKALLOC)
                self.state = 2316
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BOOL) | (1 << CSharpParser.BY) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.INT) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.LONG) | (1 << CSharpParser.NAMEOF))) != 0) or ((((_la - 67)) & ~0x3f) == 0 and ((1 << (_la - 67)) & ((1 << (CSharpParser.OBJECT - 67)) | (1 << (CSharpParser.ON - 67)) | (1 << (CSharpParser.ORDERBY - 67)) | (1 << (CSharpParser.PARTIAL - 67)) | (1 << (CSharpParser.REMOVE - 67)) | (1 << (CSharpParser.SBYTE - 67)) | (1 << (CSharpParser.SELECT - 67)) | (1 << (CSharpParser.SET - 67)) | (1 << (CSharpParser.SHORT - 67)) | (1 << (CSharpParser.STRING - 67)) | (1 << (CSharpParser.UINT - 67)) | (1 << (CSharpParser.ULONG - 67)) | (1 << (CSharpParser.UNMANAGED - 67)) | (1 << (CSharpParser.USHORT - 67)) | (1 << (CSharpParser.VAR - 67)) | (1 << (CSharpParser.VOID - 67)) | (1 << (CSharpParser.WHEN - 67)) | (1 << (CSharpParser.WHERE - 67)) | (1 << (CSharpParser.YIELD - 67)) | (1 << (CSharpParser.IDENTIFIER - 67)) | (1 << (CSharpParser.OPEN_PARENS - 67)))) != 0):
                    self.state = 2315
                    self.type_()


                self.state = 2318
                self.match(CSharpParser.OPEN_BRACKET)
                self.state = 2320
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BASE) | (1 << CSharpParser.BOOL) | (1 << CSharpParser.BY) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.CHECKED) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DEFAULT) | (1 << CSharpParser.DELEGATE) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FALSE) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.INT) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.LONG) | (1 << CSharpParser.NAMEOF))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (CSharpParser.NEW - 65)) | (1 << (CSharpParser.NULL - 65)) | (1 << (CSharpParser.OBJECT - 65)) | (1 << (CSharpParser.ON - 65)) | (1 << (CSharpParser.ORDERBY - 65)) | (1 << (CSharpParser.PARTIAL - 65)) | (1 << (CSharpParser.REF - 65)) | (1 << (CSharpParser.REMOVE - 65)) | (1 << (CSharpParser.SBYTE - 65)) | (1 << (CSharpParser.SELECT - 65)) | (1 << (CSharpParser.SET - 65)) | (1 << (CSharpParser.SHORT - 65)) | (1 << (CSharpParser.SIZEOF - 65)) | (1 << (CSharpParser.STRING - 65)) | (1 << (CSharpParser.THIS - 65)) | (1 << (CSharpParser.TRUE - 65)) | (1 << (CSharpParser.TYPEOF - 65)) | (1 << (CSharpParser.UINT - 65)) | (1 << (CSharpParser.ULONG - 65)) | (1 << (CSharpParser.UNCHECKED - 65)) | (1 << (CSharpParser.UNMANAGED - 65)) | (1 << (CSharpParser.USHORT - 65)) | (1 << (CSharpParser.VAR - 65)) | (1 << (CSharpParser.WHEN - 65)) | (1 << (CSharpParser.WHERE - 65)) | (1 << (CSharpParser.YIELD - 65)) | (1 << (CSharpParser.IDENTIFIER - 65)) | (1 << (CSharpParser.LITERAL_ACCESS - 65)) | (1 << (CSharpParser.INTEGER_LITERAL - 65)) | (1 << (CSharpParser.HEX_INTEGER_LITERAL - 65)) | (1 << (CSharpParser.BIN_INTEGER_LITERAL - 65)) | (1 << (CSharpParser.REAL_LITERAL - 65)) | (1 << (CSharpParser.CHARACTER_LITERAL - 65)) | (1 << (CSharpParser.REGULAR_STRING - 65)) | (1 << (CSharpParser.VERBATIUM_STRING - 65)) | (1 << (CSharpParser.INTERPOLATED_REGULAR_STRING_START - 65)) | (1 << (CSharpParser.INTERPOLATED_VERBATIUM_STRING_START - 65)) | (1 << (CSharpParser.OPEN_PARENS - 65)))) != 0) or ((((_la - 134)) & ~0x3f) == 0 and ((1 << (_la - 134)) & ((1 << (CSharpParser.PLUS - 134)) | (1 << (CSharpParser.MINUS - 134)) | (1 << (CSharpParser.STAR - 134)) | (1 << (CSharpParser.AMP - 134)) | (1 << (CSharpParser.CARET - 134)) | (1 << (CSharpParser.BANG - 134)) | (1 << (CSharpParser.TILDE - 134)) | (1 << (CSharpParser.OP_INC - 134)) | (1 << (CSharpParser.OP_DEC - 134)) | (1 << (CSharpParser.OP_RANGE - 134)))) != 0):
                    self.state = 2319
                    self.expression()


                self.state = 2322
                self.match(CSharpParser.CLOSE_BRACKET)
                self.state = 2323
                self.match(CSharpParser.OPEN_BRACE)
                self.state = 2324
                self.expression()
                self.state = 2329
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,292,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 2325
                        self.match(CSharpParser.COMMA)
                        self.state = 2326
                        self.expression() 
                    self.state = 2331
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,292,self._ctx)

                self.state = 2333
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.COMMA:
                    self.state = 2332
                    self.match(CSharpParser.COMMA)


                self.state = 2335
                self.match(CSharpParser.CLOSE_BRACE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Right_arrowContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.first = None # Token
            self.second = None # Token

        def ASSIGNMENT(self):
            return self.getToken(CSharpParser.ASSIGNMENT, 0)

        def GT(self):
            return self.getToken(CSharpParser.GT, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_right_arrow

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRight_arrow" ):
                listener.enterRight_arrow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRight_arrow" ):
                listener.exitRight_arrow(self)




    def right_arrow(self):

        localctx = CSharpParser.Right_arrowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 374, self.RULE_right_arrow)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2339
            localctx.first = self.match(CSharpParser.ASSIGNMENT)
            self.state = 2340
            localctx.second = self.match(CSharpParser.GT)
            self.state = 2341
            if not (0 if localctx.first is None else localctx.first.tokenIndex) + 1 == (0 if localctx.second is None else localctx.second.tokenIndex):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$first.index + 1 == $second.index")
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Right_shiftContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.first = None # Token
            self.second = None # Token

        def GT(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.GT)
            else:
                return self.getToken(CSharpParser.GT, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_right_shift

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRight_shift" ):
                listener.enterRight_shift(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRight_shift" ):
                listener.exitRight_shift(self)




    def right_shift(self):

        localctx = CSharpParser.Right_shiftContext(self, self._ctx, self.state)
        self.enterRule(localctx, 376, self.RULE_right_shift)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2343
            localctx.first = self.match(CSharpParser.GT)
            self.state = 2344
            localctx.second = self.match(CSharpParser.GT)
            self.state = 2345
            if not (0 if localctx.first is None else localctx.first.tokenIndex) + 1 == (0 if localctx.second is None else localctx.second.tokenIndex):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$first.index + 1 == $second.index")
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Right_shift_assignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.first = None # Token
            self.second = None # Token

        def GT(self):
            return self.getToken(CSharpParser.GT, 0)

        def OP_GE(self):
            return self.getToken(CSharpParser.OP_GE, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_right_shift_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRight_shift_assignment" ):
                listener.enterRight_shift_assignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRight_shift_assignment" ):
                listener.exitRight_shift_assignment(self)




    def right_shift_assignment(self):

        localctx = CSharpParser.Right_shift_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 378, self.RULE_right_shift_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2347
            localctx.first = self.match(CSharpParser.GT)
            self.state = 2348
            localctx.second = self.match(CSharpParser.OP_GE)
            self.state = 2349
            if not (0 if localctx.first is None else localctx.first.tokenIndex) + 1 == (0 if localctx.second is None else localctx.second.tokenIndex):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$first.index + 1 == $second.index")
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boolean_literal(self):
            return self.getTypedRuleContext(CSharpParser.Boolean_literalContext,0)


        def string_literal(self):
            return self.getTypedRuleContext(CSharpParser.String_literalContext,0)


        def INTEGER_LITERAL(self):
            return self.getToken(CSharpParser.INTEGER_LITERAL, 0)

        def HEX_INTEGER_LITERAL(self):
            return self.getToken(CSharpParser.HEX_INTEGER_LITERAL, 0)

        def BIN_INTEGER_LITERAL(self):
            return self.getToken(CSharpParser.BIN_INTEGER_LITERAL, 0)

        def REAL_LITERAL(self):
            return self.getToken(CSharpParser.REAL_LITERAL, 0)

        def CHARACTER_LITERAL(self):
            return self.getToken(CSharpParser.CHARACTER_LITERAL, 0)

        def NULL(self):
            return self.getToken(CSharpParser.NULL, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = CSharpParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 380, self.RULE_literal)
        try:
            self.state = 2359
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.FALSE, CSharpParser.TRUE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2351
                self.boolean_literal()
                pass
            elif token in [CSharpParser.REGULAR_STRING, CSharpParser.VERBATIUM_STRING, CSharpParser.INTERPOLATED_REGULAR_STRING_START, CSharpParser.INTERPOLATED_VERBATIUM_STRING_START]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2352
                self.string_literal()
                pass
            elif token in [CSharpParser.INTEGER_LITERAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 2353
                self.match(CSharpParser.INTEGER_LITERAL)
                pass
            elif token in [CSharpParser.HEX_INTEGER_LITERAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 2354
                self.match(CSharpParser.HEX_INTEGER_LITERAL)
                pass
            elif token in [CSharpParser.BIN_INTEGER_LITERAL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 2355
                self.match(CSharpParser.BIN_INTEGER_LITERAL)
                pass
            elif token in [CSharpParser.REAL_LITERAL]:
                self.enterOuterAlt(localctx, 6)
                self.state = 2356
                self.match(CSharpParser.REAL_LITERAL)
                pass
            elif token in [CSharpParser.CHARACTER_LITERAL]:
                self.enterOuterAlt(localctx, 7)
                self.state = 2357
                self.match(CSharpParser.CHARACTER_LITERAL)
                pass
            elif token in [CSharpParser.NULL]:
                self.enterOuterAlt(localctx, 8)
                self.state = 2358
                self.match(CSharpParser.NULL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Boolean_literalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(CSharpParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(CSharpParser.FALSE, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_boolean_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolean_literal" ):
                listener.enterBoolean_literal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolean_literal" ):
                listener.exitBoolean_literal(self)




    def boolean_literal(self):

        localctx = CSharpParser.Boolean_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 382, self.RULE_boolean_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2361
            _la = self._input.LA(1)
            if not(_la==CSharpParser.FALSE or _la==CSharpParser.TRUE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_literalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interpolated_regular_string(self):
            return self.getTypedRuleContext(CSharpParser.Interpolated_regular_stringContext,0)


        def interpolated_verbatium_string(self):
            return self.getTypedRuleContext(CSharpParser.Interpolated_verbatium_stringContext,0)


        def REGULAR_STRING(self):
            return self.getToken(CSharpParser.REGULAR_STRING, 0)

        def VERBATIUM_STRING(self):
            return self.getToken(CSharpParser.VERBATIUM_STRING, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_string_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString_literal" ):
                listener.enterString_literal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString_literal" ):
                listener.exitString_literal(self)




    def string_literal(self):

        localctx = CSharpParser.String_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 384, self.RULE_string_literal)
        try:
            self.state = 2367
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.INTERPOLATED_REGULAR_STRING_START]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2363
                self.interpolated_regular_string()
                pass
            elif token in [CSharpParser.INTERPOLATED_VERBATIUM_STRING_START]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2364
                self.interpolated_verbatium_string()
                pass
            elif token in [CSharpParser.REGULAR_STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 2365
                self.match(CSharpParser.REGULAR_STRING)
                pass
            elif token in [CSharpParser.VERBATIUM_STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 2366
                self.match(CSharpParser.VERBATIUM_STRING)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interpolated_regular_stringContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTERPOLATED_REGULAR_STRING_START(self):
            return self.getToken(CSharpParser.INTERPOLATED_REGULAR_STRING_START, 0)

        def DOUBLE_QUOTE_INSIDE(self):
            return self.getToken(CSharpParser.DOUBLE_QUOTE_INSIDE, 0)

        def interpolated_regular_string_part(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Interpolated_regular_string_partContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Interpolated_regular_string_partContext,i)


        def getRuleIndex(self):
            return CSharpParser.RULE_interpolated_regular_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterpolated_regular_string" ):
                listener.enterInterpolated_regular_string(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterpolated_regular_string" ):
                listener.exitInterpolated_regular_string(self)




    def interpolated_regular_string(self):

        localctx = CSharpParser.Interpolated_regular_stringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 386, self.RULE_interpolated_regular_string)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2369
            self.match(CSharpParser.INTERPOLATED_REGULAR_STRING_START)
            self.state = 2373
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BASE) | (1 << CSharpParser.BOOL) | (1 << CSharpParser.BY) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.CHECKED) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DEFAULT) | (1 << CSharpParser.DELEGATE) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FALSE) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.INT) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.LONG) | (1 << CSharpParser.NAMEOF))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (CSharpParser.NEW - 65)) | (1 << (CSharpParser.NULL - 65)) | (1 << (CSharpParser.OBJECT - 65)) | (1 << (CSharpParser.ON - 65)) | (1 << (CSharpParser.ORDERBY - 65)) | (1 << (CSharpParser.PARTIAL - 65)) | (1 << (CSharpParser.REF - 65)) | (1 << (CSharpParser.REMOVE - 65)) | (1 << (CSharpParser.SBYTE - 65)) | (1 << (CSharpParser.SELECT - 65)) | (1 << (CSharpParser.SET - 65)) | (1 << (CSharpParser.SHORT - 65)) | (1 << (CSharpParser.SIZEOF - 65)) | (1 << (CSharpParser.STRING - 65)) | (1 << (CSharpParser.THIS - 65)) | (1 << (CSharpParser.TRUE - 65)) | (1 << (CSharpParser.TYPEOF - 65)) | (1 << (CSharpParser.UINT - 65)) | (1 << (CSharpParser.ULONG - 65)) | (1 << (CSharpParser.UNCHECKED - 65)) | (1 << (CSharpParser.UNMANAGED - 65)) | (1 << (CSharpParser.USHORT - 65)) | (1 << (CSharpParser.VAR - 65)) | (1 << (CSharpParser.WHEN - 65)) | (1 << (CSharpParser.WHERE - 65)) | (1 << (CSharpParser.YIELD - 65)) | (1 << (CSharpParser.IDENTIFIER - 65)) | (1 << (CSharpParser.LITERAL_ACCESS - 65)) | (1 << (CSharpParser.INTEGER_LITERAL - 65)) | (1 << (CSharpParser.HEX_INTEGER_LITERAL - 65)) | (1 << (CSharpParser.BIN_INTEGER_LITERAL - 65)) | (1 << (CSharpParser.REAL_LITERAL - 65)) | (1 << (CSharpParser.CHARACTER_LITERAL - 65)) | (1 << (CSharpParser.REGULAR_STRING - 65)) | (1 << (CSharpParser.VERBATIUM_STRING - 65)) | (1 << (CSharpParser.INTERPOLATED_REGULAR_STRING_START - 65)) | (1 << (CSharpParser.INTERPOLATED_VERBATIUM_STRING_START - 65)) | (1 << (CSharpParser.OPEN_PARENS - 65)))) != 0) or ((((_la - 134)) & ~0x3f) == 0 and ((1 << (_la - 134)) & ((1 << (CSharpParser.PLUS - 134)) | (1 << (CSharpParser.MINUS - 134)) | (1 << (CSharpParser.STAR - 134)) | (1 << (CSharpParser.AMP - 134)) | (1 << (CSharpParser.CARET - 134)) | (1 << (CSharpParser.BANG - 134)) | (1 << (CSharpParser.TILDE - 134)) | (1 << (CSharpParser.OP_INC - 134)) | (1 << (CSharpParser.OP_DEC - 134)) | (1 << (CSharpParser.OP_RANGE - 134)) | (1 << (CSharpParser.DOUBLE_CURLY_INSIDE - 134)) | (1 << (CSharpParser.REGULAR_CHAR_INSIDE - 134)) | (1 << (CSharpParser.REGULAR_STRING_INSIDE - 134)))) != 0):
                self.state = 2370
                self.interpolated_regular_string_part()
                self.state = 2375
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2376
            self.match(CSharpParser.DOUBLE_QUOTE_INSIDE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interpolated_verbatium_stringContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTERPOLATED_VERBATIUM_STRING_START(self):
            return self.getToken(CSharpParser.INTERPOLATED_VERBATIUM_STRING_START, 0)

        def DOUBLE_QUOTE_INSIDE(self):
            return self.getToken(CSharpParser.DOUBLE_QUOTE_INSIDE, 0)

        def interpolated_verbatium_string_part(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Interpolated_verbatium_string_partContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Interpolated_verbatium_string_partContext,i)


        def getRuleIndex(self):
            return CSharpParser.RULE_interpolated_verbatium_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterpolated_verbatium_string" ):
                listener.enterInterpolated_verbatium_string(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterpolated_verbatium_string" ):
                listener.exitInterpolated_verbatium_string(self)




    def interpolated_verbatium_string(self):

        localctx = CSharpParser.Interpolated_verbatium_stringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 388, self.RULE_interpolated_verbatium_string)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2378
            self.match(CSharpParser.INTERPOLATED_VERBATIUM_STRING_START)
            self.state = 2382
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BASE) | (1 << CSharpParser.BOOL) | (1 << CSharpParser.BY) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.CHECKED) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DEFAULT) | (1 << CSharpParser.DELEGATE) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FALSE) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.INT) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.LONG) | (1 << CSharpParser.NAMEOF))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (CSharpParser.NEW - 65)) | (1 << (CSharpParser.NULL - 65)) | (1 << (CSharpParser.OBJECT - 65)) | (1 << (CSharpParser.ON - 65)) | (1 << (CSharpParser.ORDERBY - 65)) | (1 << (CSharpParser.PARTIAL - 65)) | (1 << (CSharpParser.REF - 65)) | (1 << (CSharpParser.REMOVE - 65)) | (1 << (CSharpParser.SBYTE - 65)) | (1 << (CSharpParser.SELECT - 65)) | (1 << (CSharpParser.SET - 65)) | (1 << (CSharpParser.SHORT - 65)) | (1 << (CSharpParser.SIZEOF - 65)) | (1 << (CSharpParser.STRING - 65)) | (1 << (CSharpParser.THIS - 65)) | (1 << (CSharpParser.TRUE - 65)) | (1 << (CSharpParser.TYPEOF - 65)) | (1 << (CSharpParser.UINT - 65)) | (1 << (CSharpParser.ULONG - 65)) | (1 << (CSharpParser.UNCHECKED - 65)) | (1 << (CSharpParser.UNMANAGED - 65)) | (1 << (CSharpParser.USHORT - 65)) | (1 << (CSharpParser.VAR - 65)) | (1 << (CSharpParser.WHEN - 65)) | (1 << (CSharpParser.WHERE - 65)) | (1 << (CSharpParser.YIELD - 65)) | (1 << (CSharpParser.IDENTIFIER - 65)) | (1 << (CSharpParser.LITERAL_ACCESS - 65)) | (1 << (CSharpParser.INTEGER_LITERAL - 65)) | (1 << (CSharpParser.HEX_INTEGER_LITERAL - 65)) | (1 << (CSharpParser.BIN_INTEGER_LITERAL - 65)) | (1 << (CSharpParser.REAL_LITERAL - 65)) | (1 << (CSharpParser.CHARACTER_LITERAL - 65)) | (1 << (CSharpParser.REGULAR_STRING - 65)) | (1 << (CSharpParser.VERBATIUM_STRING - 65)) | (1 << (CSharpParser.INTERPOLATED_REGULAR_STRING_START - 65)) | (1 << (CSharpParser.INTERPOLATED_VERBATIUM_STRING_START - 65)) | (1 << (CSharpParser.OPEN_PARENS - 65)))) != 0) or ((((_la - 134)) & ~0x3f) == 0 and ((1 << (_la - 134)) & ((1 << (CSharpParser.PLUS - 134)) | (1 << (CSharpParser.MINUS - 134)) | (1 << (CSharpParser.STAR - 134)) | (1 << (CSharpParser.AMP - 134)) | (1 << (CSharpParser.CARET - 134)) | (1 << (CSharpParser.BANG - 134)) | (1 << (CSharpParser.TILDE - 134)) | (1 << (CSharpParser.OP_INC - 134)) | (1 << (CSharpParser.OP_DEC - 134)) | (1 << (CSharpParser.OP_RANGE - 134)) | (1 << (CSharpParser.DOUBLE_CURLY_INSIDE - 134)) | (1 << (CSharpParser.VERBATIUM_DOUBLE_QUOTE_INSIDE - 134)) | (1 << (CSharpParser.VERBATIUM_INSIDE_STRING - 134)))) != 0):
                self.state = 2379
                self.interpolated_verbatium_string_part()
                self.state = 2384
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2385
            self.match(CSharpParser.DOUBLE_QUOTE_INSIDE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interpolated_regular_string_partContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interpolated_string_expression(self):
            return self.getTypedRuleContext(CSharpParser.Interpolated_string_expressionContext,0)


        def DOUBLE_CURLY_INSIDE(self):
            return self.getToken(CSharpParser.DOUBLE_CURLY_INSIDE, 0)

        def REGULAR_CHAR_INSIDE(self):
            return self.getToken(CSharpParser.REGULAR_CHAR_INSIDE, 0)

        def REGULAR_STRING_INSIDE(self):
            return self.getToken(CSharpParser.REGULAR_STRING_INSIDE, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_interpolated_regular_string_part

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterpolated_regular_string_part" ):
                listener.enterInterpolated_regular_string_part(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterpolated_regular_string_part" ):
                listener.exitInterpolated_regular_string_part(self)




    def interpolated_regular_string_part(self):

        localctx = CSharpParser.Interpolated_regular_string_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 390, self.RULE_interpolated_regular_string_part)
        try:
            self.state = 2391
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.ADD, CSharpParser.ALIAS, CSharpParser.ARGLIST, CSharpParser.ASCENDING, CSharpParser.ASYNC, CSharpParser.AWAIT, CSharpParser.BASE, CSharpParser.BOOL, CSharpParser.BY, CSharpParser.BYTE, CSharpParser.CHAR, CSharpParser.CHECKED, CSharpParser.DECIMAL, CSharpParser.DEFAULT, CSharpParser.DELEGATE, CSharpParser.DESCENDING, CSharpParser.DOUBLE, CSharpParser.DYNAMIC, CSharpParser.EQUALS, CSharpParser.FALSE, CSharpParser.FLOAT, CSharpParser.FROM, CSharpParser.GET, CSharpParser.GROUP, CSharpParser.INT, CSharpParser.INTO, CSharpParser.JOIN, CSharpParser.LET, CSharpParser.LONG, CSharpParser.NAMEOF, CSharpParser.NEW, CSharpParser.NULL, CSharpParser.OBJECT, CSharpParser.ON, CSharpParser.ORDERBY, CSharpParser.PARTIAL, CSharpParser.REF, CSharpParser.REMOVE, CSharpParser.SBYTE, CSharpParser.SELECT, CSharpParser.SET, CSharpParser.SHORT, CSharpParser.SIZEOF, CSharpParser.STRING, CSharpParser.THIS, CSharpParser.TRUE, CSharpParser.TYPEOF, CSharpParser.UINT, CSharpParser.ULONG, CSharpParser.UNCHECKED, CSharpParser.UNMANAGED, CSharpParser.USHORT, CSharpParser.VAR, CSharpParser.WHEN, CSharpParser.WHERE, CSharpParser.YIELD, CSharpParser.IDENTIFIER, CSharpParser.LITERAL_ACCESS, CSharpParser.INTEGER_LITERAL, CSharpParser.HEX_INTEGER_LITERAL, CSharpParser.BIN_INTEGER_LITERAL, CSharpParser.REAL_LITERAL, CSharpParser.CHARACTER_LITERAL, CSharpParser.REGULAR_STRING, CSharpParser.VERBATIUM_STRING, CSharpParser.INTERPOLATED_REGULAR_STRING_START, CSharpParser.INTERPOLATED_VERBATIUM_STRING_START, CSharpParser.OPEN_PARENS, CSharpParser.PLUS, CSharpParser.MINUS, CSharpParser.STAR, CSharpParser.AMP, CSharpParser.CARET, CSharpParser.BANG, CSharpParser.TILDE, CSharpParser.OP_INC, CSharpParser.OP_DEC, CSharpParser.OP_RANGE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2387
                self.interpolated_string_expression()
                pass
            elif token in [CSharpParser.DOUBLE_CURLY_INSIDE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2388
                self.match(CSharpParser.DOUBLE_CURLY_INSIDE)
                pass
            elif token in [CSharpParser.REGULAR_CHAR_INSIDE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 2389
                self.match(CSharpParser.REGULAR_CHAR_INSIDE)
                pass
            elif token in [CSharpParser.REGULAR_STRING_INSIDE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 2390
                self.match(CSharpParser.REGULAR_STRING_INSIDE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interpolated_verbatium_string_partContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interpolated_string_expression(self):
            return self.getTypedRuleContext(CSharpParser.Interpolated_string_expressionContext,0)


        def DOUBLE_CURLY_INSIDE(self):
            return self.getToken(CSharpParser.DOUBLE_CURLY_INSIDE, 0)

        def VERBATIUM_DOUBLE_QUOTE_INSIDE(self):
            return self.getToken(CSharpParser.VERBATIUM_DOUBLE_QUOTE_INSIDE, 0)

        def VERBATIUM_INSIDE_STRING(self):
            return self.getToken(CSharpParser.VERBATIUM_INSIDE_STRING, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_interpolated_verbatium_string_part

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterpolated_verbatium_string_part" ):
                listener.enterInterpolated_verbatium_string_part(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterpolated_verbatium_string_part" ):
                listener.exitInterpolated_verbatium_string_part(self)




    def interpolated_verbatium_string_part(self):

        localctx = CSharpParser.Interpolated_verbatium_string_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 392, self.RULE_interpolated_verbatium_string_part)
        try:
            self.state = 2397
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.ADD, CSharpParser.ALIAS, CSharpParser.ARGLIST, CSharpParser.ASCENDING, CSharpParser.ASYNC, CSharpParser.AWAIT, CSharpParser.BASE, CSharpParser.BOOL, CSharpParser.BY, CSharpParser.BYTE, CSharpParser.CHAR, CSharpParser.CHECKED, CSharpParser.DECIMAL, CSharpParser.DEFAULT, CSharpParser.DELEGATE, CSharpParser.DESCENDING, CSharpParser.DOUBLE, CSharpParser.DYNAMIC, CSharpParser.EQUALS, CSharpParser.FALSE, CSharpParser.FLOAT, CSharpParser.FROM, CSharpParser.GET, CSharpParser.GROUP, CSharpParser.INT, CSharpParser.INTO, CSharpParser.JOIN, CSharpParser.LET, CSharpParser.LONG, CSharpParser.NAMEOF, CSharpParser.NEW, CSharpParser.NULL, CSharpParser.OBJECT, CSharpParser.ON, CSharpParser.ORDERBY, CSharpParser.PARTIAL, CSharpParser.REF, CSharpParser.REMOVE, CSharpParser.SBYTE, CSharpParser.SELECT, CSharpParser.SET, CSharpParser.SHORT, CSharpParser.SIZEOF, CSharpParser.STRING, CSharpParser.THIS, CSharpParser.TRUE, CSharpParser.TYPEOF, CSharpParser.UINT, CSharpParser.ULONG, CSharpParser.UNCHECKED, CSharpParser.UNMANAGED, CSharpParser.USHORT, CSharpParser.VAR, CSharpParser.WHEN, CSharpParser.WHERE, CSharpParser.YIELD, CSharpParser.IDENTIFIER, CSharpParser.LITERAL_ACCESS, CSharpParser.INTEGER_LITERAL, CSharpParser.HEX_INTEGER_LITERAL, CSharpParser.BIN_INTEGER_LITERAL, CSharpParser.REAL_LITERAL, CSharpParser.CHARACTER_LITERAL, CSharpParser.REGULAR_STRING, CSharpParser.VERBATIUM_STRING, CSharpParser.INTERPOLATED_REGULAR_STRING_START, CSharpParser.INTERPOLATED_VERBATIUM_STRING_START, CSharpParser.OPEN_PARENS, CSharpParser.PLUS, CSharpParser.MINUS, CSharpParser.STAR, CSharpParser.AMP, CSharpParser.CARET, CSharpParser.BANG, CSharpParser.TILDE, CSharpParser.OP_INC, CSharpParser.OP_DEC, CSharpParser.OP_RANGE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2393
                self.interpolated_string_expression()
                pass
            elif token in [CSharpParser.DOUBLE_CURLY_INSIDE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2394
                self.match(CSharpParser.DOUBLE_CURLY_INSIDE)
                pass
            elif token in [CSharpParser.VERBATIUM_DOUBLE_QUOTE_INSIDE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 2395
                self.match(CSharpParser.VERBATIUM_DOUBLE_QUOTE_INSIDE)
                pass
            elif token in [CSharpParser.VERBATIUM_INSIDE_STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 2396
                self.match(CSharpParser.VERBATIUM_INSIDE_STRING)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interpolated_string_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CSharpParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.COMMA)
            else:
                return self.getToken(CSharpParser.COMMA, i)

        def COLON(self):
            return self.getToken(CSharpParser.COLON, 0)

        def FORMAT_STRING(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.FORMAT_STRING)
            else:
                return self.getToken(CSharpParser.FORMAT_STRING, i)

        def getRuleIndex(self):
            return CSharpParser.RULE_interpolated_string_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterpolated_string_expression" ):
                listener.enterInterpolated_string_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterpolated_string_expression" ):
                listener.exitInterpolated_string_expression(self)




    def interpolated_string_expression(self):

        localctx = CSharpParser.Interpolated_string_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 394, self.RULE_interpolated_string_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2399
            self.expression()
            self.state = 2404
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSharpParser.COMMA:
                self.state = 2400
                self.match(CSharpParser.COMMA)
                self.state = 2401
                self.expression()
                self.state = 2406
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2413
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.COLON:
                self.state = 2407
                self.match(CSharpParser.COLON)
                self.state = 2409 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 2408
                    self.match(CSharpParser.FORMAT_STRING)
                    self.state = 2411 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==CSharpParser.FORMAT_STRING):
                        break



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeywordContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ABSTRACT(self):
            return self.getToken(CSharpParser.ABSTRACT, 0)

        def AS(self):
            return self.getToken(CSharpParser.AS, 0)

        def BASE(self):
            return self.getToken(CSharpParser.BASE, 0)

        def BOOL(self):
            return self.getToken(CSharpParser.BOOL, 0)

        def BREAK(self):
            return self.getToken(CSharpParser.BREAK, 0)

        def BYTE(self):
            return self.getToken(CSharpParser.BYTE, 0)

        def CASE(self):
            return self.getToken(CSharpParser.CASE, 0)

        def CATCH(self):
            return self.getToken(CSharpParser.CATCH, 0)

        def CHAR(self):
            return self.getToken(CSharpParser.CHAR, 0)

        def CHECKED(self):
            return self.getToken(CSharpParser.CHECKED, 0)

        def CLASS(self):
            return self.getToken(CSharpParser.CLASS, 0)

        def CONST(self):
            return self.getToken(CSharpParser.CONST, 0)

        def CONTINUE(self):
            return self.getToken(CSharpParser.CONTINUE, 0)

        def DECIMAL(self):
            return self.getToken(CSharpParser.DECIMAL, 0)

        def DEFAULT(self):
            return self.getToken(CSharpParser.DEFAULT, 0)

        def DELEGATE(self):
            return self.getToken(CSharpParser.DELEGATE, 0)

        def DO(self):
            return self.getToken(CSharpParser.DO, 0)

        def DOUBLE(self):
            return self.getToken(CSharpParser.DOUBLE, 0)

        def ELSE(self):
            return self.getToken(CSharpParser.ELSE, 0)

        def ENUM(self):
            return self.getToken(CSharpParser.ENUM, 0)

        def EVENT(self):
            return self.getToken(CSharpParser.EVENT, 0)

        def EXPLICIT(self):
            return self.getToken(CSharpParser.EXPLICIT, 0)

        def EXTERN(self):
            return self.getToken(CSharpParser.EXTERN, 0)

        def FALSE(self):
            return self.getToken(CSharpParser.FALSE, 0)

        def FINALLY(self):
            return self.getToken(CSharpParser.FINALLY, 0)

        def FIXED(self):
            return self.getToken(CSharpParser.FIXED, 0)

        def FLOAT(self):
            return self.getToken(CSharpParser.FLOAT, 0)

        def FOR(self):
            return self.getToken(CSharpParser.FOR, 0)

        def FOREACH(self):
            return self.getToken(CSharpParser.FOREACH, 0)

        def GOTO(self):
            return self.getToken(CSharpParser.GOTO, 0)

        def IF(self):
            return self.getToken(CSharpParser.IF, 0)

        def IMPLICIT(self):
            return self.getToken(CSharpParser.IMPLICIT, 0)

        def IN(self):
            return self.getToken(CSharpParser.IN, 0)

        def INT(self):
            return self.getToken(CSharpParser.INT, 0)

        def INTERFACE(self):
            return self.getToken(CSharpParser.INTERFACE, 0)

        def INTERNAL(self):
            return self.getToken(CSharpParser.INTERNAL, 0)

        def IS(self):
            return self.getToken(CSharpParser.IS, 0)

        def LOCK(self):
            return self.getToken(CSharpParser.LOCK, 0)

        def LONG(self):
            return self.getToken(CSharpParser.LONG, 0)

        def NAMESPACE(self):
            return self.getToken(CSharpParser.NAMESPACE, 0)

        def NEW(self):
            return self.getToken(CSharpParser.NEW, 0)

        def NULL(self):
            return self.getToken(CSharpParser.NULL, 0)

        def OBJECT(self):
            return self.getToken(CSharpParser.OBJECT, 0)

        def OPERATOR(self):
            return self.getToken(CSharpParser.OPERATOR, 0)

        def OUT(self):
            return self.getToken(CSharpParser.OUT, 0)

        def OVERRIDE(self):
            return self.getToken(CSharpParser.OVERRIDE, 0)

        def PARAMS(self):
            return self.getToken(CSharpParser.PARAMS, 0)

        def PRIVATE(self):
            return self.getToken(CSharpParser.PRIVATE, 0)

        def PROTECTED(self):
            return self.getToken(CSharpParser.PROTECTED, 0)

        def PUBLIC(self):
            return self.getToken(CSharpParser.PUBLIC, 0)

        def READONLY(self):
            return self.getToken(CSharpParser.READONLY, 0)

        def REF(self):
            return self.getToken(CSharpParser.REF, 0)

        def RETURN(self):
            return self.getToken(CSharpParser.RETURN, 0)

        def SBYTE(self):
            return self.getToken(CSharpParser.SBYTE, 0)

        def SEALED(self):
            return self.getToken(CSharpParser.SEALED, 0)

        def SHORT(self):
            return self.getToken(CSharpParser.SHORT, 0)

        def SIZEOF(self):
            return self.getToken(CSharpParser.SIZEOF, 0)

        def STACKALLOC(self):
            return self.getToken(CSharpParser.STACKALLOC, 0)

        def STATIC(self):
            return self.getToken(CSharpParser.STATIC, 0)

        def STRING(self):
            return self.getToken(CSharpParser.STRING, 0)

        def STRUCT(self):
            return self.getToken(CSharpParser.STRUCT, 0)

        def SWITCH(self):
            return self.getToken(CSharpParser.SWITCH, 0)

        def THIS(self):
            return self.getToken(CSharpParser.THIS, 0)

        def THROW(self):
            return self.getToken(CSharpParser.THROW, 0)

        def TRUE(self):
            return self.getToken(CSharpParser.TRUE, 0)

        def TRY(self):
            return self.getToken(CSharpParser.TRY, 0)

        def TYPEOF(self):
            return self.getToken(CSharpParser.TYPEOF, 0)

        def UINT(self):
            return self.getToken(CSharpParser.UINT, 0)

        def ULONG(self):
            return self.getToken(CSharpParser.ULONG, 0)

        def UNCHECKED(self):
            return self.getToken(CSharpParser.UNCHECKED, 0)

        def UNMANAGED(self):
            return self.getToken(CSharpParser.UNMANAGED, 0)

        def UNSAFE(self):
            return self.getToken(CSharpParser.UNSAFE, 0)

        def USHORT(self):
            return self.getToken(CSharpParser.USHORT, 0)

        def USING(self):
            return self.getToken(CSharpParser.USING, 0)

        def VIRTUAL(self):
            return self.getToken(CSharpParser.VIRTUAL, 0)

        def VOID(self):
            return self.getToken(CSharpParser.VOID, 0)

        def VOLATILE(self):
            return self.getToken(CSharpParser.VOLATILE, 0)

        def WHILE(self):
            return self.getToken(CSharpParser.WHILE, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_keyword

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeyword" ):
                listener.enterKeyword(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeyword" ):
                listener.exitKeyword(self)




    def keyword(self):

        localctx = CSharpParser.KeywordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 396, self.RULE_keyword)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2415
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ABSTRACT) | (1 << CSharpParser.AS) | (1 << CSharpParser.BASE) | (1 << CSharpParser.BOOL) | (1 << CSharpParser.BREAK) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CASE) | (1 << CSharpParser.CATCH) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.CHECKED) | (1 << CSharpParser.CLASS) | (1 << CSharpParser.CONST) | (1 << CSharpParser.CONTINUE) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DEFAULT) | (1 << CSharpParser.DELEGATE) | (1 << CSharpParser.DO) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.ELSE) | (1 << CSharpParser.ENUM) | (1 << CSharpParser.EVENT) | (1 << CSharpParser.EXPLICIT) | (1 << CSharpParser.EXTERN) | (1 << CSharpParser.FALSE) | (1 << CSharpParser.FINALLY) | (1 << CSharpParser.FIXED) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.FOR) | (1 << CSharpParser.FOREACH) | (1 << CSharpParser.GOTO) | (1 << CSharpParser.IF) | (1 << CSharpParser.IMPLICIT) | (1 << CSharpParser.IN) | (1 << CSharpParser.INT) | (1 << CSharpParser.INTERFACE) | (1 << CSharpParser.INTERNAL) | (1 << CSharpParser.IS) | (1 << CSharpParser.LOCK) | (1 << CSharpParser.LONG))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CSharpParser.NAMESPACE - 64)) | (1 << (CSharpParser.NEW - 64)) | (1 << (CSharpParser.NULL - 64)) | (1 << (CSharpParser.OBJECT - 64)) | (1 << (CSharpParser.OPERATOR - 64)) | (1 << (CSharpParser.OUT - 64)) | (1 << (CSharpParser.OVERRIDE - 64)) | (1 << (CSharpParser.PARAMS - 64)) | (1 << (CSharpParser.PRIVATE - 64)) | (1 << (CSharpParser.PROTECTED - 64)) | (1 << (CSharpParser.PUBLIC - 64)) | (1 << (CSharpParser.READONLY - 64)) | (1 << (CSharpParser.REF - 64)) | (1 << (CSharpParser.RETURN - 64)) | (1 << (CSharpParser.SBYTE - 64)) | (1 << (CSharpParser.SEALED - 64)) | (1 << (CSharpParser.SHORT - 64)) | (1 << (CSharpParser.SIZEOF - 64)) | (1 << (CSharpParser.STACKALLOC - 64)) | (1 << (CSharpParser.STATIC - 64)) | (1 << (CSharpParser.STRING - 64)) | (1 << (CSharpParser.STRUCT - 64)) | (1 << (CSharpParser.SWITCH - 64)) | (1 << (CSharpParser.THIS - 64)) | (1 << (CSharpParser.THROW - 64)) | (1 << (CSharpParser.TRUE - 64)) | (1 << (CSharpParser.TRY - 64)) | (1 << (CSharpParser.TYPEOF - 64)) | (1 << (CSharpParser.UINT - 64)) | (1 << (CSharpParser.ULONG - 64)) | (1 << (CSharpParser.UNCHECKED - 64)) | (1 << (CSharpParser.UNMANAGED - 64)) | (1 << (CSharpParser.UNSAFE - 64)) | (1 << (CSharpParser.USHORT - 64)) | (1 << (CSharpParser.USING - 64)) | (1 << (CSharpParser.VIRTUAL - 64)) | (1 << (CSharpParser.VOID - 64)) | (1 << (CSharpParser.VOLATILE - 64)) | (1 << (CSharpParser.WHILE - 64)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_definitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(CSharpParser.CLASS, 0)

        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def class_body(self):
            return self.getTypedRuleContext(CSharpParser.Class_bodyContext,0)


        def type_parameter_list(self):
            return self.getTypedRuleContext(CSharpParser.Type_parameter_listContext,0)


        def class_base(self):
            return self.getTypedRuleContext(CSharpParser.Class_baseContext,0)


        def type_parameter_constraints_clauses(self):
            return self.getTypedRuleContext(CSharpParser.Type_parameter_constraints_clausesContext,0)


        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_class_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_definition" ):
                listener.enterClass_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_definition" ):
                listener.exitClass_definition(self)




    def class_definition(self):

        localctx = CSharpParser.Class_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 398, self.RULE_class_definition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2417
            self.match(CSharpParser.CLASS)
            self.state = 2418
            self.identifier()
            self.state = 2420
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.LT:
                self.state = 2419
                self.type_parameter_list()


            self.state = 2423
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.COLON:
                self.state = 2422
                self.class_base()


            self.state = 2426
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.WHERE:
                self.state = 2425
                self.type_parameter_constraints_clauses()


            self.state = 2428
            self.class_body()
            self.state = 2430
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.SEMICOLON:
                self.state = 2429
                self.match(CSharpParser.SEMICOLON)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_definitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRUCT(self):
            return self.getToken(CSharpParser.STRUCT, 0)

        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def struct_body(self):
            return self.getTypedRuleContext(CSharpParser.Struct_bodyContext,0)


        def type_parameter_list(self):
            return self.getTypedRuleContext(CSharpParser.Type_parameter_listContext,0)


        def struct_interfaces(self):
            return self.getTypedRuleContext(CSharpParser.Struct_interfacesContext,0)


        def type_parameter_constraints_clauses(self):
            return self.getTypedRuleContext(CSharpParser.Type_parameter_constraints_clausesContext,0)


        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def READONLY(self):
            return self.getToken(CSharpParser.READONLY, 0)

        def REF(self):
            return self.getToken(CSharpParser.REF, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_struct_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStruct_definition" ):
                listener.enterStruct_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStruct_definition" ):
                listener.exitStruct_definition(self)




    def struct_definition(self):

        localctx = CSharpParser.Struct_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 400, self.RULE_struct_definition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2433
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.READONLY or _la==CSharpParser.REF:
                self.state = 2432
                _la = self._input.LA(1)
                if not(_la==CSharpParser.READONLY or _la==CSharpParser.REF):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 2435
            self.match(CSharpParser.STRUCT)
            self.state = 2436
            self.identifier()
            self.state = 2438
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.LT:
                self.state = 2437
                self.type_parameter_list()


            self.state = 2441
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.COLON:
                self.state = 2440
                self.struct_interfaces()


            self.state = 2444
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.WHERE:
                self.state = 2443
                self.type_parameter_constraints_clauses()


            self.state = 2446
            self.struct_body()
            self.state = 2448
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.SEMICOLON:
                self.state = 2447
                self.match(CSharpParser.SEMICOLON)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_definitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTERFACE(self):
            return self.getToken(CSharpParser.INTERFACE, 0)

        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def class_body(self):
            return self.getTypedRuleContext(CSharpParser.Class_bodyContext,0)


        def variant_type_parameter_list(self):
            return self.getTypedRuleContext(CSharpParser.Variant_type_parameter_listContext,0)


        def interface_base(self):
            return self.getTypedRuleContext(CSharpParser.Interface_baseContext,0)


        def type_parameter_constraints_clauses(self):
            return self.getTypedRuleContext(CSharpParser.Type_parameter_constraints_clausesContext,0)


        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_interface_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterface_definition" ):
                listener.enterInterface_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterface_definition" ):
                listener.exitInterface_definition(self)




    def interface_definition(self):

        localctx = CSharpParser.Interface_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 402, self.RULE_interface_definition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2450
            self.match(CSharpParser.INTERFACE)
            self.state = 2451
            self.identifier()
            self.state = 2453
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.LT:
                self.state = 2452
                self.variant_type_parameter_list()


            self.state = 2456
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.COLON:
                self.state = 2455
                self.interface_base()


            self.state = 2459
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.WHERE:
                self.state = 2458
                self.type_parameter_constraints_clauses()


            self.state = 2461
            self.class_body()
            self.state = 2463
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.SEMICOLON:
                self.state = 2462
                self.match(CSharpParser.SEMICOLON)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Enum_definitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENUM(self):
            return self.getToken(CSharpParser.ENUM, 0)

        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def enum_body(self):
            return self.getTypedRuleContext(CSharpParser.Enum_bodyContext,0)


        def enum_base(self):
            return self.getTypedRuleContext(CSharpParser.Enum_baseContext,0)


        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_enum_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnum_definition" ):
                listener.enterEnum_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnum_definition" ):
                listener.exitEnum_definition(self)




    def enum_definition(self):

        localctx = CSharpParser.Enum_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 404, self.RULE_enum_definition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2465
            self.match(CSharpParser.ENUM)
            self.state = 2466
            self.identifier()
            self.state = 2468
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.COLON:
                self.state = 2467
                self.enum_base()


            self.state = 2470
            self.enum_body()
            self.state = 2472
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.SEMICOLON:
                self.state = 2471
                self.match(CSharpParser.SEMICOLON)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Delegate_definitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DELEGATE(self):
            return self.getToken(CSharpParser.DELEGATE, 0)

        def return_type(self):
            return self.getTypedRuleContext(CSharpParser.Return_typeContext,0)


        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)

        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def variant_type_parameter_list(self):
            return self.getTypedRuleContext(CSharpParser.Variant_type_parameter_listContext,0)


        def formal_parameter_list(self):
            return self.getTypedRuleContext(CSharpParser.Formal_parameter_listContext,0)


        def type_parameter_constraints_clauses(self):
            return self.getTypedRuleContext(CSharpParser.Type_parameter_constraints_clausesContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_delegate_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDelegate_definition" ):
                listener.enterDelegate_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDelegate_definition" ):
                listener.exitDelegate_definition(self)




    def delegate_definition(self):

        localctx = CSharpParser.Delegate_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 406, self.RULE_delegate_definition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2474
            self.match(CSharpParser.DELEGATE)
            self.state = 2475
            self.return_type()
            self.state = 2476
            self.identifier()
            self.state = 2478
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.LT:
                self.state = 2477
                self.variant_type_parameter_list()


            self.state = 2480
            self.match(CSharpParser.OPEN_PARENS)
            self.state = 2482
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BOOL) | (1 << CSharpParser.BY) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.IN) | (1 << CSharpParser.INT) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.LONG) | (1 << CSharpParser.NAMEOF))) != 0) or ((((_la - 67)) & ~0x3f) == 0 and ((1 << (_la - 67)) & ((1 << (CSharpParser.OBJECT - 67)) | (1 << (CSharpParser.ON - 67)) | (1 << (CSharpParser.ORDERBY - 67)) | (1 << (CSharpParser.OUT - 67)) | (1 << (CSharpParser.PARAMS - 67)) | (1 << (CSharpParser.PARTIAL - 67)) | (1 << (CSharpParser.REF - 67)) | (1 << (CSharpParser.REMOVE - 67)) | (1 << (CSharpParser.SBYTE - 67)) | (1 << (CSharpParser.SELECT - 67)) | (1 << (CSharpParser.SET - 67)) | (1 << (CSharpParser.SHORT - 67)) | (1 << (CSharpParser.STRING - 67)) | (1 << (CSharpParser.THIS - 67)) | (1 << (CSharpParser.UINT - 67)) | (1 << (CSharpParser.ULONG - 67)) | (1 << (CSharpParser.UNMANAGED - 67)) | (1 << (CSharpParser.USHORT - 67)) | (1 << (CSharpParser.VAR - 67)) | (1 << (CSharpParser.VOID - 67)) | (1 << (CSharpParser.WHEN - 67)) | (1 << (CSharpParser.WHERE - 67)) | (1 << (CSharpParser.YIELD - 67)) | (1 << (CSharpParser.IDENTIFIER - 67)) | (1 << (CSharpParser.OPEN_BRACKET - 67)) | (1 << (CSharpParser.OPEN_PARENS - 67)))) != 0):
                self.state = 2481
                self.formal_parameter_list()


            self.state = 2484
            self.match(CSharpParser.CLOSE_PARENS)
            self.state = 2486
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.WHERE:
                self.state = 2485
                self.type_parameter_constraints_clauses()


            self.state = 2488
            self.match(CSharpParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Event_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EVENT(self):
            return self.getToken(CSharpParser.EVENT, 0)

        def type_(self):
            return self.getTypedRuleContext(CSharpParser.Type_Context,0)


        def variable_declarators(self):
            return self.getTypedRuleContext(CSharpParser.Variable_declaratorsContext,0)


        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def member_name(self):
            return self.getTypedRuleContext(CSharpParser.Member_nameContext,0)


        def OPEN_BRACE(self):
            return self.getToken(CSharpParser.OPEN_BRACE, 0)

        def event_accessor_declarations(self):
            return self.getTypedRuleContext(CSharpParser.Event_accessor_declarationsContext,0)


        def CLOSE_BRACE(self):
            return self.getToken(CSharpParser.CLOSE_BRACE, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_event_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEvent_declaration" ):
                listener.enterEvent_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEvent_declaration" ):
                listener.exitEvent_declaration(self)




    def event_declaration(self):

        localctx = CSharpParser.Event_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 408, self.RULE_event_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2490
            self.match(CSharpParser.EVENT)
            self.state = 2491
            self.type_()
            self.state = 2500
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,322,self._ctx)
            if la_ == 1:
                self.state = 2492
                self.variable_declarators()
                self.state = 2493
                self.match(CSharpParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.state = 2495
                self.member_name()
                self.state = 2496
                self.match(CSharpParser.OPEN_BRACE)
                self.state = 2497
                self.event_accessor_declarations()
                self.state = 2498
                self.match(CSharpParser.CLOSE_BRACE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_declarators(self):
            return self.getTypedRuleContext(CSharpParser.Variable_declaratorsContext,0)


        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_field_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_declaration" ):
                listener.enterField_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_declaration" ):
                listener.exitField_declaration(self)




    def field_declaration(self):

        localctx = CSharpParser.Field_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 410, self.RULE_field_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2502
            self.variable_declarators()
            self.state = 2503
            self.match(CSharpParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Property_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member_name(self):
            return self.getTypedRuleContext(CSharpParser.Member_nameContext,0)


        def OPEN_BRACE(self):
            return self.getToken(CSharpParser.OPEN_BRACE, 0)

        def accessor_declarations(self):
            return self.getTypedRuleContext(CSharpParser.Accessor_declarationsContext,0)


        def CLOSE_BRACE(self):
            return self.getToken(CSharpParser.CLOSE_BRACE, 0)

        def right_arrow(self):
            return self.getTypedRuleContext(CSharpParser.Right_arrowContext,0)


        def throwable_expression(self):
            return self.getTypedRuleContext(CSharpParser.Throwable_expressionContext,0)


        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def ASSIGNMENT(self):
            return self.getToken(CSharpParser.ASSIGNMENT, 0)

        def variable_initializer(self):
            return self.getTypedRuleContext(CSharpParser.Variable_initializerContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_property_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProperty_declaration" ):
                listener.enterProperty_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProperty_declaration" ):
                listener.exitProperty_declaration(self)




    def property_declaration(self):

        localctx = CSharpParser.Property_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 412, self.RULE_property_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2505
            self.member_name()
            self.state = 2519
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.OPEN_BRACE]:
                self.state = 2506
                self.match(CSharpParser.OPEN_BRACE)
                self.state = 2507
                self.accessor_declarations()
                self.state = 2508
                self.match(CSharpParser.CLOSE_BRACE)
                self.state = 2513
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.ASSIGNMENT:
                    self.state = 2509
                    self.match(CSharpParser.ASSIGNMENT)
                    self.state = 2510
                    self.variable_initializer()
                    self.state = 2511
                    self.match(CSharpParser.SEMICOLON)


                pass
            elif token in [CSharpParser.ASSIGNMENT]:
                self.state = 2515
                self.right_arrow()
                self.state = 2516
                self.throwable_expression()
                self.state = 2517
                self.match(CSharpParser.SEMICOLON)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constant_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(CSharpParser.CONST, 0)

        def type_(self):
            return self.getTypedRuleContext(CSharpParser.Type_Context,0)


        def constant_declarators(self):
            return self.getTypedRuleContext(CSharpParser.Constant_declaratorsContext,0)


        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_constant_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant_declaration" ):
                listener.enterConstant_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant_declaration" ):
                listener.exitConstant_declaration(self)




    def constant_declaration(self):

        localctx = CSharpParser.Constant_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 414, self.RULE_constant_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2521
            self.match(CSharpParser.CONST)
            self.state = 2522
            self.type_()
            self.state = 2523
            self.constant_declarators()
            self.state = 2524
            self.match(CSharpParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Indexer_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def THIS(self):
            return self.getToken(CSharpParser.THIS, 0)

        def OPEN_BRACKET(self):
            return self.getToken(CSharpParser.OPEN_BRACKET, 0)

        def formal_parameter_list(self):
            return self.getTypedRuleContext(CSharpParser.Formal_parameter_listContext,0)


        def CLOSE_BRACKET(self):
            return self.getToken(CSharpParser.CLOSE_BRACKET, 0)

        def OPEN_BRACE(self):
            return self.getToken(CSharpParser.OPEN_BRACE, 0)

        def accessor_declarations(self):
            return self.getTypedRuleContext(CSharpParser.Accessor_declarationsContext,0)


        def CLOSE_BRACE(self):
            return self.getToken(CSharpParser.CLOSE_BRACE, 0)

        def right_arrow(self):
            return self.getTypedRuleContext(CSharpParser.Right_arrowContext,0)


        def throwable_expression(self):
            return self.getTypedRuleContext(CSharpParser.Throwable_expressionContext,0)


        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_indexer_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndexer_declaration" ):
                listener.enterIndexer_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndexer_declaration" ):
                listener.exitIndexer_declaration(self)




    def indexer_declaration(self):

        localctx = CSharpParser.Indexer_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 416, self.RULE_indexer_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2526
            self.match(CSharpParser.THIS)
            self.state = 2527
            self.match(CSharpParser.OPEN_BRACKET)
            self.state = 2528
            self.formal_parameter_list()
            self.state = 2529
            self.match(CSharpParser.CLOSE_BRACKET)
            self.state = 2538
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.OPEN_BRACE]:
                self.state = 2530
                self.match(CSharpParser.OPEN_BRACE)
                self.state = 2531
                self.accessor_declarations()
                self.state = 2532
                self.match(CSharpParser.CLOSE_BRACE)
                pass
            elif token in [CSharpParser.ASSIGNMENT]:
                self.state = 2534
                self.right_arrow()
                self.state = 2535
                self.throwable_expression()
                self.state = 2536
                self.match(CSharpParser.SEMICOLON)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Destructor_definitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TILDE(self):
            return self.getToken(CSharpParser.TILDE, 0)

        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)

        def body(self):
            return self.getTypedRuleContext(CSharpParser.BodyContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_destructor_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDestructor_definition" ):
                listener.enterDestructor_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDestructor_definition" ):
                listener.exitDestructor_definition(self)




    def destructor_definition(self):

        localctx = CSharpParser.Destructor_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 418, self.RULE_destructor_definition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2540
            self.match(CSharpParser.TILDE)
            self.state = 2541
            self.identifier()
            self.state = 2542
            self.match(CSharpParser.OPEN_PARENS)
            self.state = 2543
            self.match(CSharpParser.CLOSE_PARENS)
            self.state = 2544
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constructor_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)

        def body(self):
            return self.getTypedRuleContext(CSharpParser.BodyContext,0)


        def formal_parameter_list(self):
            return self.getTypedRuleContext(CSharpParser.Formal_parameter_listContext,0)


        def constructor_initializer(self):
            return self.getTypedRuleContext(CSharpParser.Constructor_initializerContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_constructor_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstructor_declaration" ):
                listener.enterConstructor_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstructor_declaration" ):
                listener.exitConstructor_declaration(self)




    def constructor_declaration(self):

        localctx = CSharpParser.Constructor_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 420, self.RULE_constructor_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2546
            self.identifier()
            self.state = 2547
            self.match(CSharpParser.OPEN_PARENS)
            self.state = 2549
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BOOL) | (1 << CSharpParser.BY) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.IN) | (1 << CSharpParser.INT) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.LONG) | (1 << CSharpParser.NAMEOF))) != 0) or ((((_la - 67)) & ~0x3f) == 0 and ((1 << (_la - 67)) & ((1 << (CSharpParser.OBJECT - 67)) | (1 << (CSharpParser.ON - 67)) | (1 << (CSharpParser.ORDERBY - 67)) | (1 << (CSharpParser.OUT - 67)) | (1 << (CSharpParser.PARAMS - 67)) | (1 << (CSharpParser.PARTIAL - 67)) | (1 << (CSharpParser.REF - 67)) | (1 << (CSharpParser.REMOVE - 67)) | (1 << (CSharpParser.SBYTE - 67)) | (1 << (CSharpParser.SELECT - 67)) | (1 << (CSharpParser.SET - 67)) | (1 << (CSharpParser.SHORT - 67)) | (1 << (CSharpParser.STRING - 67)) | (1 << (CSharpParser.THIS - 67)) | (1 << (CSharpParser.UINT - 67)) | (1 << (CSharpParser.ULONG - 67)) | (1 << (CSharpParser.UNMANAGED - 67)) | (1 << (CSharpParser.USHORT - 67)) | (1 << (CSharpParser.VAR - 67)) | (1 << (CSharpParser.VOID - 67)) | (1 << (CSharpParser.WHEN - 67)) | (1 << (CSharpParser.WHERE - 67)) | (1 << (CSharpParser.YIELD - 67)) | (1 << (CSharpParser.IDENTIFIER - 67)) | (1 << (CSharpParser.OPEN_BRACKET - 67)) | (1 << (CSharpParser.OPEN_PARENS - 67)))) != 0):
                self.state = 2548
                self.formal_parameter_list()


            self.state = 2551
            self.match(CSharpParser.CLOSE_PARENS)
            self.state = 2553
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.COLON:
                self.state = 2552
                self.constructor_initializer()


            self.state = 2555
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method_member_name(self):
            return self.getTypedRuleContext(CSharpParser.Method_member_nameContext,0)


        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)

        def method_body(self):
            return self.getTypedRuleContext(CSharpParser.Method_bodyContext,0)


        def right_arrow(self):
            return self.getTypedRuleContext(CSharpParser.Right_arrowContext,0)


        def throwable_expression(self):
            return self.getTypedRuleContext(CSharpParser.Throwable_expressionContext,0)


        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def type_parameter_list(self):
            return self.getTypedRuleContext(CSharpParser.Type_parameter_listContext,0)


        def formal_parameter_list(self):
            return self.getTypedRuleContext(CSharpParser.Formal_parameter_listContext,0)


        def type_parameter_constraints_clauses(self):
            return self.getTypedRuleContext(CSharpParser.Type_parameter_constraints_clausesContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_method_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod_declaration" ):
                listener.enterMethod_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod_declaration" ):
                listener.exitMethod_declaration(self)




    def method_declaration(self):

        localctx = CSharpParser.Method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 422, self.RULE_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2557
            self.method_member_name()
            self.state = 2559
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.LT:
                self.state = 2558
                self.type_parameter_list()


            self.state = 2561
            self.match(CSharpParser.OPEN_PARENS)
            self.state = 2563
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BOOL) | (1 << CSharpParser.BY) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.IN) | (1 << CSharpParser.INT) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.LONG) | (1 << CSharpParser.NAMEOF))) != 0) or ((((_la - 67)) & ~0x3f) == 0 and ((1 << (_la - 67)) & ((1 << (CSharpParser.OBJECT - 67)) | (1 << (CSharpParser.ON - 67)) | (1 << (CSharpParser.ORDERBY - 67)) | (1 << (CSharpParser.OUT - 67)) | (1 << (CSharpParser.PARAMS - 67)) | (1 << (CSharpParser.PARTIAL - 67)) | (1 << (CSharpParser.REF - 67)) | (1 << (CSharpParser.REMOVE - 67)) | (1 << (CSharpParser.SBYTE - 67)) | (1 << (CSharpParser.SELECT - 67)) | (1 << (CSharpParser.SET - 67)) | (1 << (CSharpParser.SHORT - 67)) | (1 << (CSharpParser.STRING - 67)) | (1 << (CSharpParser.THIS - 67)) | (1 << (CSharpParser.UINT - 67)) | (1 << (CSharpParser.ULONG - 67)) | (1 << (CSharpParser.UNMANAGED - 67)) | (1 << (CSharpParser.USHORT - 67)) | (1 << (CSharpParser.VAR - 67)) | (1 << (CSharpParser.VOID - 67)) | (1 << (CSharpParser.WHEN - 67)) | (1 << (CSharpParser.WHERE - 67)) | (1 << (CSharpParser.YIELD - 67)) | (1 << (CSharpParser.IDENTIFIER - 67)) | (1 << (CSharpParser.OPEN_BRACKET - 67)) | (1 << (CSharpParser.OPEN_PARENS - 67)))) != 0):
                self.state = 2562
                self.formal_parameter_list()


            self.state = 2565
            self.match(CSharpParser.CLOSE_PARENS)
            self.state = 2567
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.WHERE:
                self.state = 2566
                self.type_parameter_constraints_clauses()


            self.state = 2574
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.OPEN_BRACE, CSharpParser.SEMICOLON]:
                self.state = 2569
                self.method_body()
                pass
            elif token in [CSharpParser.ASSIGNMENT]:
                self.state = 2570
                self.right_arrow()
                self.state = 2571
                self.throwable_expression()
                self.state = 2572
                self.match(CSharpParser.SEMICOLON)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_member_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(CSharpParser.IdentifierContext,i)


        def DOUBLE_COLON(self):
            return self.getToken(CSharpParser.DOUBLE_COLON, 0)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.DOT)
            else:
                return self.getToken(CSharpParser.DOT, i)

        def type_argument_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Type_argument_listContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Type_argument_listContext,i)


        def getRuleIndex(self):
            return CSharpParser.RULE_method_member_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod_member_name" ):
                listener.enterMethod_member_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod_member_name" ):
                listener.exitMethod_member_name(self)




    def method_member_name(self):

        localctx = CSharpParser.Method_member_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 424, self.RULE_method_member_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2581
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,332,self._ctx)
            if la_ == 1:
                self.state = 2576
                self.identifier()
                pass

            elif la_ == 2:
                self.state = 2577
                self.identifier()
                self.state = 2578
                self.match(CSharpParser.DOUBLE_COLON)
                self.state = 2579
                self.identifier()
                pass


            self.state = 2590
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,334,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2584
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==CSharpParser.LT:
                        self.state = 2583
                        self.type_argument_list()


                    self.state = 2586
                    self.match(CSharpParser.DOT)
                    self.state = 2587
                    self.identifier() 
                self.state = 2592
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,334,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Operator_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPERATOR(self):
            return self.getToken(CSharpParser.OPERATOR, 0)

        def overloadable_operator(self):
            return self.getTypedRuleContext(CSharpParser.Overloadable_operatorContext,0)


        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)

        def arg_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpParser.Arg_declarationContext)
            else:
                return self.getTypedRuleContext(CSharpParser.Arg_declarationContext,i)


        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)

        def body(self):
            return self.getTypedRuleContext(CSharpParser.BodyContext,0)


        def right_arrow(self):
            return self.getTypedRuleContext(CSharpParser.Right_arrowContext,0)


        def throwable_expression(self):
            return self.getTypedRuleContext(CSharpParser.Throwable_expressionContext,0)


        def SEMICOLON(self):
            return self.getToken(CSharpParser.SEMICOLON, 0)

        def IN(self, i:int=None):
            if i is None:
                return self.getTokens(CSharpParser.IN)
            else:
                return self.getToken(CSharpParser.IN, i)

        def COMMA(self):
            return self.getToken(CSharpParser.COMMA, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_operator_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator_declaration" ):
                listener.enterOperator_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator_declaration" ):
                listener.exitOperator_declaration(self)




    def operator_declaration(self):

        localctx = CSharpParser.Operator_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 426, self.RULE_operator_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2593
            self.match(CSharpParser.OPERATOR)
            self.state = 2594
            self.overloadable_operator()
            self.state = 2595
            self.match(CSharpParser.OPEN_PARENS)
            self.state = 2597
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.IN:
                self.state = 2596
                self.match(CSharpParser.IN)


            self.state = 2599
            self.arg_declaration()
            self.state = 2605
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.COMMA:
                self.state = 2600
                self.match(CSharpParser.COMMA)
                self.state = 2602
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpParser.IN:
                    self.state = 2601
                    self.match(CSharpParser.IN)


                self.state = 2604
                self.arg_declaration()


            self.state = 2607
            self.match(CSharpParser.CLOSE_PARENS)
            self.state = 2613
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpParser.OPEN_BRACE, CSharpParser.SEMICOLON]:
                self.state = 2608
                self.body()
                pass
            elif token in [CSharpParser.ASSIGNMENT]:
                self.state = 2609
                self.right_arrow()
                self.state = 2610
                self.throwable_expression()
                self.state = 2611
                self.match(CSharpParser.SEMICOLON)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arg_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(CSharpParser.Type_Context,0)


        def identifier(self):
            return self.getTypedRuleContext(CSharpParser.IdentifierContext,0)


        def ASSIGNMENT(self):
            return self.getToken(CSharpParser.ASSIGNMENT, 0)

        def expression(self):
            return self.getTypedRuleContext(CSharpParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_arg_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArg_declaration" ):
                listener.enterArg_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArg_declaration" ):
                listener.exitArg_declaration(self)




    def arg_declaration(self):

        localctx = CSharpParser.Arg_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 428, self.RULE_arg_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2615
            self.type_()
            self.state = 2616
            self.identifier()
            self.state = 2619
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.ASSIGNMENT:
                self.state = 2617
                self.match(CSharpParser.ASSIGNMENT)
                self.state = 2618
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invocationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)

        def argument_list(self):
            return self.getTypedRuleContext(CSharpParser.Argument_listContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_method_invocation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod_invocation" ):
                listener.enterMethod_invocation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod_invocation" ):
                listener.exitMethod_invocation(self)




    def method_invocation(self):

        localctx = CSharpParser.Method_invocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 430, self.RULE_method_invocation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2621
            self.match(CSharpParser.OPEN_PARENS)
            self.state = 2623
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BASE) | (1 << CSharpParser.BOOL) | (1 << CSharpParser.BY) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.CHECKED) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DEFAULT) | (1 << CSharpParser.DELEGATE) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FALSE) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.IN) | (1 << CSharpParser.INT) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.LONG) | (1 << CSharpParser.NAMEOF))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (CSharpParser.NEW - 65)) | (1 << (CSharpParser.NULL - 65)) | (1 << (CSharpParser.OBJECT - 65)) | (1 << (CSharpParser.ON - 65)) | (1 << (CSharpParser.ORDERBY - 65)) | (1 << (CSharpParser.OUT - 65)) | (1 << (CSharpParser.PARTIAL - 65)) | (1 << (CSharpParser.REF - 65)) | (1 << (CSharpParser.REMOVE - 65)) | (1 << (CSharpParser.SBYTE - 65)) | (1 << (CSharpParser.SELECT - 65)) | (1 << (CSharpParser.SET - 65)) | (1 << (CSharpParser.SHORT - 65)) | (1 << (CSharpParser.SIZEOF - 65)) | (1 << (CSharpParser.STRING - 65)) | (1 << (CSharpParser.THIS - 65)) | (1 << (CSharpParser.TRUE - 65)) | (1 << (CSharpParser.TYPEOF - 65)) | (1 << (CSharpParser.UINT - 65)) | (1 << (CSharpParser.ULONG - 65)) | (1 << (CSharpParser.UNCHECKED - 65)) | (1 << (CSharpParser.UNMANAGED - 65)) | (1 << (CSharpParser.USHORT - 65)) | (1 << (CSharpParser.VAR - 65)) | (1 << (CSharpParser.WHEN - 65)) | (1 << (CSharpParser.WHERE - 65)) | (1 << (CSharpParser.YIELD - 65)) | (1 << (CSharpParser.IDENTIFIER - 65)) | (1 << (CSharpParser.LITERAL_ACCESS - 65)) | (1 << (CSharpParser.INTEGER_LITERAL - 65)) | (1 << (CSharpParser.HEX_INTEGER_LITERAL - 65)) | (1 << (CSharpParser.BIN_INTEGER_LITERAL - 65)) | (1 << (CSharpParser.REAL_LITERAL - 65)) | (1 << (CSharpParser.CHARACTER_LITERAL - 65)) | (1 << (CSharpParser.REGULAR_STRING - 65)) | (1 << (CSharpParser.VERBATIUM_STRING - 65)) | (1 << (CSharpParser.INTERPOLATED_REGULAR_STRING_START - 65)) | (1 << (CSharpParser.INTERPOLATED_VERBATIUM_STRING_START - 65)) | (1 << (CSharpParser.OPEN_PARENS - 65)))) != 0) or ((((_la - 134)) & ~0x3f) == 0 and ((1 << (_la - 134)) & ((1 << (CSharpParser.PLUS - 134)) | (1 << (CSharpParser.MINUS - 134)) | (1 << (CSharpParser.STAR - 134)) | (1 << (CSharpParser.AMP - 134)) | (1 << (CSharpParser.CARET - 134)) | (1 << (CSharpParser.BANG - 134)) | (1 << (CSharpParser.TILDE - 134)) | (1 << (CSharpParser.OP_INC - 134)) | (1 << (CSharpParser.OP_DEC - 134)) | (1 << (CSharpParser.OP_RANGE - 134)))) != 0):
                self.state = 2622
                self.argument_list()


            self.state = 2625
            self.match(CSharpParser.CLOSE_PARENS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Object_creation_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_PARENS(self):
            return self.getToken(CSharpParser.OPEN_PARENS, 0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpParser.CLOSE_PARENS, 0)

        def argument_list(self):
            return self.getTypedRuleContext(CSharpParser.Argument_listContext,0)


        def object_or_collection_initializer(self):
            return self.getTypedRuleContext(CSharpParser.Object_or_collection_initializerContext,0)


        def getRuleIndex(self):
            return CSharpParser.RULE_object_creation_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObject_creation_expression" ):
                listener.enterObject_creation_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObject_creation_expression" ):
                listener.exitObject_creation_expression(self)




    def object_creation_expression(self):

        localctx = CSharpParser.Object_creation_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 432, self.RULE_object_creation_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2627
            self.match(CSharpParser.OPEN_PARENS)
            self.state = 2629
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BASE) | (1 << CSharpParser.BOOL) | (1 << CSharpParser.BY) | (1 << CSharpParser.BYTE) | (1 << CSharpParser.CHAR) | (1 << CSharpParser.CHECKED) | (1 << CSharpParser.DECIMAL) | (1 << CSharpParser.DEFAULT) | (1 << CSharpParser.DELEGATE) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DOUBLE) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FALSE) | (1 << CSharpParser.FLOAT) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.IN) | (1 << CSharpParser.INT) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.LONG) | (1 << CSharpParser.NAMEOF))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (CSharpParser.NEW - 65)) | (1 << (CSharpParser.NULL - 65)) | (1 << (CSharpParser.OBJECT - 65)) | (1 << (CSharpParser.ON - 65)) | (1 << (CSharpParser.ORDERBY - 65)) | (1 << (CSharpParser.OUT - 65)) | (1 << (CSharpParser.PARTIAL - 65)) | (1 << (CSharpParser.REF - 65)) | (1 << (CSharpParser.REMOVE - 65)) | (1 << (CSharpParser.SBYTE - 65)) | (1 << (CSharpParser.SELECT - 65)) | (1 << (CSharpParser.SET - 65)) | (1 << (CSharpParser.SHORT - 65)) | (1 << (CSharpParser.SIZEOF - 65)) | (1 << (CSharpParser.STRING - 65)) | (1 << (CSharpParser.THIS - 65)) | (1 << (CSharpParser.TRUE - 65)) | (1 << (CSharpParser.TYPEOF - 65)) | (1 << (CSharpParser.UINT - 65)) | (1 << (CSharpParser.ULONG - 65)) | (1 << (CSharpParser.UNCHECKED - 65)) | (1 << (CSharpParser.UNMANAGED - 65)) | (1 << (CSharpParser.USHORT - 65)) | (1 << (CSharpParser.VAR - 65)) | (1 << (CSharpParser.WHEN - 65)) | (1 << (CSharpParser.WHERE - 65)) | (1 << (CSharpParser.YIELD - 65)) | (1 << (CSharpParser.IDENTIFIER - 65)) | (1 << (CSharpParser.LITERAL_ACCESS - 65)) | (1 << (CSharpParser.INTEGER_LITERAL - 65)) | (1 << (CSharpParser.HEX_INTEGER_LITERAL - 65)) | (1 << (CSharpParser.BIN_INTEGER_LITERAL - 65)) | (1 << (CSharpParser.REAL_LITERAL - 65)) | (1 << (CSharpParser.CHARACTER_LITERAL - 65)) | (1 << (CSharpParser.REGULAR_STRING - 65)) | (1 << (CSharpParser.VERBATIUM_STRING - 65)) | (1 << (CSharpParser.INTERPOLATED_REGULAR_STRING_START - 65)) | (1 << (CSharpParser.INTERPOLATED_VERBATIUM_STRING_START - 65)) | (1 << (CSharpParser.OPEN_PARENS - 65)))) != 0) or ((((_la - 134)) & ~0x3f) == 0 and ((1 << (_la - 134)) & ((1 << (CSharpParser.PLUS - 134)) | (1 << (CSharpParser.MINUS - 134)) | (1 << (CSharpParser.STAR - 134)) | (1 << (CSharpParser.AMP - 134)) | (1 << (CSharpParser.CARET - 134)) | (1 << (CSharpParser.BANG - 134)) | (1 << (CSharpParser.TILDE - 134)) | (1 << (CSharpParser.OP_INC - 134)) | (1 << (CSharpParser.OP_DEC - 134)) | (1 << (CSharpParser.OP_RANGE - 134)))) != 0):
                self.state = 2628
                self.argument_list()


            self.state = 2631
            self.match(CSharpParser.CLOSE_PARENS)
            self.state = 2633
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSharpParser.OPEN_BRACE:
                self.state = 2632
                self.object_or_collection_initializer()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(CSharpParser.IDENTIFIER, 0)

        def ADD(self):
            return self.getToken(CSharpParser.ADD, 0)

        def ALIAS(self):
            return self.getToken(CSharpParser.ALIAS, 0)

        def ARGLIST(self):
            return self.getToken(CSharpParser.ARGLIST, 0)

        def ASCENDING(self):
            return self.getToken(CSharpParser.ASCENDING, 0)

        def ASYNC(self):
            return self.getToken(CSharpParser.ASYNC, 0)

        def AWAIT(self):
            return self.getToken(CSharpParser.AWAIT, 0)

        def BY(self):
            return self.getToken(CSharpParser.BY, 0)

        def DESCENDING(self):
            return self.getToken(CSharpParser.DESCENDING, 0)

        def DYNAMIC(self):
            return self.getToken(CSharpParser.DYNAMIC, 0)

        def EQUALS(self):
            return self.getToken(CSharpParser.EQUALS, 0)

        def FROM(self):
            return self.getToken(CSharpParser.FROM, 0)

        def GET(self):
            return self.getToken(CSharpParser.GET, 0)

        def GROUP(self):
            return self.getToken(CSharpParser.GROUP, 0)

        def INTO(self):
            return self.getToken(CSharpParser.INTO, 0)

        def JOIN(self):
            return self.getToken(CSharpParser.JOIN, 0)

        def LET(self):
            return self.getToken(CSharpParser.LET, 0)

        def NAMEOF(self):
            return self.getToken(CSharpParser.NAMEOF, 0)

        def ON(self):
            return self.getToken(CSharpParser.ON, 0)

        def ORDERBY(self):
            return self.getToken(CSharpParser.ORDERBY, 0)

        def PARTIAL(self):
            return self.getToken(CSharpParser.PARTIAL, 0)

        def REMOVE(self):
            return self.getToken(CSharpParser.REMOVE, 0)

        def SELECT(self):
            return self.getToken(CSharpParser.SELECT, 0)

        def SET(self):
            return self.getToken(CSharpParser.SET, 0)

        def UNMANAGED(self):
            return self.getToken(CSharpParser.UNMANAGED, 0)

        def VAR(self):
            return self.getToken(CSharpParser.VAR, 0)

        def WHEN(self):
            return self.getToken(CSharpParser.WHEN, 0)

        def WHERE(self):
            return self.getToken(CSharpParser.WHERE, 0)

        def YIELD(self):
            return self.getToken(CSharpParser.YIELD, 0)

        def getRuleIndex(self):
            return CSharpParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)




    def identifier(self):

        localctx = CSharpParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 434, self.RULE_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2635
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSharpParser.ADD) | (1 << CSharpParser.ALIAS) | (1 << CSharpParser.ARGLIST) | (1 << CSharpParser.ASCENDING) | (1 << CSharpParser.ASYNC) | (1 << CSharpParser.AWAIT) | (1 << CSharpParser.BY) | (1 << CSharpParser.DESCENDING) | (1 << CSharpParser.DYNAMIC) | (1 << CSharpParser.EQUALS) | (1 << CSharpParser.FROM) | (1 << CSharpParser.GET) | (1 << CSharpParser.GROUP) | (1 << CSharpParser.INTO) | (1 << CSharpParser.JOIN) | (1 << CSharpParser.LET) | (1 << CSharpParser.NAMEOF))) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & ((1 << (CSharpParser.ON - 68)) | (1 << (CSharpParser.ORDERBY - 68)) | (1 << (CSharpParser.PARTIAL - 68)) | (1 << (CSharpParser.REMOVE - 68)) | (1 << (CSharpParser.SELECT - 68)) | (1 << (CSharpParser.SET - 68)) | (1 << (CSharpParser.UNMANAGED - 68)) | (1 << (CSharpParser.VAR - 68)) | (1 << (CSharpParser.WHEN - 68)) | (1 << (CSharpParser.WHERE - 68)) | (1 << (CSharpParser.YIELD - 68)) | (1 << (CSharpParser.IDENTIFIER - 68)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[187] = self.right_arrow_sempred
        self._predicates[188] = self.right_shift_sempred
        self._predicates[189] = self.right_shift_assignment_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def right_arrow_sempred(self, localctx:Right_arrowContext, predIndex:int):
            if predIndex == 0:
                return (0 if localctx.first is None else localctx.first.tokenIndex) + 1 == (0 if localctx.second is None else localctx.second.tokenIndex)
         

    def right_shift_sempred(self, localctx:Right_shiftContext, predIndex:int):
            if predIndex == 1:
                return (0 if localctx.first is None else localctx.first.tokenIndex) + 1 == (0 if localctx.second is None else localctx.second.tokenIndex)
         

    def right_shift_assignment_sempred(self, localctx:Right_shift_assignmentContext, predIndex:int):
            if predIndex == 2:
                return (0 if localctx.first is None else localctx.first.tokenIndex) + 1 == (0 if localctx.second is None else localctx.second.tokenIndex)
         





from com.google.zxing.qrcode import QRCodeReader
from com.google.zxing.client.j2se import BufferedImageLuminanceSource
from com.google.zxing import BinaryBitmap
from java.util import Hashtable
from com.google.zxing import DecodeHintType
from com.google.zxing.common import HybridBinarizer
from java.util import Hashtable
from com.google.zxing import NotFoundException


'''
Name:
	QR_Decoder.py

Brief:
	Decodes the QR Code in any standard ImageJ bit depths/formats

 Author:
 	Pushkar Paranjpe
	 C-CAMP, India
	 pushkarparanjpe@gmail.com
	 http://mezzoderm.webfactional.com/
	 
Version:
	0.1

Since:
	Aug, 10, 2015

Based upon:
	* https://bitbucket.org/elliottslaughter/qr_decoder
	* the ZXing open-source, multi-format 1D/2D barcode image processing library. 
		http://code.google.com/p/zxing/
 '''


def getdata():
	defaultResultText = "Decoding Failed"
	
	qread = QRCodeReader()
	ip = IJ.getProcessor()
	myimg = ip.getBufferedImage()
	source = BufferedImageLuminanceSource(myimg)
	bitmap = BinaryBitmap(HybridBinarizer(source))
	resultText = defaultResultText
	try :
		hints = Hashtable()
		hints.put(DecodeHintType.TRY_HARDER, True)
		result = qread.decode(bitmap, hints)
		resultText = result.getText()
	except NotFoundException, ex:
		print ex
	
	return resultText



if __name__=='__main__':
	print getdata()
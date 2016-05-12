import Cocoa

aF = len(Cocoa.NSFontManager.sharedFontManager().availableFonts())
msg = str(aF) + " Active Fonts"

print msg


ES_IST = [9,10,30,49,50]
_EIN = [24,35,44]
_EINS = _EIN + [55]
_ZWEI = [4,15,24,35]
_DREI = [16,23,36,43]
_VIER = [77,82,97,102]
_FUENF = [76,83,96,103]
_SECHS = [19,20,39,40,59]
_SIEBEN = [55,64,75,84,95,104]
_ACHT = [18,21,38,41]
_NEUN = [37,42,57,62]
_ZEHN = [58,61,78,81]
_ELF = [2,17,22]
_ZWOELF = [54,65,74,85,94]
STUNDE = [_EINS, _ZWEI, _DREI, _VIER, _FUENF, _SECHS, _SIEBEN, _ACHT, _NEUN, _ZEHN, _ELF, _ZWOELF]

#X nach/vor
_NACH = [26,33,46,53]
_VOR = [66,73,86]

_FUENF_MINUTE = [70,89,90,109]
_ZEHN_MINUTE = [8,11,28,31]
_VIERTEL = [47,52,67,72,87,92,107]
_ZWANZIG = [48,51,68,71,88,91,108]
HALB = [5,14,25,34]


#X nach
FUENF_NACH = _FUENF_MINUTE + _NACH
ZEHN_NACH = _ZEHN_MINUTE + _NACH
VIERTEL_NACH = _VIERTEL + _NACH
ZWANZIG_NACH = _ZWANZIG + _NACH
FUENF_NACH_HALB = _FUENF_MINUTE + _NACH + HALB

#X vor
FUENF_VOR = _FUENF_MINUTE + _VOR
ZEHN_VOR = _ZEHN_MINUTE + _VOR
VIERTEL_VOR = _VIERTEL + _VOR
ZWANZIG_VOR = _ZWANZIG + _VOR
FUENF_VOR_HALB = _FUENF_MINUTE + _VOR + HALB

UHR = [80,99,100]



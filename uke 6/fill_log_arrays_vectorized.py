#6.2
import numpy as np

def f(x):
    return np.log(x)

x = np.linspace(1, 10, 101)
y = f(x)

for a, b in zip(x, y):
    print("%7.2f%7.2f"%(a, b))

"""
Terminal>fill_log_arrays_vectorized.py
   1.00   0.00
   1.09   0.09
   1.18   0.17
   1.27   0.24
   1.36   0.31
   1.45   0.37
   1.54   0.43
   1.63   0.49
   1.72   0.54
   1.81   0.59
   1.90   0.64
   1.99   0.69
   2.08   0.73
   2.17   0.77
   2.26   0.82
   2.35   0.85
   2.44   0.89
   2.53   0.93
   2.62   0.96
   2.71   1.00
   2.80   1.03
   2.89   1.06
   2.98   1.09
   3.07   1.12
   3.16   1.15
   3.25   1.18
   3.34   1.21
   3.43   1.23
   3.52   1.26
   3.61   1.28
   3.70   1.31
   3.79   1.33
   3.88   1.36
   3.97   1.38
   4.06   1.40
   4.15   1.42
   4.24   1.44
   4.33   1.47
   4.42   1.49
   4.51   1.51
   4.60   1.53
   4.69   1.55
   4.78   1.56
   4.87   1.58
   4.96   1.60
   5.05   1.62
   5.14   1.64
   5.23   1.65
   5.32   1.67
   5.41   1.69
   5.50   1.70
   5.59   1.72
   5.68   1.74
   5.77   1.75
   5.86   1.77
   5.95   1.78
   6.04   1.80
   6.13   1.81
   6.22   1.83
   6.31   1.84
   6.40   1.86
   6.49   1.87
   6.58   1.88
   6.67   1.90
   6.76   1.91
   6.85   1.92
   6.94   1.94
   7.03   1.95
   7.12   1.96
   7.21   1.98
   7.30   1.99
   7.39   2.00
   7.48   2.01
   7.57   2.02
   7.66   2.04
   7.75   2.05
   7.84   2.06
   7.93   2.07
   8.02   2.08
   8.11   2.09
   8.20   2.10
   8.29   2.12
   8.38   2.13
   8.47   2.14
   8.56   2.15
   8.65   2.16
   8.74   2.17
   8.83   2.18
   8.92   2.19
   9.01   2.20
   9.10   2.21
   9.19   2.22
   9.28   2.23
   9.37   2.24
   9.46   2.25
   9.55   2.26
   9.64   2.27
   9.73   2.28
   9.82   2.28
   9.91   2.29
  10.00   2.30
"""

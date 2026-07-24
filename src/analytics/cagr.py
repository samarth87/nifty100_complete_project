def calculate_cagr(start,end,years,available=None):
 if available is not None and available<years+1:return None,'INSUFFICIENT'
 if start==0:return None,'ZERO_BASE'
 if start>0>end:return None,'DECLINE_TO_LOSS'
 if start<0<end:return None,'TURNAROUND'
 if start<0 and end<0:return None,'BOTH_NEGATIVE'
 return ((end/start)**(1/years)-1)*100,'OK'

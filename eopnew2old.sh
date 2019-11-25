

awk '{printf ("%3s%3d%7d%9.4f%9.4f%10.5f%12.5f%9.1f%8.1f\n",$2,$3,$4,$5,$6,$7,$7-19,$9*1000,$10*1000)}' eopc.final >EOP.final0

awk '{switch ($1) { case "1" : $1="Jan"; print $0;break;
 case "2" : $1="Feb"; print $0;break;
 case "3" : $1="Mar"; print $0;break;
 case "4" : $1="Apr"; print $0;break;
 case "5" : $1="May"; print $0;break;
 case "6" : $1="Jun"; print $0;break;
 case "7" : $1="Jul"; print $0;break;
 case "8" : $1="Aug"; print $0;break;
 case "9" : $1="Sep"; print $0;break;
 case "10" : $1="Oct"; print $0;break;
 case "11" : $1="Nov"; print $0;break;
 case "12" : $1="Dec"; print $0;break; }}' EOP.final0 >>EOP.final

awk '{printf ("%3s%3d%7d%9.4f%9.4f%10.5f%12.5f%9.1f%8.1f\n",$1,$2,$3,$4,$5,$6,$7,$8,$9)}' EOP.final >EOP1.final

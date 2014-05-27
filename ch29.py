def time12hr(time):
        hr = int(time[0:2])
        if hr == 0:
        	return "%s:%s a.m."%("12",time[2:4])
        if hr < 12:
                return "%s:%s a.m."%(time[0:2],time[2:4])
        elif hr > 12:
                return "%s:%s p.m."%(int(time[0:2])-12,time[2:4])
        else:
        	return "%s:%s p.m."%(time[0:2],time[2:4])

if __name__ == "__main__":
	print time12hr('1619')

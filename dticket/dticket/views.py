import sys
import sqlite3
from datetime import timedelta, datetime, date
import matplotlib

class Dticket(object):
	def save_wait_ts (self, t_id, t_start_ts, t_end_ts, t_email=None, t_customer=None):
		"""
		Method to add/update data related dticket record to dticketdb.
		"""
		# Setup connection to dticket database
		conn = sqlite3.connect('../db/dticketdb.db', timeout=5)
		c = conn.cursor()
		
		try:			#attempt to insert new ticket record into database if ticket id is not there.
			c.execute('INSERT INTO dticket (ticket_id, ticket_start_ts, ticket_end_ts, email, ticket_cust) VALUES (?,?,?,?,?)',
			(t_id, t_start_ts, t_end_ts, t_email, t_customer))
		except sqlite3.IntegrityError:	#Catch exception if ticket id already exists and insert was performed, do update instead.
			c.execute('UPDATE dticket SET ticket_end_ts = ? WHERE ticket_id = ?', (t_end_ts, t_id))
		except Exception:				#General exception handling for invalid inputs for creation of dticket.
			print('ERROR INSERTING DTICKET RECORD!!!')
		
		# Commit updates to database and close connection.
		conn.commit()
		conn.close()
		
	def strfdelta (self, tdelta, fmt):
		"""
		Method to format timedelta object into a desired format for showing estimated wait time.
		"""
		d = {"days": tdelta.days}
		d["hours"], rem = divmod(tdelta.seconds, 3600)
		d["minutes"], d["seconds"] = divmod(rem, 60)
		return fmt.format(**d)

	def get_est_wait (self, t_date):
		"""
		Method to get the estimated wait time for ticket processing on given date
		"""
		#sdate = datetime.today().date()
		t_date = t_date.__str__()
		sdate_start_range = t_date + ' 00:00:00.000000'				#Beginning of search range of given day
		#$sdate_start_range = t_date + ' 17:20:00.000000'
		sdate_end_range = t_date + ' 23:59:59:999999'				#End of search of given day
		#sdate_end_range = t_date + ' 18:05:00:999999'
		#print(sdate_start_range)
		#print(sdate_end_range)
		conn = sqlite3.connect('../db/dticketdb.db', timeout=5)
		c = conn.cursor()
		try:
			c.execute('SELECT ticket_start_ts, ticket_end_ts FROM dticket WHERE ticket_start_ts >= ? AND ticket_end_ts <= ?',
			(sdate_start_range, sdate_end_range))
			#print c.fetchall()
			dticketset = c.fetchall()
			totaltickets = len(dticketset)
			if totaltickets == 0:
				whole_minutes = 0
			else:
				totalseconds = 0.0						#Initialize total seconds to 0.0.
				#totaltime = datetime.strptime(totaltime, "%H:%M:%S.%f")
				for i in range (0, totaltickets):				#Iterate
					#print dticketset[i]
					dt_start_time = dticketset[i][0]
					dt_start_time = datetime.strptime(dt_start_time, "%Y-%m-%d %H:%M:%S.%f")
					#print dt_start_time
					dt_end_time = dticketset[i][1]
					dt_end_time = datetime.strptime(dt_end_time, "%Y-%m-%d %H:%M:%S.%f")
					#print dt_end_time
					delta = dt_end_time - dt_start_time
					#delta = delta.timedelta()
					#print type(delta)
					#print delta
					ticket_seconds = delta.total_seconds()			#convert timedelta to seconds.
					print ('Seconds of ticket # [%s] is [%s] seconds' % (i,ticket_seconds))
					totalseconds = totalseconds + ticket_seconds	#keep running total of seconds of each.
				print ('Total seconds of all tickets is [%s] seconds' % totalseconds)
				avg_time_in_seconds = totalseconds/totaltickets			#calculate average time of ticket in seconds using total seconds divided by number of tickets.
				print ('Average time in SECONDS of tickets is [%s]' % avg_time_in_seconds)
				avg_time_in_minutes = avg_time_in_seconds/60			#convert average time in seconds to minutes
				print ('Average time in MINUTES of tickets is [%s]' % avg_time_in_minutes)
				whole_minutes = int(avg_time_in_minutes)				#Round the time in minutes down to lowest whole minute.
				print ('Average time in MINUTES rounded down to whole minutes is [%s]' % whole_minutes)
		except sqlite3.IntegrityError:
			print('Invalid date provided!')
		#conn.commit()
		if whole_minutes <> 1:
			str_minutes = '%s minutes' % whole_minutes
		else:
			str_minutes = '%s minute' % whole_minutes
		return str_minutes
		
		conn.close()
		
	def main(self,argv=None):
		#self.save_wait_ts(1, datetime.now(), datetime.now(), 'kevin.hsu@dealertrack.com', 'Kevin')
		#self.save_wait_ts('3@', datetime.now(), datetime.now(), 'rajanikanth.susarapu@dealertrack.com', 'Raj')
		
		#Provide yesterday's date for all the records we have so far
		input_date = datetime.now().date()
		day = timedelta(days=1)
		input_date = input_date - day
		
		input_date = datetime.now().date()
		
		x = self.get_est_wait(input_date)
		print x

if __name__ == "__main__":
	Dticket().main()
	
	
	
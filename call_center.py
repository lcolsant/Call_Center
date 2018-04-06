from datetime import datetime

class Call(object):
    NUM_CALLS = 1
    def __init__(self,caller_name, phone_num, reason):

        self.unique_id = Call.NUM_CALLS
        self.caller_name = caller_name
        self.phone_num = phone_num
        self.time = datetime.now().strftime("%I:%M:%S")
        self.reason = reason

        Call.NUM_CALLS+=1
        
 
    def display(self):
        print "unique_id:{}".format(self.unique_id)
        print "caller_name:{}".format(self.caller_name)
        print "phone_num:{}".format(self.phone_num)
        print "time:{}".format(self.time)
        print "reason:{}".format(self.reason)
        return self

class CallCenter(object):
    def __init__(self):
        self.calls = []

    def add_call(self,call):
        self.calls.append(call)

    def remove_call(self, call):
        self.calls.remove(call)

    def get_queue_size(self):
        print 'length of queue size: {}'.format(len(self.calls))

    def info(self):
        for i in self.calls:
            print 'Caller id: {} , {}, called at {} from number {} '.format(i.unique_id, i.caller_name, i.time, i.phone_num)
        return self

call1 = Call('lee','773-456-7891','product defect')
call2 = Call('lilian','312-654-9875','return')


newCall = CallCenter()
newCall.add_call(call1)
newCall.add_call(call2)
newCall.get_queue_size()
newCall.info()



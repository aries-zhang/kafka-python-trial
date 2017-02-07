'''Consumer module'''
from kafka import KafkaConsumer

SERVER = 'winsam1:9092'  #'10.161.169.142:9092' #10.152.29.38:9092

def main():
    '''The main function'''
    startconsume()

def startconsume():
    '''The consume function'''
    print 'start consumption..'
    consumer = KafkaConsumer('data-raw', bootstrap_servers=SERVER)
    print 'connected.'
    for msg in consumer:
        print msg.value

    print 'done.'

if __name__ == '__main__':
    main()
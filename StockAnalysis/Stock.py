import pandas_datareader.data as web
from datetime import datetime

class Stock:
    
    '''Return specific stock data for specific time period'''
    
    _stock_list = []
    
    def __init__(self,stock_name,enddate,length = 1,source='yahoo'):
        self._stock_name = stock_name
        self._length = length
        self._end_date = enddate
        
        self._start_date = datetime(self._end_date.year-self._length,self._end_date.month,self._end_date.day)
        self._source = source
        
        self.stock = self._get_stock_data()
        self._stock_list.append(self._stock_name)
   

    def _get_stock_data(self):
        return web.DataReader(self._stock_name,self._source,self._start_date,self._end_date)
    
    
    def get_stock_metadata(self):
        print('{} records with {} columns from {} to {} for the stock {}\n'. \
              format(self.stock.shape[0],self.stock.shape[1],min(self.stock.index),max(self.stock.index),self._stock_name))
        print('columns names: {}\n'.format(self.stock.columns))
        print('metadata: \n {} \n'.format(self.stock.describe()))
        print('here is the top 10 records: \n {}'.format(self.stock.head(10)))
    
    
    @classmethod
    def get_stock_list(self):
        return self._stock_list
        
        
    @property
    def stock_name(self):
        print('the stock is: ')
        return self._stock_name
    
    @stock_name.setter
    def stock_name(self,stock_name):        
        self._stock_name = stock_name
        self.stock = self._get_stock_data()
        self._stock_list.append(self._stock_name)
        print('the new stock set to: {}'.format(self._stock_name))
        
        
    @property
    def length(self):
        print('the length is: {}'.format(self._length))
        return self._length
    
    @length.setter
    def length(self,length):
        self._length = length
        self._start_date = datetime(self._end_date.year-self._length,self._end_date.month,self._end_date.day)
        self.stock = self._get_stock_data()
        print('the new length set to: {}'.format(self._length))
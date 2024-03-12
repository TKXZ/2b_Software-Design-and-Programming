class Emitter:
  __events = {}
  # 订阅
  def on(self, event, fn):
    if (event in self.__events):
      self.__events.get(event).append(fn)
    else:
      self.__events[event] = [fn]
  # 发布
  def emit(self, event, *args):
    if (event in self.__events):
      fns = self.__events[event]
      for f in fns:
        try: 
          f(*args)
        except Exception as e: 
          print(f"Error ${e}$")
        if (len(self.__events[event])): 
          continue
        else: 
          break
    else:
      print(f"No subscriber to ${event}$")
  # 取消订阅
  def off(self, event, fn):
    if (event in self.__events):
      fns = self.__events[event]
      self.__events[event] = [f for f in fns if f.__name__ != fn.__name__]
    else:
      print(f"Event ${event}$ not be subscribed")
  # 单次订阅
  def once(self, event, fn):
    def onlyOnce(*args):
      fn(*args)
      self.off(event, onlyOnce)
    self.on(event, onlyOnce)


bus = Emitter()

def fn(a, b):
  print(a, b)
def fn2():
  print("fn2")

bus.on('message', fn)
bus.once('message', fn)

bus.emit('message', True, 36)
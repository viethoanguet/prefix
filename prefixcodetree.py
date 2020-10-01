class PrefixCodeNode:
  def __init__(self):
    self.symbol = None
    self.left = None
    self.right = None
    
  def insertLeft(self):
    if self.left == None:
      self.left = PrefixCodeNode()

  def insertRight(self):
    if self.right == None:
      self.right = PrefixCodeNode()
  
class PrefixCodeTree:
  def __init__(self):
    self.root = PrefixCodeNode()

  def insert(self, codeword, symbol):
    node = self.root
    for bit in codeword:
      if bit == 0:
        node.insertLeft()
        node = node.left
      elif bit == 1:
        node.insertRight()
        node = node.right
    node.symbol = symbol
  
  def decode(self, encodedData, datalen):
    node = self.root
    res = ''
    bits =''
    for i in encodedData:
      bits += bin(i)[2:].zfill(8)
    bits = bits[0:datalen]
    for bit in bits:
      if bit == '0':
        node = node.left
      elif bit == '1':
        node = node.right 
      if node.symbol: 
        res += node.symbol
        node = self.root
    return res

if __name__ == "__main__" :
  codebook= {
    'x1': [0],
    'x2': [1,0,0],
    'x3': [1,0,1],
    'x4': [1,1],
  }
  codeTree = PrefixCodeTree()
  for symbol in codebook:
    codeTree.insert(codebook[symbol], symbol)
  message = codeTree.decode(b'\xd2\x9f\x20', 21)
  print(message)

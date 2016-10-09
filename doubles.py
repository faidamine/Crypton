from urllib import urlencode

def testcase(text, result):
   

   if (result != text):
       print "Error: double_urlencode testcase failure :("


      
       print text
       print result

       buf = ""
       for i in range(0, len(result)):
           try:
               if text[i] == result[i]:
                   buf += " "
               else:
                   buf += "^"
           except IndexError:
               buf += "*"

       print buf


def double_urlencode(text):
  

   text = single_urlencode(text)
   text = single_urlencode(text)

   return text

def single_urlencode(text):
   

   blah = urlencode({'blahblahblah':text})

  
   blah = blah[13:]

   return blah

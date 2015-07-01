import json

json_str = '{"a":"1", "b":"2", "c":"3"}';
parsed_str = json.loads(json_str);

print parsed_str; 
for key in parsed_str:
    print key, " with value of ", parsed_str[key];

print "key c has value ", parsed_str['c'];

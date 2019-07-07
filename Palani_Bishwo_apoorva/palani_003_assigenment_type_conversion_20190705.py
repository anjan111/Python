#type conversion functions and error messages

var_dict={  "int":12,
"float":2.52,
"bool":False,
"complex":1+0j,
"str":'sam',
"None":None,
"list":[1,2,3],
"tuple":(4,5,6),
"set":{10,11,12},
"dict":{"a":12,"b":15,"c":16}}
for i in var_dict:
    print "::Converting::", i, "::to other data types::\n"
    for ii in var_dict:
        try:
            eval(i)(var_dict[ii])
            print "::Conversion of::", i, " ::to::", ii, "::is allowed::", eval(i)(var_dict[ii])
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:{1!r}"
            print "::Conversion of::", i, " ::to::", ii, "::is not allowed::", template.format(type(ex).__name__, ex.args)
    print "\n"

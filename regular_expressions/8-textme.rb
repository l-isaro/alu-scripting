#!/usr/bin/env ruby
#: match output [sender],[reciever],[flags]

puts ARGV[0].scan(/\[(?:from:|to:|flags:)(.*?)\]/).join(",")

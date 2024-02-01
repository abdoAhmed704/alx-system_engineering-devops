#!/usr/bin/env ruby

def parse_log_entry(log_entry)
  match_data = log_entry.match(/\[from:(?<sender>[^\]]+)\] \[to:(?<receiver>[^\]]+)\] \[flags:(?<flags>[^\]]+)\]/)
  if match_data
    sender = match_data[:sender].strip
    receiver = match_data[:receiver].strip
    flags = match_data[:flags].strip
    puts "#{sender},#{receiver},#{flags}"
  else
    puts "Invalid log entry format"
  end
end

if ARGV.empty?
  puts "Usage: #{$PROGRAM_NAME} <log_entry>"
else
  log_entry = ARGV[0]
  parse_log_entry(log_entry)
end


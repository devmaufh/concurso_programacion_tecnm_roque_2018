def open_and_read_file(filename)
    b= Array.new
    text=""
    File.open(filename).each do |line|
        b<<line.reverse
    end
    for value in b do
        text+=value +"\n"
    end
    return text
end
def write_file(filename,text)
    File.open(filename, 'w') { |file| file.write(text) }
end


write_file("new_file.txt",open_and_read_file('file.txt'))
require 'prime'
array= Array.new
def Check_if_its_Prime(number)
    counter=0
    for value in 1..number do
        if number%value==0
            counter+=1
          #  puts value
        end
    end
    if(counter==2)
        return true
    else return false
    end
end

def prime_numbers_in_array(array)
    for number in array do
        
    end
end
prime_numbers_in_array([10,20,30,40])


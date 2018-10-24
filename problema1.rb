def cambiobase(n,b)
    if n==0
        return " "
    else
        return cambiobase(n/b,b)+ " "+ (n%b)
    end    
end


puts Integer.to_s("384739",2)
let rec fib n = 
        match n with
        | (0|1) -> 1
        | x when x > 0 -> (fib (x-2) + fib (x-1))
        | _ -> raise (Invalid_argument "dont do");;


let rec catalan =
       (fun n -> if n = 0 then 1 
       else catalan (n - 1) * 2 * (2 * n - 1) / (n + 1));;


let rec catalanMatch n =
        match n with
        | 0 -> 1
        | x when x > 0 -> catalan (n - 1) * 2 * (2 * n - 1) / (n + 1);;



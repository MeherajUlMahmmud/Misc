function nthFib(n) {
    # let cache = {}; //Start here
    function recurse(num) {
        # if (cache[num]):
        # 	return cache[num] // second step

        if (num == = 0 | | num == 1) return 1

        let result = recurse(num-1) + recurse(num-2)
        # cache[num] = result; // final step
        return result
    }
    return recurse(n)
}

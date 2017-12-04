#this file must be placed in a folder called tests(the run_test file also included tells R where to look for the tests)

test_that("Test functionality",{

  expect_equal(10,10)
})

# All test functions written below however this is  highlighted out while trying to understand why test_that command nto working
# ctrl and ALT  and C with the highlighted code removes the comments.

# test_that("Test Mean function",{
#   expect_that(6 ,equals(my_mean(c(3,6,9))))
# })
# 
# test_that("Sum  function works ",
#           {
#   expect_that(6 ,equals(my_sum(3,3)))
# })
# 
# 
# test_that("Subtract  function works ",
#           {
#             expect_that(6 ,equals(my_takeaway(9,3)))
#           })
# 
# test_that("Remainder function works ",
#           {
#             expect_that(0 ,equals(my_remainder(4,2)))
#           })
# 
# test_that("Division function works ",
#           {
#             expect_that(6 ,equals(my_divisor(18,3)))
#           })
# 
# test_that("Multiply function works ",
#           {
#             expect_that(12 ,equals(my_multiply(4,3)))
#           })
# 
# test_that("Square of a number function works ",
#           {
#             expect_that(9 ,equals(my_square(3)))
#           })
# test_that("A to the power of B  function works ",
#           {
#             expect_that(8 ,equals(my_power(2,3)))
#           })
# 
# test_that("Reciprocal unction works ",
#           {
#             expect_that(0.5 ,equals(my_reciprocal(2)))
#           })
# 
# test_that("Percentage function works ",
#           {
#             expect_that("75%" ,equals(my_percentage(0.75)))
#           })

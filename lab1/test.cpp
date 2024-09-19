#include "gtest/gtest.h"
#include "C:\Users\Арина\source\repos\laba1test\laba1test\laba1\Fun.cpp"
#include <iostream>
#include <list>
#include <algorithm>
#include <iterator>
#include <string>

using namespace std;

TEST(decimalToBinaryTest, PositiveNumbers) {
    EXPECT_EQ(decimalToBinary(5), "00000101 11111010 11111001");
    EXPECT_EQ(decimalToBinary(10), "00001010 11110101 11110100");
    EXPECT_EQ(decimalToBinary(25), "00011001 11100110 11100101");
}

TEST(decimalToBinaryTest, NegativeNumbers) {
    EXPECT_EQ(decimalToBinary(-5), "11111011 00000100 00000011");
    EXPECT_EQ(decimalToBinary(-10), "11110110 00001001 00001000");
    EXPECT_EQ(decimalToBinary(-25), "11100111 00011000 00010111");
}

TEST(addComplementaryTest, PositiveNumbers) {
    EXPECT_EQ(addComplementary(5, 3), "8 00001000 11110111 11110110");
    EXPECT_EQ(addComplementary(10, 7), "17 00010001 11101110 11101101");
    EXPECT_EQ(addComplementary(25, 15), "40 00101000 11010111 11010110");
}

TEST(DecimalToBinaryTest, test1) {
    int num = 10;

    ASSERT_EQ(decimalToBinary(num), "00001010 11110101 11110100");
}

TEST(AddComplementaryTest, test2) {
    int num1 = 5, num2 = 3;

    ASSERT_EQ(addComplementary(num1, num2), "8 00001000 11110111 11110110");
}


TEST(SubtractComplementaryTest, test3) {
    int num1 = 8, num2 = 3;

    ASSERT_EQ(subtractComplementary(num1, num2), "5 00000101 11111010 11111001");
}


TEST(MultiplyDirectTest, test4) {
    int num1 = 4, num2 = 2;

    ASSERT_EQ(multiplyDirect(num1, num2), "8 00001000 11110111 11110110");
}


TEST(DivideDirectTest, test5) {
    int num1 = 8, num2 = 2;

    ASSERT_EQ(divideDirect(num1, num2), "4.000000");
}

TEST(AddFloatingPointTest, test6) {
    float num1 = 3.5, num2 = 2.5;

    ASSERT_EQ(addFloatingPoint(num1, num2), "6.000000 00000000 11111111 11111110");
}

TEST(SubtractComplementaryTest, UnusedFunctionTest) {
    int num1 = 8, num2 = 3;
    ASSERT_EQ(subtractComplementary(num1, num2), "5 00000101 11111010 11111001");
}

TEST(MultiplyDirectTest2, UnusedFunctionTest) {
    int num1 = 4, num2 = 2;
    ASSERT_EQ(multiplyDirect(num1, num2), "8 00001000 11110111 11110110");
}

TEST(AddFloatingPointTest2, UnusedFunctionTest) {
    float num1 = 3.5, num2 = 2.5;
    ASSERT_EQ(addFloatingPoint(num1, num2), "6.000000 00000000 11111111 11111110");
}

TEST(MultiplyDirectTest3, PositiveNumbers) {
    EXPECT_EQ(multiplyDirect(5, 3), "15 00001111 11110000 11101111");
    EXPECT_EQ(multiplyDirect(10, 7), "70 01000110 10111001 10111000");
    EXPECT_EQ(multiplyDirect(25, 15), "375 01110111 10001000 10000111");
}

TEST(MultiplyDirectTest4, NegativeNumbers) {
    EXPECT_EQ(multiplyDirect(-5, -3), "15 00001111 11110000 11101111");
    EXPECT_EQ(multiplyDirect(-10, -7), "70 01000110 10111001 10111000");
    EXPECT_EQ(multiplyDirect(-25, -15), "375 01110111 10001000 10000111");
}

TEST(MultiplyDirectTest5, MixedNumbers) {
    EXPECT_EQ(multiplyDirect(5, -3), "-15 11110001 00001110 00001101");
    EXPECT_EQ(multiplyDirect(-10, 7), "-70 10111010 01000101 01000100");
    EXPECT_EQ(multiplyDirect(-25, 15), "-375 10001001 01110110 01110101");
}

TEST(decimalToBinaryTest2, ZeroInput) {
    EXPECT_EQ(decimalToBinary(0), "00000000 11111111 11111110");
}

TEST(subtractComplementaryTest2, ZeroDifference) {
    EXPECT_EQ(subtractComplementary(10, 10), "0 00000000 11111111 11111110");
}

TEST(subtractComplementaryTest2, NegativeDifference) {
    EXPECT_EQ(subtractComplementary(5, 10), "-5 11111011 00000100 00000011");
}

TEST(addFloatingPointTest2, NegativeNumbers) {
    EXPECT_EQ(addFloatingPoint(-3.5, -2.5), "-6.000000 00000000 11111111 11111110");
}

TEST(decimalToBinaryTest, ZeroInput) {
    EXPECT_EQ(decimalToBinary(0), "00000000 11111111 11111110");
}

TEST(addComplementaryTest, NegativeSum) {
    EXPECT_EQ(addComplementary(-5, -10), "-15 11110001 00001110 00001101");
}

TEST(subtractComplementaryTest3, ZeroDifference) {
    EXPECT_EQ(subtractComplementary(10, 10), "0 00000000 11111111 11111110");
}

TEST(subtractComplementaryTest4, NegativeDifference) {
    EXPECT_EQ(subtractComplementary(5, 10), "-5 11111011 00000100 00000011");
}

TEST(MultiplyDirectTest6, ZeroNum1) {
    EXPECT_EQ(multiplyDirect(0, 5), "0 00000000 11111111 11111110");
}

TEST(MultiplyDirectTest7, ZeroNum2) {
    EXPECT_EQ(multiplyDirect(10, 0), "0 00000000 11111111 11111110");
}

TEST(MultiplyDirectTest8, OverflowPositive) {
    EXPECT_EQ(multiplyDirect(INT_MAX, 2), "-2 11111110 00000001 00000000");
}

TEST(MultiplyDirectTest9, OverflowNegative) {
    EXPECT_EQ(multiplyDirect(INT_MIN, -2), "0 00000000 11111111 11111110");
}
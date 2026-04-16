module Demo
{
    interface Printer
    {
        void printString(string s);
        void printInt(int val);
    };

    interface Calculator
    {
        int add(int a, int b);
    };
};

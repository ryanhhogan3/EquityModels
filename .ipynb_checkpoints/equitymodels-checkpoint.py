{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "informative-england",
   "metadata": {},
   "outputs": [],
   "source": [
    "### This is the interworkings and mathematics behind the equity models\n",
    "\n",
    "### Gordon (Constant) Growth Model module ###\n",
    "def Gordongrowth(dividend, costofequity, growthrate):\n",
    "    price = dividend / (costofequity - growthrate)\n",
    "    price1 = round(price * .95, 2)\n",
    "    price2 = round(price * 1.05, 2)\n",
    "    print(f\"Based on the Gordon Growth Model, this stock's price is valued between: {price1} and {price2}.\")\n",
    "    \n",
    "### One Year Holding Perid\n",
    "def oneyearmodel(saleprice, dividend, costofequity):\n",
    "    price = (dividend + saleprice) / (1 + costofequity)\n",
    "    price1 = round(price * .95, 2)\n",
    "    price2 = round(price * 1.05, 2)\n",
    "    print(f\"Based on the One Year Holding Model, this stock's price is valued between: {price1} and {price2}.\")\n",
    "\n",
    "### Multi-Stage (Double Year Holding Period) Dividend Discount Model module ###\n",
    "def doubleyearmodel(saleprice, dividend1, dividend2, costofequity):\n",
    "    price = (dividend1 / (1 + costofequity)) + (dividend2 / (1 + costofequity)**2) + (saleprice / (1 + costofequity)**2)\n",
    "    price1 = round(price * .95, 2)\n",
    "    price2 = round(price * 1.05, 2)\n",
    "    print(f\"Based on the Two Year Holding Model, this stock's price is valued between: {price1} and {price2}.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "postal-title",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Based on the Gordon Growth Model, this stock's price is valued between: 158.33 and 175.0.\n"
     ]
    }
   ],
   "source": [
    "Gordongrowth(5, .08, 0.05)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "thrown-length",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Based on the Two Year Holding Model, this stock's price is valued between: 194.09 and 214.52.\n"
     ]
    }
   ],
   "source": [
    "doubleyearmodel(200, 5, 20,.05)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "hungarian-symbol",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Based on the One Year Holding Model, this stock's price is valued between: 185.48 and 205.0.\n"
     ]
    }
   ],
   "source": [
    "oneyearmodel(200, 5, .05)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "impossible-coral",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "oneyearmodel() missing 1 required positional argument: 'costofequity'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-24-e0f7cbe98c62>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0moneyearmodel\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m4\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m: oneyearmodel() missing 1 required positional argument: 'costofequity'"
     ]
    }
   ],
   "source": [
    "oneyearmodel(2,4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "binary-glass",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

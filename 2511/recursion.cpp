#include <iostream>
#include <random>

#include "vector"

std::vector<int> randomIntegers;
/// @brief recursive function mocking game-play 
/// where the second player always picks the same as the first.
/// you can modify the max number to anything you want
/// I didnt put in a condition to make it stop at zero. 
/// @param player1 
/// @param player2 
/// @param i 
void gameOfCards( int player1,  int player2, unsigned int i) {
    auto x = randomIntegers[i];
    player1 -= x;
    if (player1 <= 0 && player2 > 0) {
        std::cout << "Player one loses." << std::endl;
        std::cout << "Round # " << i << std::endl
                  << "X = " << x << std::endl
                  << "Player 1 = " << player1 << std::endl
                  << "Player 2 = " << player2 << std::endl;
        exit(EXIT_SUCCESS);

    }
    player2 -= x;
    if (player2 <= 0 && player1 > 0) {
        std::cout << "Player two loses." << std::endl;
        std::cout << "Round # " << i << std::endl
                  << "X = " << x << std::endl
                  << "Player 1 = " << player1 << std::endl
                  << "Player 2 = " << player2 << std::endl;
        exit(EXIT_SUCCESS);

    }
    std::cout << "Round # " << i << std::endl
              << "X = " << x << std::endl
              << "Player 1 = " << player1 << std::endl
              << "Player 2 = " << player2 << std::endl;
    --i;
    gameOfCards(player1, player2, i);
}

int main() {
    // create object for seeding
    std::random_device randomDevice;
    // create engine and seed it
    std::mt19937 engine{randomDevice()};
    // distribution in range [1, max]
    std::uniform_int_distribution<std::mt19937::result_type> dist20(1, 21);
     int maxSize = 10;
    /// @brief Generate random numbers
    for (unsigned int j = 0; j < maxSize; ++j) {
        randomIntegers.push_back(dist20(engine));
    }
    gameOfCards(maxSize, maxSize, maxSize);
}

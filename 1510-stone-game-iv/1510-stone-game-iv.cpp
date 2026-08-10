namespace {

namespace rs = std::ranges;
namespace vs = std::views;

constexpr auto kStoneUpLim{100'000};


const auto kWinningStates{[] [[nodiscard]] {
    auto winningStates{std::array<bool, kStoneUpLim + 1>{}};

   
    auto validSquareMoves{
        vs::iota(1) |
        vs::transform([] (auto const baseVal_) { return baseVal_ * baseVal_; }) |
        vs::take_while([] (auto const squareVal_) {
            return squareVal_ <= kStoneUpLim;
        }) |
        rs::to<std::vector>() 
    };

   
    for(auto const currStones: vs::iota(0, kStoneUpLim + 1)) {
        if(winningStates[currStones]) {
            continue;
        }

        
        for(auto const squareMove: validSquareMoves) {
            auto const nextStones{currStones + squareMove};

     
            if(nextStones > kStoneUpLim) {
                break;
            }
            winningStates[nextStones] = true;
        }
    }

    return winningStates;
}()};

auto const fastIOInit{
    [] {
        std::ios_base::sync_with_stdio(false);
        std::cin.tie(nullptr);
        return 0;
    } ()
};

} 

class Solution final {
public:
    [[nodiscard]]
    static auto winnerSquareGame(int const totalStones) -> bool;
};


auto Solution::winnerSquareGame(int const totalStones) -> bool {
    return kWinningStates[totalStones];
}
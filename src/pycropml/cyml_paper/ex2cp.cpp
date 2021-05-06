#define _USE_MATH_DEFINES
#include <cmath>
#include <iostream>
# include<vector>
# include<string>
# include<numeric>
# include<algorithm>
# include<array>
# include<ctime>
using namespace std;

template<typename T, class Container = std::vector<T>>
class Array
{
public:
    using container_type = Container;
    using value_type = T;
    using reference = typename container_type::reference;
    using const_reference = typename container_type::const_reference;
    using iterator = typename container_type::iterator;
    using const_iterator = typename container_type::const_iterator;
    using reverse_iterator = typename container_type::reverse_iterator;
    using const_reverse_iterator =
      typename container_type::const_reverse_iterator;
    using size_type = typename container_type::size_type;

protected:
    container_type m_c;
    size_type m_rows, m_columns;

public:
    Array();

    explicit Array(size_type cols, size_type rows);
    explicit Array(size_type cols, size_type rows, const value_type& value);

    ~Array() = default;

    Array(const Array& q) = default;
    Array(Array&& q) = default;

    Array& operator=(const Array& q) = default;
    Array& operator=(Array&& q) = default;

    Array& operator=(std::initializer_list<value_type> init);

    void resize(size_type cols, size_type rows);
    void resize(size_type cols, size_type rows, const value_type& value);

    template<class InputIterator>
    void assign(InputIterator first, InputIterator last);

    iterator begin() noexcept;
    const_iterator begin() const noexcept;
    iterator end() noexcept;
    const_iterator end() const noexcept;

    reverse_iterator rbegin() noexcept;
    const_reverse_iterator rbegin() const noexcept;
    reverse_iterator rend() noexcept;
    const_reverse_iterator rend() const noexcept;

    const_iterator cbegin() const noexcept;
    const_iterator cend() const noexcept;
    const_reverse_iterator crbegin() const noexcept;
    const_reverse_iterator crend() const noexcept;

    bool empty() const noexcept;
    size_type size() const noexcept;

    size_type rows() const noexcept;
    size_type columns() const noexcept;

    void set(size_type col, size_type row, const value_type& x);
    void set(size_type col, size_type row, value_type&& x);

    template<class... Args>
    void emplace(size_type col, size_type row, Args&&... args);

    const_reference operator()(size_type col, size_type row) const;
    reference operator()(size_type col, size_type row);

    void swap(Array& c) noexcept(noexcept(m_c.swap(c.m_c)));

private:
    void m_check_index(size_type col, size_type) const;
};


vector<int>  select(vector<int> x)
{
    vector<int> y;
    int e;
    for(const auto& e_cyml : x)
    {
        e = e_cyml;
        if (e != 0)
        {
            y.push_back(e);
        }
    }
    return y;
}


vector<int>  datype(vector<int> x)
{
    vector<int> y;
    vector<float> y2;
    vector<string> y3;
    vector<bool> y4;
    string k;
    float ll;
    int e;
    array<int, 5> yy;
    bool ee;
    for(const auto& e_cyml : x)
    {
        e = e_cyml;
        if (e != 0)
        {
            y.push_back(e);
        }
    }
    return y;
}

int main()
{
 vector<int>h{15,14,00,0,15,4};

 for(const auto&i: select(h)){

     cout<<i<<"\n";
 }
    
}
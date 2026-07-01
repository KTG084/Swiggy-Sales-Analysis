# 🍔 Swiggy Sales Analysis — Power BI DAX Measures

---

# Date Table
```DAX
DateTable = 
ADDCOLUMNS(
    CALENDAR(DATE(2022,1,1), DATE(2025,12,31)),
    "Year", YEAR([Date]),
    "Quarter", "Q" & FORMAT([Date], "Q"),
    "QuarterNum", QUARTER([Date]),
    "Month", FORMAT([Date], "MMMM"),
    "MonthNum", MONTH([Date]),
    "MonthShort", FORMAT([Date], "MMM"),
    "YearMonth", FORMAT([Date], "YYYY-MM"),
    "YearQuarter", FORMAT([Date], "YYYY") & " Q" & FORMAT([Date], "Q"),
    "WeekDay", FORMAT([Date], "dddd"),
    "DayOfWeek", WEEKDAY([Date]),
    "DayOfMonth", DAY([Date]),
    "IsWeekend", IF(WEEKDAY([Date]) IN {1,7}, "Weekend", "Weekday"),
    "FiscalYear", IF(MONTH([Date]) >= 4, YEAR([Date]), YEAR([Date]) - 1),
    "FiscalQuarter", 
        IF(MONTH([Date]) >= 4, 
           "Q" & FORMAT(QUARTER(DATE(YEAR([Date]), MONTH([Date]) - 3, 1)), "0"),
           "Q" & FORMAT(QUARTER(DATE(YEAR([Date]) - 1, MONTH([Date]) + 9, 1)), "0")
        )
)
```

---

# 🎯 DASHBOARD 1: EXECUTIVE OVERVIEW

## 🔥 OVERVIEW_MEASURES
```
// ============================================
// REVENUE MEASURES
// ============================================

Total Revenue = 
CALCULATE(
    SUM(orders_master[total_amount]),
    KEEPFILTERS(orders_master[order_status] = "Delivered")
)

Total Revenue Lakh = 
[Total Revenue] / 100000

Total Revenue Display = 
"₹" & FORMAT([Total Revenue] / 10000000, "0.00") & " Cr"

Revenue CY = 
VAR EndDate = MAX('DateTable'[Date])                
VAR StartDate = EDATE(EndDate, -12) + 1             
RETURN
CALCULATE(
    [Total Revenue],
    REMOVEFILTERS('DateTable'),                      
    'DateTable'[Date] >= StartDate,
    'DateTable'[Date] <= EndDate
)

Revenue LY = 
VAR CurrentEndDate = MAX('DateTable'[Date])
VAR PriorEndDate = EDATE(CurrentEndDate, -12)       
VAR PriorStartDate = EDATE(PriorEndDate, -12) + 1   
RETURN
CALCULATE(
    [Total Revenue],
    REMOVEFILTERS('DateTable'),
    'DateTable'[Date] >= PriorStartDate,
    'DateTable'[Date] <= PriorEndDate
)

Revenue Growth % = 
DIVIDE(
    [Revenue CY] - [Revenue LY], 
    [Revenue LY], 
    0
)

Revenue Growth Display = 
VAR _growth = [Revenue Growth %]
VAR _arrow = IF(_growth > 0, "▲", "▼")
VAR _color_indicator = IF(_growth >= 0, "+", "-") 
RETURN
IF(
    ISBLANK([Revenue LY]) || [Revenue LY] = 0,
    "No Prior Data",
    _arrow & " " & FORMAT(_growth, "0.00%") & " vs LY"
)

// ============================================
// ORDER MEASURES
// ============================================

Total Orders = 
COUNTROWS(orders_master)

Delivered Orders = 
CALCULATE(
    COUNTROWS(orders_master),
    orders_master[order_status] = "Delivered"
)

Cancelled Orders = 
CALCULATE(
    COUNTROWS(orders_master),
    orders_master[order_status] = "Cancelled"
)

Orders CY = 
VAR EndDate = MAX('DateTable'[Date])                
VAR StartDate = EDATE(EndDate, -12) + 1             
RETURN
CALCULATE(
    [Delivered Orders],                        
    REMOVEFILTERS('DateTable'),                      
    'DateTable'[Date] >= StartDate,
    'DateTable'[Date] <= EndDate
)

Orders LY = 
VAR CurrentEndDate = MAX('DateTable'[Date])
VAR PriorEndDate = EDATE(CurrentEndDate, -12)       
VAR PriorStartDate = EDATE(PriorEndDate, -12) + 1 
RETURN
CALCULATE(
    [Delivered Orders],
    REMOVEFILTERS('DateTable'),
    'DateTable'[Date] >= PriorStartDate,
    'DateTable'[Date] <= PriorEndDate
)

Orders Growth % = 
DIVIDE(
    [Orders CY] - [Orders LY], 
    [Orders LY], 
    0
)

Orders Growth Display = 
VAR _growth = [Orders Growth %]
VAR _arrow = IF(_growth > 0, "▲", "▼")
RETURN
IF(
    ISBLANK([Orders LY]) || [Orders LY] = 0,
    "No Prior Data",
    _arrow & " " & FORMAT(_growth, "0.00%") & " vs LY"
)

// ============================================
// CUSTOMER MEASURES
// ============================================

Total Customers = 
DISTINCTCOUNT(orders_master[user_id])

Customers CY = 
VAR EndDate = MAX('DateTable'[Date])                
VAR StartDate = EDATE(EndDate, -12) + 1             
RETURN
CALCULATE(
    [Total Customers],                        
    REMOVEFILTERS('DateTable'),                      
    'DateTable'[Date] >= StartDate,
    'DateTable'[Date] <= EndDate
)

Customers LY = 
VAR CurrentEndDate = MAX('DateTable'[Date])
VAR PriorEndDate = EDATE(CurrentEndDate, -12)       
VAR PriorStartDate = EDATE(PriorEndDate, -12) + 1 
RETURN
CALCULATE(
    [Total Customers],
    REMOVEFILTERS('DateTable'),
    'DateTable'[Date] >= PriorStartDate,
    'DateTable'[Date] <= PriorEndDate
)

Customers Growth % = 
DIVIDE([Customers CY] - [Customers LY], [Customers LY], 0)

Customers Growth Display = 
VAR _growth = [Customers Growth %]
VAR _arrow = IF(_growth > 0, "▲", "▼")
RETURN
IF(
    ISBLANK([Customers LY]) || [Customers LY] = 0,
    "No Prior Data",
    _arrow & " " & FORMAT(_growth, "0.00%") & " vs LY"
)

// ============================================
// AOV MEASURES
// ============================================

AOV = 
DIVIDE([Total Revenue], [Delivered Orders], 0)

AOV CY = 
DIVIDE([Revenue CY], [Orders CY], 0)

AOV LY = 
DIVIDE([Revenue LY], [Orders LY], 0)

AOV Growth % = 
DIVIDE(
    [AOV CY] - [AOV LY], 
    [AOV LY], 
    0
)

AOV Growth Display = 
VAR _growth = [AOV Growth %]
VAR _arrow = IF(_growth > 0, "▲", "▼")
RETURN
IF(
    ISBLANK([AOV LY]) || [AOV LY] = 0,
    "No Prior Data",
    _arrow & " " & FORMAT(_growth, "0.00%") & " vs LY"
)

// ============================================
// OTHER CORE MEASURES
// ============================================

Fulfillment Rate % = 
DIVIDE([Delivered Orders], [Total Orders], 0)

Cancellation Rate % = 
DIVIDE([Cancelled Orders], [Total Orders], 0)

// ============================================
// TOP PERFORMERS MEASURES
// ============================================

Top City Name = 
VAR _TopCity = TOPN(1, VALUES(orders_master[city]), [Total Revenue], DESC)
RETURN
MAXX(_TopCity, orders_master[city])

Top City Revenue = 
VAR _TopCityName = [Top City Name]
RETURN
CALCULATE([Total Revenue], orders_master[city] = _TopCityName)

Top City Display = 
[Top City Name] & UNICHAR(10) & 
"₹" & FORMAT([Top City Revenue] / 10000000, "0.00") & " Cr"

Top Cuisine Name = 
VAR _TopCuisineTable = TOPN(1, VALUES(orders_master[cuisine]), [Total Revenue], DESC)
RETURN
MAXX(_TopCuisineTable, orders_master[cuisine])

Top Cuisine Revenue = 
VAR _SelectedCuisine = [Top Cuisine Name]
RETURN
CALCULATE(
    [Total Revenue],
    orders_master[cuisine] = _SelectedCuisine
)

Top Cuisine Display = 
[Top Cuisine Name] & UNICHAR(10) &
"₹" & FORMAT([Top Cuisine Revenue] / 10000000, "0.00") & " Cr"

Peak Time = 
VAR _PeakTable = TOPN(1, VALUES(orders_master[time_slot]), [Delivered Orders], DESC)
RETURN
MAXX(_PeakTable, orders_master[time_slot])

Peak Time Orders = 
VAR _SelectedHour = [Peak Time]
RETURN
CALCULATE(
    [Delivered Orders],
    orders_master[time_slot] = _SelectedHour
)

Peak Time Display = 
[Peak Time] & UNICHAR(10) &
FORMAT([Peak Time Orders], "#,##0") & " orders"

Top Restaurant Name = 
VAR _TopRestTable = TOPN(1, VALUES(orders_master[restaurant_name]), [Total Revenue], DESC)
RETURN
MAXX(_TopRestTable, orders_master[restaurant_name])

Top Restaurant Revenue = 
VAR _SelectedRest = [Top Restaurant Name]
RETURN
CALCULATE(
    [Total Revenue],
    orders_master[restaurant_name] = _SelectedRest
)

Top Restaurant Display = 
[Top Restaurant Name] & UNICHAR(10) &
"₹" & FORMAT([Top Restaurant Revenue] / 100000, "0.00") & " L"

// ============================================
//  ALERT MEASURES
// ============================================

Alert - Cancellation = 
VAR CancRate = [Cancellation Rate %]
VAR Icon = 
    IF(CancRate >= 0.0499, "🔴",
    IF(CancRate >= 0.03, "🚫", "✅"))
RETURN
Icon & " Cancellation Rate: " & FORMAT(CancRate, "0.00%") & 
IF(CancRate >= 0.0499, " (CRITICAL)", 
IF(CancRate >= 0.03, " (WARNING)", ""))

Alert - High Cancel City = 
VAR CityTable = 
    ADDCOLUMNS(
        VALUES(orders_master[city]),
        "Rate", [Cancellation Rate %]
    )
VAR TopCityTable = TOPN(1, CityTable, [Rate], DESC)
VAR CityName = SELECTCOLUMNS(TopCityTable, "City", orders_master[city])
VAR CityRate = SELECTCOLUMNS(TopCityTable, "Rate", [Rate])
RETURN
"🔴 " & CityName & ": " & FORMAT(CityRate, "0.00%") & " cancellation"

Alert - At Risk Customers = 
VAR ReferenceDate = MAX(orders_master[order_date]) 
VAR AtRiskCustomersTable = 
    FILTER(
        SUMMARIZE(
            ALLSELECTED(orders_master), 
            orders_master[user_id],
            "LastOrderDate", MAX(orders_master[order_date])
        ),
        DATEDIFF([LastOrderDate], ReferenceDate, DAY) > 90
    )
VAR AtRiskCount = COUNTROWS(AtRiskCustomersTable)
VAR AtRiskRevenue = 
    CALCULATE(
        [Total Revenue],
        KEEPFILTERS(AtRiskCustomersTable)
    )
RETURN
IF(
    ISBLANK(AtRiskCount), 
    "No customers currently at risk",
    "👥 " & FORMAT(AtRiskCount, "#,##0") & " customers at risk" &
    " (₹" & FORMAT(AtRiskRevenue / 10000000, "0.00") & " Cr potential loss)"
)

Alert - Growth Status = 
VAR Growth = [Revenue Growth %]
RETURN
IF(Growth > 0.1, 
   "📈 Strong growth: +" & FORMAT(Growth, "0.00%") & " YoY",
IF(Growth > 0,
   "➡️ Modest growth: +" & FORMAT(Growth, "0.00%") & " YoY",
   "📉 Declining: " & FORMAT(Growth, "0.00%") & " YoY"
))

```

### Slicers (Filters)
**1.** Date Range Slicer
**2.** City Slicer
**3.** Customer Segment Slicer

---

# 🎯 DASHBOARD 2: CUSTOMER INTELLIGENCE 

### 👥 CUSTOMER_MEASURES
```
// ============================================
//  RFM MEASURES
// ============================================

Recency Days = 
VAR CustomerLastOrderDate = 
    MAX(orders_master[order_date])
VAR TodayDate = 
    TODAY()   //DATE(2025, 12, 31)
VAR DaysSinceLastOrder = 
    DATEDIFF(CustomerLastOrderDate, TodayDate, DAY)
RETURN
DaysSinceLastOrder

Frequency = [Delivered Orders]

Monetary Value = [Total Revenue]

R Score = 
VAR AllCustomers = ALL(orders_master[user_id])
VAR Q1 = PERCENTILEX.INC(AllCustomers, [Recency Days], 0.2)
VAR Q2 = PERCENTILEX.INC(AllCustomers, [Recency Days], 0.4)
VAR Q3 = PERCENTILEX.INC(AllCustomers, [Recency Days], 0.6)
VAR Q4 = PERCENTILEX.INC(AllCustomers, [Recency Days], 0.8)
RETURN
SWITCH(
    TRUE(),
    [Recency Days] <= Q1, 5,
    [Recency Days] <= Q2, 4,
    [Recency Days] <= Q3, 3,
    [Recency Days] <= Q4, 2,
    1
)

F Score = 
VAR AllCustomers = ALL(orders_master[user_id])
VAR F20 = PERCENTILEX.INC(AllCustomers, [Frequency], 0.2)
VAR F40 = PERCENTILEX.INC(AllCustomers, [Frequency], 0.4)
VAR F60 = PERCENTILEX.INC(AllCustomers, [Frequency], 0.6)
VAR F80 = PERCENTILEX.INC(AllCustomers, [Frequency], 0.8)
RETURN
SWITCH(
    TRUE(),
    [Frequency] >= F80, 5,
    [Frequency] >= F60, 4,
    [Frequency] >= F40, 3,
    [Frequency] >= F20, 2,
    1
)

M Score = 
VAR AllCustomers = ALL(orders_master[user_id])
VAR M20 = PERCENTILEX.INC(AllCustomers, [Monetary Value], 0.2)
VAR M40 = PERCENTILEX.INC(AllCustomers, [Monetary Value], 0.4)
VAR M60 = PERCENTILEX.INC(AllCustomers, [Monetary Value], 0.6)
VAR M80 = PERCENTILEX.INC(AllCustomers, [Monetary Value], 0.8)
RETURN
SWITCH(
    TRUE(),
    [Monetary Value] >= M80, 5,
    [Monetary Value] >= M60, 4,
    [Monetary Value] >= M40, 3,
    [Monetary Value] >= M20, 2,
    1
)

RFM Segment = 
VAR R = [R Score]
VAR F = [F Score]
VAR M = [M Score]
VAR Segment = 
SWITCH(
    TRUE(),
    R >= 4 && F >= 4 && M >= 4, "Champions",
    R >= 3 && F >= 3 && M >= 3, "Loyal Customers",
    R >= 4 && F < 3, "Potential Loyalists",
    R >= 3 && F < 3, "New Customers",
    R < 3 && F >= 3, "At Risk",
    R < 2 && F >= 3, "Can't Lose Them",
    R < 3 && F < 3 && M >= 3, "Hibernating",
    R < 2, "Lost",
    "Promising"
)
RETURN
Segment

Champions Count = 
CALCULATE(
    [Total Customers],
    FILTER(
        VALUES(orders_master[user_id]),
        [RFM Segment] = "Champions"
    )
)

Loyal Count = 
CALCULATE(
    [Total Customers],
    FILTER(
        VALUES(orders_master[user_id]),
        [RFM Segment] = "Loyal Customers"
    )
)

Promising Count = 
CALCULATE(
    [Total Customers],
    FILTER(
        VALUES(orders_master[user_id]),
        [RFM Segment] = "Promising"
    )
)

At Risk Count = 
CALCULATE(
    [Total Customers],
    FILTER(
        VALUES(orders_master[user_id]),
        [RFM Segment] = "At Risk"
    )
)

// ============================================
//  CLV MEASURES
// ============================================

Customer AOV = 
DIVIDE(
    [Monetary Value],
    [Frequency],
    0
)

Customer Lifetime Value = 
VAR AOV = [Customer AOV]
VAR OrdersPerMonth = 
    DIVIDE([Frequency], 12, 0)
VAR LifespanMonths = 36
VAR RetentionRate = 0.85
VAR GrossMargin = 0.25
VAR CLV = 
    AOV * OrdersPerMonth * LifespanMonths * RetentionRate * GrossMargin
RETURN
CLV

Average CLV = 
AVERAGEX(
    VALUES(orders_master[user_id]), 
    [Customer Lifetime Value]
)

Champions Average CLV = 
CALCULATE(
    [Average CLV],
    FILTER(
        VALUES(orders_master[user_id]), 
        [RFM Segment] = "Champions"
    )
)

Loyal Average CLV = 
CALCULATE(
    [Average CLV],
    FILTER(
        VALUES(orders_master[user_id]), 
        [RFM Segment] = "Loyal Customers"
    )
)

Promising Average CLV = 
CALCULATE(
    [Average CLV],
    FILTER(
        VALUES(orders_master[user_id]), 
        [RFM Segment] = "Promising"
    )
)

At Risk Average CLV = 
CALCULATE(
    [Average CLV],
    FILTER(
        VALUES(orders_master[user_id]), 
        [RFM Segment] = "At Risk"
    )
)

Total CLV = 
SUMX(
    VALUES(orders_master[user_id]),
    [Customer Lifetime Value]
)

At Risk Revenue Potential = 
[At Risk Count] * [At Risk Average CLV]

Avg Orders per Customer = 
DIVIDE(
    [Total Orders],
    [Total Customers],
    0
)
```

### Customer Segments Table

1. **"Modeling"** ribbon (top menu)
2. Click **"New table"**
3. A formula bar appears
4. DAX measure:

```DAX
Customer Segments = 
ADDCOLUMNS(
    SUMMARIZE(orders_master, orders_master[user_id]),
    "Segment", [RFM Segment],
    "CLV", [Customer Lifetime Value],
    "Recency", [Recency Days],
    "Frequency", [Frequency],
    "Monetary", [Monetary Value]
)
```

### Add Cohort Columns in `orders_master` Table

- Click **"Transform data"**

**Column 1: CohortMonth**
```M
Date.StartOfMonth([order_date])
```

**Column 2: FirstOrderMonth**
```M
let 
    currentID = [user_id] ,
    MinDate = List.Min(
    Table.SelectRows(#"Previous Step Name", each [user_id] = currentID)[order_date]
)
in 
    Date.StartOfMonth(MinDate)
```

**Column 3: MonthsFromFirst**
```M
(Date.Year([CohortMonth]) - Date.Year([FirstOrderMonth])) * 12 + 
(Date.Month([CohortMonth]) - Date.Month([FirstOrderMonth]))
```

### 👥 CUSTOMER_MEASURES (Continue)
```
// ============================================
//  COHORT MEASURES
// ============================================
Cohort Retention % = 
VAR SelectedCohort = SELECTEDVALUE(orders_master[FirstOrderMonth])
VAR SelectedMonth = SELECTEDVALUE(orders_master[MonthsFromFirst])
VAR CohortSize = 
    CALCULATE(
        DISTINCTCOUNT(orders_master[user_id]),
        orders_master[FirstOrderMonth] = SelectedCohort,
        orders_master[MonthsFromFirst] = 0
    )
VAR ActiveInMonth = 
    CALCULATE(
        DISTINCTCOUNT(orders_master[user_id]),
        orders_master[FirstOrderMonth] = SelectedCohort,
        orders_master[MonthsFromFirst] = SelectedMonth
    )
RETURN
DIVIDE(ActiveInMonth, CohortSize, 0)

// ============================================
//  Display MEASURES
// ============================================

Total CLV Display = 
"₹" & FORMAT([Total CLV] / 10000000, "0.00") & " Cr"

Champions Display = 
FORMAT([Champions Count], "#,##0")

Champions % = DIVIDE([Champions Count], [Total Customers], 0)

Champions % Display = 
var champ = [Champions %] + 0
RETURN
FORMAT(champ, "0.00%") & " of Customers"

At Risk Display = 
FORMAT([At Risk Count], "#,##0")

At Risk Cr Display = 
"₹" & FORMAT([At Risk Revenue Potential] / 10000000, "0.00") & " Cr at Stake"

Avg Orders per Customer Display = 
FORMAT([Avg Orders per Customer], "#,##0")

Champions CLV Card = 
"💎 Champions
Avg CLV: ₹" & FORMAT([Champions Average CLV] / 1000, "0.0") & "K
Count: " & FORMAT([Champions Count], "#,##0") & "
Total Value: ₹" & FORMAT([Champions Count] * [Champions Average CLV] / 10000000, "0.0") & " Cr"

Loyal CLV Card = 
"✓ Loyal Customers
Avg CLV: ₹" & FORMAT([Loyal Average CLV] / 1000, "0.0") & "K
Count: " & FORMAT([Loyal Count], "#,##0") & "
Total Value: ₹" & FORMAT([Loyal Count] * [Loyal Average CLV] / 10000000, "0.0") & " Cr"

Promising CLV Card = 
"🌱 Promising
Avg CLV: ₹" & FORMAT([Promising Average CLV] / 1000, "0.0") & "K
Count: " & FORMAT([Promising Count], "#,##0") & "
Total Value: ₹" & FORMAT([Promising Count] * [Promising Average CLV] / 10000000, "0.0") & " Cr"

At Risk CLV Card = 
"⚠️ At Risk
Avg CLV: ₹" & FORMAT([At Risk Average CLV] / 1000, "0.0") & "K
Count: " & FORMAT([At Risk Count], "#,##0") & "
At Stake: ₹" & FORMAT([At Risk Revenue Potential] / 10000000, "0.0") & " Cr"
```

### Slicers (Filters)
**1.** Date Range Slicer
**2.** City Slicer
**3.** Customer Segment Slicer

---

# 🎯 DASHBOARD 3: REVENUE ANALYTICS 

### 💰 REVENUE MEASURES
```
MTD Revenue = 
TOTALMTD(
    [Total Revenue],
    DateTable[Date]
)

MTD Revenue LM = 
CALCULATE(
    [MTD Revenue],
    DATEADD(DateTable[Date], -1, MONTH)
)

MTD Growth % = 
DIVIDE(
    [MTD Revenue] - [MTD Revenue LM],
    [MTD Revenue LM],
    0
)

MTD Display = 
"₹" & FORMAT([MTD Revenue] / 10000000, "0.00") & " Cr" 

MTD Growth Display = 
VAR _growth = [MTD Growth %]
VAR _arrow = IF(_growth > 0, "▲", "▼")
VAR _color_indicator = IF(_growth >= 0, "+", "-") 
RETURN
IF(
    ISBLANK([MTD Revenue LM]) || [MTD Revenue LM] = 0,
    "No Prior Data",
    _arrow & " " & _color_indicator & FORMAT(ABS(_growth), "0.00%") & " vs LM"
)

QTD Revenue = 
TOTALQTD(
    [Total Revenue],
    DateTable[Date]
)

QTD Revenue LQ = 
CALCULATE(
    [QTD Revenue], 
    DATEADD('DateTable'[Date], -1, QUARTER)
)

QTD Growth % = 
DIVIDE(
    [QTD Revenue] - [QTD Revenue LQ],
    [QTD Revenue LQ],
    0
)

QTD Display = 
"₹" & FORMAT([QTD Revenue] / 10000000, "0.00") & " Cr" 

QTD Growth Display = 
VAR _growth = [QTD Growth %]
VAR _arrow = IF(_growth > 0, "▲", "▼")
VAR _color_indicator = IF(_growth >= 0, "+", "-") 
RETURN
IF(
    ISBLANK([QTD Revenue LQ]) || [QTD Revenue LQ] = 0,
    "No Prior Data",
    _arrow & " " & _color_indicator & FORMAT(ABS(_growth), "0.00%") & " vs LQ"
)

YTD Revenue = 
TOTALYTD(
    [Total Revenue],
    DateTable[Date]
)

YTD Revenue LY = 
CALCULATE(
    [YTD Revenue], 
    DATEADD('DateTable'[Date], -1, YEAR)
)

YTD Growth % = 
DIVIDE(
    [YTD Revenue] - [YTD Revenue LY],
    [YTD Revenue LY],
    0
)

YTD Display = 
"₹" & FORMAT([YTD Revenue] / 10000000, "0.00") & " Cr" 

YTD Growth Display = 
VAR _growth = [YTD Growth %]
VAR _arrow = IF(_growth > 0, "▲", "▼")
VAR _color_indicator = IF(_growth >= 0, "+", "-") 
RETURN
IF(
    ISBLANK([YTD Revenue LY]) || [YTD Revenue LY] = 0,
    "No Prior Data",
    _arrow & " " & _color_indicator & FORMAT(ABS(_growth), "0.00%") & " vs LY"
)

Revenue Target Year = [Revenue LY] * 1.10

Target Achievement = [Revenue CY] - [Revenue Target Year]

Target Achievement % = 
DIVIDE(
    [Target Achievement],
    [Revenue Target Year],
    0
)

YOY_Display = 
VAR _growth = [Revenue Growth %]
VAR _arrow = IF(_growth > 0, "▲", "▼")
VAR _color_indicator = IF(_growth >= 0, "+", "-") 
RETURN
IF(
    ISBLANK([Revenue LY]) || [Revenue LY] = 0,
    "No Prior Data",
    _arrow & " " & _color_indicator & FORMAT(ABS(_growth), "0.00%")
)

Target Achievement Display = 
VAR TargetStatus = [Target Achievement %]
VAR _arrow = IF(TargetStatus > 0, "▲", "▼")
VAR _color_indicator = IF(TargetStatus >= 0, "+", "-") 
RETURN
IF(
    ISBLANK([Revenue LY]) || [Revenue LY] = 0,
    "No Prior Data",
    "YoY Growth " & _arrow & _color_indicator & FORMAT(ABS(TargetStatus), "0.00%") & " of Target"
)

Revenue LM = 
CALCULATE(
    [Total Revenue],
    DATEADD(DateTable[Date], -1, MONTH)
)

Revenue Target Month = [Revenue LM] * 1.10

City Revenue Rank = 
RANKX(
    ALL(orders_master[city]),
    [Total Revenue],
    ,
    DESC,
    DENSE
)

City Rank Display = 
"#" & FORMAT([City Revenue Rank], "0")

Max City Revenue = 
MAXX(
    ALL('orders_master'[city]), 
    [Total Revenue]
)

Target City Revenue = [Max City Revenue] * (3/5)

Total Revenue Cr = [Total Revenue] / 10000000

Cuisine Revenue % = 
DIVIDE(
    [Total Revenue],
    CALCULATE([Total Revenue], ALL(orders_master[cuisine])),
    0
)
```

### Slicers (Filters)
**1.** Date Range Slicer
**2.** City Slicer
**3.** Cuisine Slicer

---

# 🎯 DASHBOARD 4: RESTAURANT PERFORMANCE

### RESTAURANT MEASURES
```
Total Restaurants = 
DISTINCTCOUNT(orders_master[restaurant_id])

Avg Revenue per Restaurant = 
DIVIDE(
    [Total Revenue],
    [Total Restaurants],
    0
)

Avg Revenue per Restaurant Display = 
"₹" & FORMAT([Avg Revenue per Restaurant] / 100000, "0.00") & " L"

Top Performer Restaurant = 
CALCULATE(
    FIRSTNONBLANK(orders_master[restaurant_name], 1),
    TOPN(
        1,
        ALL(orders_master[restaurant_name]),
        [Total Revenue],
        DESC
    )
)

Top Performer Revenue = 
CALCULATE(
    [Total Revenue], 
    FILTER(
        ALL(orders_master[restaurant_name]), 
        orders_master[restaurant_name] = [Top Performer Restaurant]
    )
)

Top Restaurant Revenue Display = 
[Top Performer Restaurant] &
" ₹" & FORMAT([Top Performer Revenue] / 100000, "0.00") & " L"

Average Rating = 
AVERAGE(orders_master[restaurant_rating])

Restaurant Efficiency Score = 
VAR RestRevenue = [Total Revenue]
VAR RestOrders = [Delivered Orders]
VAR RestRating = [Average Rating]
VAR AvgRevenue = 
    CALCULATE(
        AVERAGEX(VALUES(orders_master[restaurant_name]), [Total Revenue]),
        ALLSELECTED(orders_master[restaurant_name])
    )
VAR AvgOrders = 
    CALCULATE(
        AVERAGEX(VALUES(orders_master[restaurant_name]), [Delivered Orders]),
        ALLSELECTED(orders_master[restaurant_name])
    )
VAR AvgRating = 
    CALCULATE(
        AVERAGEX(VALUES(orders_master[restaurant_name]), [Average Rating]),
        ALLSELECTED(orders_master[restaurant_name])
    )
VAR RevenueScore = DIVIDE(RestRevenue, AvgRevenue, 0)
VAR OrdersScore = DIVIDE(RestOrders, AvgOrders, 0)
VAR RatingScore = DIVIDE(RestRating, AvgRating, 0)
VAR EfficiencyScore = 
    (RevenueScore * 0.5) + 
    (OrdersScore * 0.3) + 
    (RatingScore * 0.2)
RETURN
EfficiencyScore

Underperforming Restaurants = 
CALCULATE(
    [Total Restaurants],
    FILTER(
        VALUES(orders_master[restaurant_name]),
        [Restaurant Efficiency Score] <= 0.7
    )
)

Underperforming Restaurants Display = 
VAR UnderperformingCount = [Underperforming Restaurants] + 0
VAR TotalCount = [Total Restaurants]
VAR Percentage = DIVIDE(UnderperformingCount, TotalCount, 0)
RETURN
FORMAT(UnderperformingCount, "#,##0") & " restaurants
" &
FORMAT(Percentage, "0.00%") & " of total"

Restaurant Revenue Rank = 
RANKX(
    ALL(orders_master[restaurant_name]),
    [Total Revenue],
    ,
    DESC,
    DENSE
)

Performance Category = 
VAR Score = [Restaurant Efficiency Score]
RETURN
SWITCH(
    TRUE(),
    Score >= 1.5, "⭐ Star Performer",
    Score >= 0.995, "✓ Good",
    Score >= 0.794, "⚠️ Average",
    "🔴 Needs Attention"
)
```

### Slicers (Filters)
**1.** Date Range Slicer
**2.** City Slicer
**3.** Cuisine Slicer

---

# 🎯 DASHBOARD 5: MENU & PRODUCT INTELLIGENCE 

### MENU & PRODUCT MEASURES
```
Total Menu Items = DISTINCTCOUNT(order_items_master[item_name])

Total Categories = DISTINCTCOUNT(order_items_master[category])

Veg Item Count = 
CALCULATE(
    DISTINCTCOUNT(order_items_master[item_name]),
    order_items_master[item_type] = "Veg"
)

Veg Percentage = 
DIVIDE([Veg Item Count], [Total Menu Items], 0)

Non-Veg Item Count = 
CALCULATE(
    DISTINCTCOUNT(order_items_master[menu_id]),
    order_items_master[item_type] = "Non-Veg"
)

Veg Percentage Display = 
VAR VegPct = [Veg Percentage] + 0
VAR VegCount = [Veg Item Count] + 0
VAR NonVegCount = [Non-Veg Item Count] + 0
RETURN
FORMAT(VegPct, "0.00%") & UNICHAR(10) &
FORMAT(VegCount, "#,##0") & " veg items" & UNICHAR(10) &
FORMAT(NonVegCount, "#,##0") & " non-veg items"

Multi Item Orders = 
CALCULATE(
    DISTINCTCOUNT(order_items_master[order_id]),
    FILTER(
        VALUES(order_items_master[order_id]),
        CALCULATE(COUNTROWS(order_items_master)) > 1
    )
)

Multi Item Order % = 
DIVIDE(
    [Multi Item Orders],
    DISTINCTCOUNT(order_items_master[order_id]),
    0
)

Items per Order = 
DIVIDE(
    COUNTROWS(order items_master),
    DISTINCTCOUNT(order_items_master[order_id]),
    0
)

Multi Item Display = 
VAR MultiOrderPct = [Multi Item Order %] + 0
VAR ItemsPerOrder = [Items per Order] + 0
RETURN
FORMAT(MultiOrderPct, "0.00%") & UNICHAR(10) &
"Multi-item orders" & UNICHAR(10) &
FORMAT(ItemsPerOrder, "0.00") & " items/order avg"

Times Ordered = 
COUNTROWS(order_items_master)

Item Revenue = SUM(order_items_master[line_total])

Item Revenue Display = 
"₹" & FORMAT([Item_Revenue] / 10000000, "0.00") & " Cr"

Item Revenue Cr = [Item_Revenue] / 10000000

Item Average Price = 
AVERAGE(order_items_master[menu_price])

Item Revenue Share % = 
DIVIDE(
    [Item Revenue],
    CALCULATE([Item Revenue], ALL(order_items_master[item_name])),
    0
)

Item Rank by Revenue = 
RANKX(
    ALL(order_items_master[item_name]),
    [Item Revenue],
    ,
    DESC,
    DENSE
)

ABC Classification = 
VAR ItemRank = [Item Rank by Revenue]
VAR TotalItems = CALCULATE([Total Menu Items], ALLSELECTED('order_items_master'))
VAR Top20Pct = TotalItems * 0.2
VAR Top50Pct = TotalItems * 0.5
RETURN
SWITCH(
    TRUE(),
    ItemRank <= Top20Pct , "A - High Value (Top 20%)",
    ItemRank <= Top50Pct , "B - Medium Value (20-50%)",
    "C - Low Value (Bottom 50%)"
)

Single Item Orders = 
CALCULATE(
    DISTINCTCOUNT(order_items_master[order_id]),
    FILTER(
        VALUES(order_items_master[order_id]),
        CALCULATE(COUNTROWS(order_items_master)) = 1
    )
)

Double Item Orders = 
CALCULATE(
    DISTINCTCOUNT(order_items_master[order_id]),
    FILTER(
        VALUES(order_items_master[order_id]),
        CALCULATE(COUNTROWS(order_items_master)) = 2
    )
)

Three or more Item Orders = 
CALCULATE(
    DISTINCTCOUNT(order_items_master[order_id]),
    FILTER(
        VALUES(order_items_master[order_id]),
        CALCULATE(COUNTROWS(order_items_master)) > 2
    )
)

Average Basket Value = 
DIVIDE(
    SUM(order_items_master[line_total]),
    DISTINCTCOUNT(order_items_master[order_id]),
    0
)

Top Combo Count = 
VAR OrderList =
    SELECTCOLUMNS(
        'order_items_master',
        "ID", [order_id],
        "Item", [item_name]
    )
VAR ItemPairs =
    GENERATE(
        OrderList,
        VAR CurrentID = [ID]
        VAR FirstItem = [Item]
        RETURN
            SELECTCOLUMNS(
                FILTER(
                    OrderList,
                    [ID] = CurrentID &&
                    [Item] > FirstItem
                ),
                "Item2", [Item]
            )
    )
VAR PairFrequency =
    GROUPBY(
        ItemPairs,
        [Item],
        [Item2],
        "Freq", SUMX(CURRENTGROUP(),1)
    )
RETURN
MAXX(PairFrequency, [Freq])


Top Combo Name = 
VAR OrderList =
    SELECTCOLUMNS(
        'order_items_master',
        "ID", [order_id],
        "Item", [item_name]
    )
VAR ItemPairs =
    GENERATE(
        OrderList,
        VAR CurrentID = [ID]
        VAR FirstItem = [Item]
        RETURN
            SELECTCOLUMNS(
                FILTER(
                    OrderList,
                    [ID] = CurrentID &&
                    [Item] > FirstItem
                ),
                "Item2", [Item]
            )
    )
VAR PairFrequency =
    GROUPBY(
        ItemPairs,
        [Item],
        [Item2],
        "Freq", SUMX(CURRENTGROUP(),1)
    )
VAR WinningPair =
    TOPN(
        1,
        PairFrequency,
        [Freq],
        DESC
    )
RETURN
MAXX(
    WinningPair,
    [Item] & " + " & [Item2]
)

Basket Insight 1 = 
"🛒 Average basket: " & FORMAT([Items per Order], "0.00") & " items per order"

Basket Insight 2 = 
"📊 " & FORMAT([Multi Item Order %], "0.00%") & " Orders contain 1+ items (" &
FORMAT([Multi Item Orders], "#,##0") & " orders)"

Basket Insight 3 = 
VAR one = FORMAT(DIVIDE([Single Item Orders], DISTINCTCOUNT(order_items_master[order_id]), 0), "0.00%")
VAR two = FORMAT(DIVIDE([Double Item Orders], DISTINCTCOUNT(order_items_master[order_id]), 0), "0.00%")
VAR three = FORMAT(DIVIDE([Three or more Item Orders], DISTINCTCOUNT(order_items_master[order_id]), 0), "0.00%")
RETURN
"✨ Item Distribution: 1 (" & one & ") | 2 (" & two & ") | 2+ (" & three & ")"

Basket Insight 4 = 
"💰 Avg. basket value: ₹" & FORMAT([Average Basket Value], "#,##0") &
" (avg " & FORMAT([Items per Order], "0.00") & " items × ₹" &
FORMAT(DIVIDE([Average Basket Value], [Items per Order], 0), "#,##0") & "/item)"

Basket Insight 5 = 
"💡 Top combo: " & [Top Combo Name] & " (" & [Top Combo Count] &" Orders)"

Basket Insight 6 = 
"📦 Only " & 
FORMAT(DIVIDE([Single Item Orders], DISTINCTCOUNT(order_items_master[order_id]), 0), "0.00%") &
" Single-Item Orders"
```

### Slicers (Filters)
**1.** Date Range Slicer
**2.** Category Slicer
**3.** Price Category Slicer

---

# 🎯 DASHBOARD 6: OPERATIONS & EFFICIENCY

### PERATIONS & EFFICIENCY MEASURES
```
Cancellation Loss Amount = 
CALCULATE(
    SUM(orders_master[total_amount]),
    orders_master[order_status] = "Cancelled"
)

Cancellation Display = 
FORMAT([Cancellation Rate %], "0.00%") & UNICHAR(10) &
FORMAT([Cancelled Orders], "#,##0") & " orders" & UNICHAR(10) &
"₹" & FORMAT([Cancellation Loss Amount] / 10000000, "0.0") & " Cr lost"

Fulfillment Display = 
FORMAT([Fulfillment Rate %], "0.00%") & UNICHAR(10) &
FORMAT([Delivered Orders], "#,##0") & " orders" & UNICHAR(10) &
"Target: 98%"

Peak Hour = 
VAR HourTable = 
    ADDCOLUMNS(
        VALUES(orders_master[delivery_time]),
        "HourNum", HOUR(orders_master[delivery_time]),
        "OrderCount", [Total Orders]
    )
VAR MaxOrders = MAXX(HourTable, [OrderCount])
VAR PeakHourNum = 
    CALCULATE(
        FIRSTNONBLANK(orders_master[delivery_time], 1),
        FILTER(HourTable, [OrderCount] = MaxOrders)
    )
RETURN
HOUR(PeakHourNum)

Peak Hour Orders = 
VAR PeakHr = [Peak Hour]
RETURN
CALCULATE(
    [Total Orders],
    HOUR(orders_master[delivery_time]) = PeakHr
)

Peak Hour Load % = 
DIVIDE([Peak Hour Orders], [Total Orders], 0)

Peak Hour Display = 
VAR PeakHr = [Peak Hour]
VAR AmPm = IF(PeakHr >= 12, "PM", "AM")
VAR Hour12 = IF(PeakHr > 12, PeakHr - 12, IF(PeakHr = 0, 12, PeakHr))
RETURN
Hour12 & ":00 " & AmPm & UNICHAR(10) &
FORMAT([Peak Hour Orders], "#,##0") & " orders" & UNICHAR(10) &
FORMAT([Peak Hour Load %], "0%") & " of daily volume"

Orders Overview = 
FORMAT([Total Orders], "#,##0") & UNICHAR(10) &
"Total Orders" & UNICHAR(10) &
FORMAT([Delivered Orders], "#,##0") & " delivered"

Revenue per Order = 
DIVIDE([Total Revenue], [Total Orders], 0)

Orders % = 
DIVIDE([Total Orders], CALCULATE([Total Orders], ALLSELECTED(orders_master)), 0)

Best Time Slot = 
CALCULATE(
    FIRSTNONBLANK(orders_master[time_slot], 1),
    TOPN(
        1,
        VALUES(orders_master[time_slot]),
        [Fulfillment Rate %],
        DESC
    )
)

Worst Time Slot = 
CALCULATE(
    FIRSTNONBLANK(orders_master[time_slot], 1),
    TOPN(
        1,
        VALUES(orders_master[time_slot]),
        [Cancellation Rate %],
        DESC
    )
)

Weekend Cancel Rate = 
CALCULATE([Cancellation Rate %], orders_master[day_type] = "Weekend")

Weekday Cancel Rate = 
CALCULATE([Cancellation Rate %], orders_master[day_type] = "Weekday")

Insight 1 = 
"⚡ Operations Summary:" & UNICHAR(10) &
"Fulfillment: " & FORMAT([Fulfillment Rate %], "0.00%") & " (Target: 98%)" & UNICHAR(10) &
"Cancellation: " & FORMAT([Cancellation Rate %], "0.00%") & " (Target: 3%)"

Insight 2 = 
"🕐 Peak Performance:" & UNICHAR(10) &
"Peak Hour: " & [Peak Hour] & ":00 (" & FORMAT([Peak Hour Load %], "0%") & " of orders)" & UNICHAR(10) &
"Best Slot: " & [Best Time Slot] & UNICHAR(10) &
"Worst Slot: " & [Worst Time Slot]

Insight 3 = 
"💰 Financial Impact:" & UNICHAR(10) &
"Lost Revenue: ₹" & FORMAT([Cancellation Loss Amount] / 10000000, "0.0") & " Cr" & UNICHAR(10) &
"If reduced to 3%: Save ₹" & 
FORMAT(([Cancellation Rate %] - 3) / 100 * [Total Revenue] / 10000000, "0.0") & " Cr"

Insight 4 = 
"🎯 Quick Wins:" & UNICHAR(10) &
IF([Cancellation Rate %] > 5, "1️⃣ Reduce cancellations urgently" & UNICHAR(10), "") &
IF([Weekend Cancel Rate] > [Weekday Cancel Rate], "2️⃣ Focus on weekend operations" & UNICHAR(10), "") &
"3️⃣ Allocate 60% more fleet during " & [Peak Hour] & ":00"
```

### Columns (orders_master)
```
Order Hour = HOUR(orders_master[delivery_time])

Day Name = 
SWITCH(
    orders_master[day_of_week],
    0, "Mon",
    1, "Tue",
    2, "Wed",
    3, "Thu",
    4, "Fri",
    5, "Sat",
    6, "Sun"
)
```

### Slicers (Filters)
**1.** Date Range Slicer
**2.** Time Slot Slicer
**3.** Day Name Slicer

---

# 🎯 DASHBOARD 7: MARKET EXPANSION

### CITY DEMOGRAPHICS TABLE
```
City Demographics = 
DATATABLE(
    "city", STRING,
    "population", INTEGER,
    "urbanization_rate", DOUBLE,
    "avg_income", INTEGER,
    {
        {"Mumbai", 21673000, 0.88, 115000},
        {"Delhi", 33807000, 0.91, 108000},
        {"Bangalore", 14354000, 0.94, 145000},
        {"Hyderabad", 11067000, 0.85, 98000},
        {"Chennai", 12324000, 0.84, 92000},
        {"Kolkata", 15644000, 0.77, 78000},
        {"Pune", 7425000, 0.89, 122000},
        {"Ahmedabad", 8940000, 0.81, 85000},
        {"Jaipur", 4325000, 0.75, 72000},
        {"Lucknow", 4120000, 0.72, 65000}
    }
)
```

### MARKET EXPANSION MEASURES

```DAX
Total Markets = 
DISTINCTCOUNT(orders_master[city])

City Orders = 
CALCULATE(
    COUNTROWS(orders_master),
    ALLEXCEPT(orders_master, orders_master[city])
)

City Population = 
Sum('City Demographics'[population])

Saturation Index = 
VAR CityOrders = [City Orders]
VAR Population = [City Population]
RETURN
DIVIDE(CityOrders, Population, 0) * 1000

Saturated Cities = 
CALCULATE(
    DISTINCTCOUNT(orders_master[city]),
    FILTER(
        VALUES('City Demographics'[city]),
        [Saturation Index] >= 50
    )
)

Saturated Markets Display = 
var SatMark = [Saturated Cities] + 0 
RETURN
SatMark

High Potential Cities = 
CALCULATE(
    DISTINCTCOUNT(orders_master[city]),
    FILTER(
        VALUES('City Demographics'[city]),
        [Saturation Index] < 50
    )
)

High Potential Display = 
var HighPote = [High Potential Cities] + 0
RETURN
HighPote

Est Total Market Orders = 
VAR Population = SUM('City Demographics'[population])
VAR OrderingRate = 0.15   
VAR MinDate = MIN(orders_master[order_date])
VAR MaxDate = MAX(orders_master[order_date])
VAR AvgOrdersPerYear = 
    SWITCH( TRUE(),
        SELECTEDVALUE('City Demographics'[city]) = "Bangalore", 80,
        SELECTEDVALUE('City Demographics'[city]) = "Delhi", 72,
        SELECTEDVALUE('City Demographics'[city]) = "Mumbai", 65,
        36
    )
VAR YearsInData = 
    IF(
        ISBLANK(MinDate) || ISBLANK(MaxDate), 
        1, 
        (DATEDIFF(MinDate, MaxDate, MONTH) / 12) + 1
    )
RETURN
Population * OrderingRate * AvgOrdersPerYear * YearsInData

Market Penetration % = 
DIVIDE([City Orders], [Est Total Market Orders], 0)

Average Penetration = 
AVERAGEX(
    VALUES('City Demographics'[city]),
    [Market Penetration %]
)

Market Size Score = 
VAR Population = SUM('City Demographics'[population])
VAR Income = SELECTEDVALUE('City Demographics'[avg_income], 65000)
VAR Urbanization = SELECTEDVALUE('City Demographics'[urbanization_rate], 0.70)
VAR MaxPopulation = 35000000 
VAR MaxIncome = 150000       
VAR NormalizedPopulation = DIVIDE(Population, MaxPopulation, 1) * 100
VAR NormalizedIncome = DIVIDE(Income, MaxIncome, 1) * 100
VAR UrbanizationScore = Urbanization * 100
RETURN
(NormalizedPopulation * 0.5) + (NormalizedIncome * 0.3) + (UrbanizationScore * 0.2)

Growth Potential Score = 
VAR GrowthRate = [Orders Growth %]
RETURN
SWITCH(
    TRUE(),
    GrowthRate >= 30, 100,  // Exceptional growth
    GrowthRate >= 20, 80,   // High growth
    GrowthRate >= 10, 60,   // Good growth
    GrowthRate >= 5, 40,    // Moderate growth
    20                      // Low/negative growth
)

Unsaturation Score = 
VAR SaturationLevel = [Saturation Index]
VAR NormalizedSaturation = DIVIDE(SaturationLevel, 100, 0) * 100
RETURN
100 - NormalizedSaturation

Expansion Priority Score = 
VAR MarketSize = [Market Size Score]
VAR GrowthPotential = [Growth Potential Score]
VAR Unsaturation = [Unsaturation Score]
RETURN
(MarketSize * 0.4) + (GrowthPotential * 0.3) + (Unsaturation * 0.3)

Population Display = [City Population] / 10000000

Priority Rank = 
RANKX(
    ALL('City Demographics'[city]),
    [Expansion Priority Score],
    ,
    DESC,
    DENSE
)
```

### Strategic Recommendations (Text Box)
```
🎯 #1 PRIORITY: Delhi (Score: 65.91)
  • Saturation: 17.75 (Low) High Growth Potential   • Penetration: 0.0334% (Room to Grow) 
 ✓ ACTION: Launch aggressive marketing campaign
 ✓ ACTION: Add 50% more restaurant partners
 ✓ EXPECTED: 3× order growth in 12 months


⭐ #2 PRIORITY: Mumbai (Score: 56.32)
 ✓ ACTION: Focus on premium restaurant partnerships
 ✓ ACTION: Launch city-specific cuisine campaigns
 ✓ EXPECTED: 2× Growth in 18 months


 ⚠️ SATURATED MARKETS (Mumbai, Delhi, Kolkata):
 ✓ ACTION: Focus on retention, not acquisition
 ✓ ACTION: Improve customer experience to defend market share
 ✓ ACTION: Launch premium services (Swiggy, Genie, Instamart)
 ✓ AVOID: Over-investing in customer acquisition


 💰 RECOMMENDED BUDGET ALLOCATION (₹10 Cr Annual):
 • Top 3 Priority Cities: ₹6 Cr (60%)
 • Other High-Potential Markets: ₹3 Cr (30%)
 • Saturated Markets: ₹1 Cr (10% - Retention only)
 → ROI Expected: 3-5× in top priority cities


 🌍 NEW CITY EXPANSION CRITERIA:
 ✓ Population: >2M (Tier 2+ cities)
 ✓ Urbanization Rate: >70%
 ✓ Average Income: >₹50K/year
💡 RECOMMENDED CANDIDATES: Surat, Indore, Chandigarh, Kochi, Vadodara
```


### Columns (City Demographics)
```
Saturation Category = 
VAR Saturation = [Saturation Index]
RETURN
SWITCH(
    TRUE(),
    Saturation >= 80, "High Saturation",
    Saturation >= 50, "Medium Saturation",
    "Low Saturation"
)
```

### Slicers (Filters)
**1.** Date Range Slicer
**2.** City Slicer
**3.** Saturation Category Slicer

---

# CompanySearchCriteria

The company-side filter blob, one field per ``CompanySearchFilters`` key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_name** | **str** | Company name match. | [optional] [default to '']
**company_name_match_type** | **str** | How company_name matches: contains (substring), exact, or similar (word-order-free fuzzy). | [optional] [default to 'contains']
**domain** | **str** | Company website domain; a pasted URL is reduced to its host. | [optional] [default to '']
**industries_include** | **List[str]** | LinkedIn industries or industry group names to include. | [optional] 
**headcount_ranges** | **List[str]** | Headcount buckets to include (1-10 through 10001+), OR-ed. | [optional] 
**revenue_min** | **str** | Minimum estimated annual revenue in USD. | [optional] [default to '']
**revenue_max** | **str** | Maximum estimated annual revenue in USD. | [optional] [default to '']
**year_founded_min** | **str** | Earliest founding year, inclusive. | [optional] [default to '']
**year_founded_max** | **str** | Latest founding year, inclusive. | [optional] [default to '']
**company_type** | **List[str]** | Canonical LinkedIn company types to include. | [optional] 
**funding_round_types** | **List[str]** | Last funding round labels to include, such as &#39;Series B&#39;. | [optional] 
**funding_amount_min** | **str** | Total disclosed investment must exceed this USD amount. | [optional] [default to '']
**growth_min** | **str** | Six-month employee growth percent must exceed this value. | [optional] [default to '']
**growth_max** | **str** | Six-month employee growth percent must be below this value. | [optional] [default to '']
**industries_exclude** | **List[str]** | LinkedIn industries or industry group names to exclude. | [optional] 
**headcount_ranges_exclude** | **List[str]** | Headcount buckets to exclude. | [optional] 
**company_type_exclude** | **List[str]** | Canonical LinkedIn company types to exclude. | [optional] 
**hq_countries_iso3** | **List[str]** | HQ countries as ISO-3 codes, country names or group names. | [optional] 
**hq_countries_iso3_exclude** | **List[str]** | HQ countries to exclude, same forms as hq_countries_iso3. | [optional] 
**largest_headcount_countries_iso3** | **List[str]** | Countries holding most employees, same forms as hq_countries_iso3. | [optional] 
**hq_states** | **List[str]** | HQ state substrings such as &#39;Texas, United States&#39;, OR-ed. | [optional] 
**hq_states_exclude** | **List[str]** | HQ state substrings to exclude. | [optional] 
**hq_cities** | **List[str]** | HQ city substrings such as &#39;Austin, Texas, United States&#39;, OR-ed. | [optional] 
**hq_cities_exclude** | **List[str]** | HQ city substrings to exclude. | [optional] 
**linkedin_categories_include** | **List[str]** | LinkedIn category tags to include. | [optional] 
**crunchbase_categories_include** | **List[str]** | Crunchbase categories to include. | [optional] 
**crunchbase_categories_exclude** | **List[str]** | Crunchbase categories to exclude. | [optional] 
**stock_listings** | **List[str]** | Stock exchange listings; PRIVATE selects unlisted companies. | [optional] 
**headcount_latest_min** | **str** | Minimum tracked employee count; overrides headcount buckets. | [optional] [default to '']
**headcount_latest_max** | **str** | Maximum tracked employee count; overrides headcount buckets. | [optional] [default to '']
**growth1m_min** | **str** | Minimum one-month employee growth percent. | [optional] [default to '']
**growth3m_min** | **str** | Minimum three-month employee growth percent. | [optional] [default to '']
**growth12m_min** | **str** | Minimum twelve-month employee growth percent. | [optional] [default to '']
**followers_min** | **str** | Minimum LinkedIn follower count. | [optional] [default to '']
**followers_growth6m_min** | **str** | Minimum six-month follower growth percent. | [optional] [default to '']
**followers_growth12m_min** | **str** | Minimum twelve-month follower growth percent. | [optional] [default to '']
**last_funding_date_after** | **str** | Last funding date floor as YYYY-MM-DD. | [optional] [default to '']
**ipo_date_after** | **str** | IPO date floor as YYYY-MM-DD. | [optional] [default to '']
**last_funding_round_amount_min** | **str** | Minimum size of the last funding round in USD. | [optional] [default to '']
**last_funding_round_amount_max** | **str** | Maximum size of the last funding round in USD. | [optional] [default to '']
**valuation_min** | **str** | Minimum Crunchbase valuation in USD. | [optional] [default to '']
**valuation_max** | **str** | Maximum Crunchbase valuation in USD. | [optional] [default to '']
**bootstrapped_only** | **bool** | Only companies with no disclosed investment. | [optional] [default to False]
**acquired_only** | **bool** | Only acquired companies. | [optional] [default to False]
**funding_round_types_exclude** | **List[str]** | Last funding round labels to exclude. | [optional] 
**investors_include** | **List[str]** | Crunchbase investors to include. | [optional] 
**investors_exclude** | **List[str]** | Crunchbase investors to exclude. | [optional] 
**stock_symbols** | **List[str]** | Stock ticker symbols to include. | [optional] 
**domains_list** | **List[str]** | Exact company domains to match; URLs are reduced to hosts. | [optional] 
**company_names_list** | **List[str]** | Exact, case-sensitive company names to match. | [optional] 
**twitter_handle** | **str** | Exact Twitter handle; a leading @ is kept. | [optional] [default to '']
**description_keyword** | **str** | Keyword matched against the LinkedIn company description. | [optional] [default to '']
**updated_after** | **str** | Crustdata updated_at floor, sent verbatim. | [optional] [default to '']
**composite_mode** | **bool** | UI-only flag from the composite section; never compiled. | [optional] [default to False]
**workforce_rules** | [**List[WorkforceRule]**](WorkforceRule.md) | AND-combined role rules: percent, growth_6m or growth_yoy, with &gt;&#x3D; or &lt;&#x3D; and a finite threshold. Growth thresholds may be negative. | [optional] 
**exclude_company_domains** | **List[str]** | Company domains to exclude; resolved by the exclusions step. | [optional] 
**exclude_in_cleanlist** | **str** | Skip companies already on the user&#39;s lists: off, any list they can open, or specific lists. | [optional] [default to 'off']
**exclude_in_cleanlist_list_ids** | **List[str]** | Lead list ids the list scope resolves against. | [optional] 
**crm_filter_sections** | [**CrmFilterSections**](CrmFilterSections.md) | Per-CRM exclude clauses resolved by the exclusions step; conditions that exclude accounts only. | [optional] 

## Example

```python
from cleanlist_ai.models.company_search_criteria import CompanySearchCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of CompanySearchCriteria from a JSON string
company_search_criteria_instance = CompanySearchCriteria.from_json(json)
# print the JSON string representation of the object
print(CompanySearchCriteria.to_json())

# convert the object into a dict
company_search_criteria_dict = company_search_criteria_instance.to_dict()
# create an instance of CompanySearchCriteria from a dict
company_search_criteria_from_dict = CompanySearchCriteria.from_dict(company_search_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



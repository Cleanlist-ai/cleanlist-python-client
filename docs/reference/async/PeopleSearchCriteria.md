# PeopleSearchCriteria

``SearchFilters``: the People Finder's filter blob, one field per control.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**industries_include** | **List[str]** | Current employer industries to include: LinkedIn industry names or industry group tokens, which expand to their member industries. | [optional] 
**industries_exclude** | **List[str]** | Current employer industries to exclude: LinkedIn industry names or industry group tokens. | [optional] 
**company_sizes** | **List[str]** | Current employer headcount buckets, e.g. 51-200 or 501-1,000. | [optional] 
**seniority** | **List[str]** | Current seniority levels, e.g. Director or Vice President. | [optional] 
**job_titles_include** | **List[str]** | Current job titles to match; abbreviations expand to synonyms unless the match type is exact. | [optional] 
**job_titles_exclude** | **List[str]** | Current job titles to exclude, matched exactly. | [optional] 
**job_title_match_type** | **str** | How job titles match: contains (substring), exact, or similar. | [optional] [default to 'contains']
**years_of_experience** | **str** | Total experience bucket: 0-1, 1-2, 3-5, 6-10 or 10+. | [optional] [default to '']
**contact_countries** | **List[str]** | Person countries to include: iso3 codes, country names or group tokens such as EMEA. | [optional] 
**contact_countries_exclude** | **List[str]** | Person countries to exclude, in any spelling the include accepts. | [optional] 
**contact_regions** | **List[str]** | Person states or regions to include, e.g. \&quot;Texas, United States\&quot;. | [optional] 
**contact_regions_exclude** | **List[str]** | Person states or regions to exclude. | [optional] 
**contact_cities** | **List[str]** | Person cities to include, e.g. \&quot;Austin, Texas, United States\&quot;. | [optional] 
**contact_cities_exclude** | **List[str]** | Person cities to exclude. | [optional] 
**company_countries** | **List[str]** | Current employer HQ countries to include. | [optional] 
**company_countries_exclude** | **List[str]** | Current employer HQ countries to exclude. | [optional] 
**company_regions** | **List[str]** | Current employer HQ states or regions to include. | [optional] 
**company_regions_exclude** | **List[str]** | Current employer HQ states or regions to exclude. | [optional] 
**company_cities** | **List[str]** | Current employer HQ cities to include. | [optional] 
**company_cities_exclude** | **List[str]** | Current employer HQ cities to exclude. | [optional] 
**skills** | **List[str]** | Skills listed on the profile, substring matched. | [optional] 
**connections_min** | **str** | Minimum number of LinkedIn connections. | [optional] [default to '']
**connections_max** | **str** | Maximum number of LinkedIn connections. | [optional] [default to '']
**degree_types** | **List[str]** | Degree types, e.g. MBA or PhD. | [optional] 
**school_names** | **List[str]** | Institution names, matched exactly. | [optional] 
**fields_of_study** | **List[str]** | Fields of study, matched exactly. | [optional] 
**certification_keywords** | **List[str]** | Certification names, matched exactly. | [optional] 
**company_name_filter** | **str** | One current employer name, ANDed. | [optional] [default to '']
**company_name_match_type** | **str** | How employer NAMES match — governs both company_name_filter and current_company_names: contains (substring), exact, or similar. Domains and LinkedIn URLs are always exact. | [optional] [default to 'contains']
**first_name** | **str** | First name, exact. | [optional] [default to '']
**last_name** | **str** | Last name, exact. | [optional] [default to '']
**linkedin_urls** | **List[str]** | Person LinkedIn vanity URLs; any of them matches. | [optional] 
**past_companies** | **List[str]** | Past employer names, substring matched. | [optional] 
**past_titles** | **List[str]** | Past job titles, substring matched. | [optional] 
**years_at_company** | **str** | Years in the current role bucket: 0-1, 1-2, 2-5, 5-10 or 10+. | [optional] [default to '']
**recently_changed_jobs** | **bool** | Only people who changed jobs recently. | [optional] [default to False]
**current_company_linked_in_urls** | **List[str]** | Current employer LinkedIn company URLs; ORed with domains and names. | [optional] 
**current_company_domains** | **List[str]** | Current employer website domains; ORed with URLs and names. | [optional] 
**current_company_names** | **List[str]** | Current employer names; ORed with URLs and domains. | [optional] 
**past_company_linked_in_urls** | **List[str]** | Past employer LinkedIn company URLs. | [optional] 
**function_categories_include** | **List[str]** | Current job functions, e.g. Engineering or Sales. | [optional] 
**past_function_categories_include** | **List[str]** | Past job functions. | [optional] 
**past_seniority** | **List[str]** | Past seniority levels. | [optional] 
**past_companies_require_all** | **bool** | When true, every past company and past company URL must appear in the person&#39;s history instead of any one of them. | [optional] [default to False]
**never_worked_at_companies** | **List[str]** | LinkedIn company URLs the person must never have worked at; unsupported values are rejected. | [optional] 
**never_held_titles** | **List[str]** | Titles the person must never have held, matched exactly. | [optional] 
**followers_min** | **str** | Minimum number of followers. | [optional] [default to '']
**followers_max** | **str** | Maximum number of followers. | [optional] [default to '']
**languages** | **List[str]** | Languages listed on the profile, substring matched. | [optional] 
**open_to_cards** | **List[str]** | LinkedIn open-to cards: CAREER_INTEREST, HIRING_MANAGER, VOLUNTEERING. | [optional] 
**profile_updated_after** | **str** | Profile last updated on or after this YYYY-MM-DD date. | [optional] [default to '']
**headline_contains** | **str** | Substring the profile headline must contain. | [optional] [default to '']
**summary_contains** | **str** | Substring the profile summary must contain. | [optional] [default to '']
**twitter_handle** | **str** | Twitter handle, exact; a leading @ is stripped. | [optional] [default to '']
**title_boolean_query** | **str** | Boolean expression over the current title using AND, OR, parentheses and quoted phrases. | [optional] [default to '']
**keywords_boolean_query** | **str** | Boolean expression matched against the headline or summary. | [optional] [default to '']
**joined_current_after** | **str** | Started the current role on or after this YYYY-MM-DD date. | [optional] [default to '']
**past_left_company_after** | **str** | Left a past company on or after this YYYY-MM-DD date. | [optional] [default to '']
**exclude_profile_urls** | **List[str]** | Person LinkedIn URLs to exclude; resolved by the exclusions step. | [optional] 
**exclude_company_domains** | **List[str]** | Current employer domains to exclude; resolved by the exclusions step. | [optional] 
**exclude_crm_customers** | **bool** | Exclude current CRM customers (legacy flat CRM toggle). | [optional] [default to False]
**exclude_crm_active_opportunities** | **bool** | Exclude CRM accounts with active opportunities (legacy toggle). | [optional] [default to False]
**exclude_crm_owned_by_me** | **bool** | Exclude CRM records owned by the caller (legacy toggle). | [optional] [default to False]
**exclude_crm_owned_by_others** | **bool** | Exclude CRM records owned by other users (legacy toggle). | [optional] [default to False]
**exclude_crm_owner** | **str** | CRM user id whose owned records are excluded (legacy field). | [optional] [default to '']
**exclude_crm_account_status** | **str** | CRM account status value to exclude (legacy field). | [optional] [default to '']
**crm_filter_sections** | [**CrmFilterSections**](CrmFilterSections.md) | Per-CRM include/exclude clauses resolved by the exclusions step. | [optional] 
**exclude_in_cleanlist** | **str** | Cleanlist dedupe scope: off, any list in the org, or specific lists. | [optional] [default to 'off']
**exclude_in_cleanlist_list_ids** | **List[str]** | Lead list ids the list scope resolves against. | [optional] 
**company_filter_composite_mode** | **bool** | Routing override that targets the company-first composite search. | [optional] [default to False]
**geo_radius** | [**GeoRadius**](GeoRadius.md) |  | [optional] 
**max_results** | **int** | Portal result cap. In the public API, explicitly setting this applies a per-response ceiling of 1-500 rows, combined with limit using the smaller value. The default is non-binding; continuation pages are separate. Not a provider filter. | [optional] [default to 100]
**limit_per_company** | **str** | Portal client-side company cap. In the public API, 1-100 caps each returned page by its selected matching company; unknown-company rows are omitted with a warning. Continuation pages may return more from that company. Empty means unset. | [optional] [default to '']

## Example

```python
from cleanlist_ai.aio.models.people_search_criteria import PeopleSearchCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of PeopleSearchCriteria from a JSON string
people_search_criteria_instance = PeopleSearchCriteria.from_json(json)
# print the JSON string representation of the object
print(PeopleSearchCriteria.to_json())

# convert the object into a dict
people_search_criteria_dict = people_search_criteria_instance.to_dict()
# create an instance of PeopleSearchCriteria from a dict
people_search_criteria_from_dict = PeopleSearchCriteria.from_dict(people_search_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



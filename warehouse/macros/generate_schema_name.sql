{# Use the custom schema exactly as written (e.g. canary_staging). dbt's default would
   glue it onto the target schema and give canary_staging_canary_marts. #}
{% macro generate_schema_name(custom_schema_name, node) -%}
    {%- if custom_schema_name is none -%}
        {{ target.schema }}
    {%- else -%}
        {{ custom_schema_name | trim }}
    {%- endif -%}
{%- endmacro %}

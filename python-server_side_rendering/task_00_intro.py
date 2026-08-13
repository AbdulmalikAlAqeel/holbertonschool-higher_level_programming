#!/usr/bin/python3
"""
Task 00: Simple Templating Program
"""
import os


def generate_invitations(template, attendees):
    """
    Generates invitation files from a template and a list of attendees.
    """
    # 1. Check Input Types
    if not isinstance(template, str):
        print(f"Error: Invalid template input type, expected str, got {type(template).__name__}.")
        return

    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print(f"Error: Invalid attendees input type, expected list of dicts, got {type(attendees).__name__}.")
        return

    # 2. Handle Empty Template
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # 3. Handle Empty List
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # 4. Process Each Attendee
    for index, attendee in enumerate(attendees, start=1):
        # Clean missing or None values with "N/A"
        name = attendee.get("name")
        name = name if name is not None else "N/A"

        event_title = attendee.get("event_title")
        event_title = event_title if event_title is not None else "N/A"

        event_date = attendee.get("event_date")
        event_date = event_date if event_date is not None else "N/A"

        event_location = attendee.get("event_location")
        event_location = event_location if event_location is not None else "N/A"

        # Format template with processed data
        output_content = template.format(
            name=name,
            event_title=event_title,
            event_date=event_date,
            event_location=event_location
        )

        # File name convention: output_1.txt, output_2.txt...
        output_filename = f"output_{index}.txt"

        # Write content to file
        try:
            with open(output_filename, 'w', encoding='utf-8') as f:
                f.write(output_content)
        except Exception as e:
            print(f"Error writing to {output_filename}: {e}")

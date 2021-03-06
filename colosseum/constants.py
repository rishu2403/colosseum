from . import parser
from . import units


class Choices:
    "A class to define allowable data types for a property"
    def __init__(
            self, *constants, length=False, percentage=False,
            integer=False, number=False, color=False,
            explicit_defaulting_constants=None):
        self.constants = set(constants)
        self.explicit_defaulting_constants = explicit_defaulting_constants or []
        self.length = length
        self.percentage = percentage
        self.integer = integer
        self.number = number
        self.color = color

    def validate(self, value):
        if self.length or self.percentage:
            try:
                val = parser.units(value)
                if self.length:
                    return val
                elif self.percentage and isinstance(val, units.Percent):
                    return val
            except ValueError:
                pass
        if self.integer:
            try:
                return int(value)
            except (ValueError, TypeError):
                pass
        if self.number:
            try:
                return float(value)
            except (ValueError, TypeError):
                pass
        if self.color:
            try:
                return parser.color(value)
            except ValueError:
                pass
        if value == 'none':
            value = None
        for const in self.constants:
            if value == const:
                return const
        for const in self.explicit_defaulting_constants:
            if value == const:
                return const

        raise ValueError()

    def __str__(self):
        choices = [str(c).lower().replace('_', '-') for c in self.constants]
        if self.length:
            choices.append("<length>")
        if self.percentage:
            choices.append("<percentage>")
        if self.integer:
            choices.append("<integer>")
        if self.number:
            choices.append("<number>")
        if self.color:
            choices.append("<color>")
        if self.explicit_defaulting_constants:
            for item in self.explicit_defaulting_constants:
                choices.append(item)
        return ", ".join(sorted(choices))


######################################################################
# Versions of the HTML standard
######################################################################
HTML4 = 'html4'
HTML5 = 'html5'

######################################################################
# Common constants
######################################################################

AUTO = 'auto'
COLUMN = 'column'
ROW = 'row'
TRANSPARENT = 'transparent'
default = object()

######################################################################
# Explicit defaulting constants
######################################################################

INITIAL = 'initial'
INHERIT = 'inherit'
UNSET = 'unset'
REVERT = 'revert'

######################################################################
# Margins
# 8.3 Margin properties
######################################################################

MARGIN_CHOICES = Choices(AUTO, length=True, percentage=True)

######################################################################
# 8.4 Padding properties
######################################################################

PADDING_CHOICES = Choices(length=True, percentage=True)

######################################################################
# 8.5 Border properties
######################################################################

THIN = 'thin'
MEDIUM = 'medium'
THICK = 'thick'

BORDER_WIDTH_CHOICES = Choices(THIN, MEDIUM, THICK, length=True)

HIDDEN = 'hidden'
DOTTED = 'dotted'
DASHED = 'dashed'
SOLID = 'solid'
DOUBLE = 'double'
GROOVE = 'groove'
RIDGE = 'ridge'
INSET = 'inset'
OUTSET = 'outset'

BORDER_STYLE_CHOICES = Choices(
    None,
    HIDDEN,
    DOTTED,
    DASHED,
    SOLID,
    DOUBLE,
    GROOVE,
    RIDGE,
    INSET,
    OUTSET,
)

BORDER_COLOR_CHOICES = Choices(TRANSPARENT, color=True,
                               explicit_defaulting_constants=[INITIAL, INHERIT, UNSET, REVERT])

######################################################################
# 9.2.4 The display property
######################################################################

INLINE = 'inline'
BLOCK = 'block'
LIST_ITEM = 'list-item'
INLINE_BLOCK = 'inline-block'
TABLE = 'table'
INLINE_TABLE = 'inline-table'
TABLE_ROW_GROUP = 'table-row-group'
TABLE_HEADER_GROUP = 'table-header-group'
TABLE_FOOTER_GROUP = 'table-footer-group'
TABLE_ROW = 'table-row'
TABLE_COLUMN_GROUP = 'table-column-group'
TABLE_COLUMN = 'table-column'
TABLE_CELL = 'table-cell'
TABLE_CAPTION = 'table-caption'

# CSS Flexbox
FLEX = 'flex'
INLINE_FLEX = 'inline-flex'

# CSS Grid
GRID = 'grid'
INLINE_GRID = 'inline-grid'

DISPLAY_CHOICES = Choices(
    None,
    INLINE,
    BLOCK,
    LIST_ITEM,
    INLINE_BLOCK,
    TABLE,
    INLINE_TABLE,
    TABLE_ROW_GROUP,
    TABLE_HEADER_GROUP,
    TABLE_FOOTER_GROUP,
    TABLE_ROW,
    TABLE_COLUMN_GROUP,
    TABLE_COLUMN,
    TABLE_CELL,
    TABLE_CAPTION,

    FLEX,
    INLINE_FLEX,

    GRID,
    INLINE_GRID,
)

######################################################################
# 9.3 Positioning schemes
# 9.3.2 Box offsets
######################################################################

STATIC = 'static'
RELATIVE = 'relative'
ABSOLUTE = 'absolute'
FIXED = 'fixed'

POSITION_CHOICES = Choices(STATIC, RELATIVE, ABSOLUTE, FIXED)

BOX_OFFSET_CHOICES = Choices(AUTO, length=True, percentage=True)

######################################################################
# 9.5.1 Positioning the float
# 9.5.2 Controlling flow next to floats
######################################################################

LEFT = 'left'
RIGHT = 'right'
BOTH = 'both'

FLOAT_CHOICES = Choices(LEFT, RIGHT, None)
CLEAR_CHOICES = Choices(None, LEFT, RIGHT, BOTH)

######################################################################
# 9.9 Layered Presentation
######################################################################

Z_INDEX_CHOICES = Choices(AUTO, integer=True)

######################################################################
# 9.10 Text Direction
######################################################################

RTL = 'rtl'
LTR = 'ltr'

DIRECTION_CHOICES = Choices(RTL, LTR)

NORMAL = 'normal'
EMBED = 'embed'
BIDI_OVERRIDE = 'bidi-override'

UNICODE_BIDI_CHOICES = Choices(NORMAL, EMBED, BIDI_OVERRIDE)

######################################################################
# 10.4 Minimum and maximum width
# 10.5 Content height
# 10.7 Minimum and maximum heights
######################################################################

SIZE_CHOICES = Choices(AUTO, length=True, percentage=True)
MIN_SIZE_CHOICES = Choices(AUTO, length=True, percentage=True)
MAX_SIZE_CHOICES = Choices(None, length=True, percentage=True)

######################################################################
# 10.8 Leading and half-leading
######################################################################
# line_height
# vertical_align

######################################################################
# 11.1.1 Overflow
######################################################################
# overflow

######################################################################
# 11.1.2 Clip
######################################################################
# clip

######################################################################
# 11.2 Visibility
######################################################################

VISIBLE = 'visible'
HIDDEN = 'hidden'
COLLAPSE = 'collapse'

VISIBILITY_CHOICES = Choices(VISIBLE, HIDDEN, COLLAPSE)

######################################################################
# 12.2 The content property
######################################################################
# content

######################################################################
# 12.3 Quotation marks
######################################################################
# quotes

######################################################################
# 12.4 Automatic counters and numbering
######################################################################
# counter-reset
# counter-increment

######################################################################
# 12.5 Lists
######################################################################
# list_style_type
# list_style_image
# list_style_position
# list_style

# 13. Paged media ####################################################
######################################################################
# 13.3.1 Page break properties
######################################################################
# page_break_before
# page_break_after
# page_break_inside

######################################################################
# 13.3.2 Breaks inside elements
######################################################################
# orphans
# widows

######################################################################
# 14.1 Foreground color
######################################################################
COLOR_CHOICES = Choices(default, color=True)

######################################################################
# 14.2.1 Background properties
######################################################################
BACKGROUND_COLOR_CHOICES = Choices(default, TRANSPARENT, color=True)

# background_image
# background_repeat
# background_attachment
# background_position
# background

######################################################################
# 15. Fonts
# 15.3 Font family
######################################################################
# font_family

######################################################################
# 15.4 Font Styling
######################################################################
# font_style

######################################################################
# 15.5 Small-caps
######################################################################
# font_variant

######################################################################
# 15.6 Font boldness
######################################################################
# font_weight

######################################################################
# 15.7 Font size
######################################################################
# font_size

######################################################################
# 16. Text ###########################################################
######################################################################
# 16.1 Indentation
######################################################################
# text_indent

######################################################################
# 16.2 Alignment
######################################################################
# text_align

######################################################################
# 16.3 Decoration
######################################################################
# text_decoration

######################################################################
# 16.4 Letter and word spacing
######################################################################
# letter_spacing
# word_spacing

######################################################################
# 16.5 Capitalization
######################################################################
# text_transform

######################################################################
# 16.6 White space
######################################################################
# white_space

######################################################################
# 17. Tables
######################################################################
# 17.4.1 Caption position and alignment
######################################################################
# caption_side

######################################################################
# 17.5.2 Table width algorithms
######################################################################
# table_layout

######################################################################
# 17.6 Borders
######################################################################
# border_collapse
# border_spacing
# empty_cells

######################################################################
# 18. User interface #################################################
######################################################################
# 18.1 Cursors
# cursor

######################################################################
# 18.4 Dynamic outlines
######################################################################
# outline_width
# outline_style
# outline_color
# outline

######################################################################
# Flex flow (CSS-flexbox-1, Section 5)
######################################################################

ROW_REVERSE = 'row-reverse'
COLUMN_REVERSE = 'column-reverse'

FLEX_DIRECTION_CHOICES = Choices(ROW, ROW_REVERSE, COLUMN, COLUMN_REVERSE)

NOWRAP = 'no-wrap'
WRAP = 'wrap'
WRAP_REVERSE = 'wrap-reverse'

FLEX_WRAP_CHOICES = Choices(NOWRAP, WRAP, WRAP_REVERSE)

ORDER_CHOICES = Choices(integer=True)

######################################################################
# Flexibility (CSS-flexbox-1, Section 7)
######################################################################

FLEX_GROW_CHOICES = Choices(number=True)
FLEX_SHRINK_CHOICES = Choices(number=True)

CONTENT = 'content'

FLEX_BASIS_CHOICES = Choices(CONTENT, AUTO, length=True, percentage=True)

######################################################################
# Flex Alignment (CSS-flexbox-1, Section 8)
######################################################################

FLEX_START = 'flex-start'
FLEX_END = 'flex-end'
CENTER = 'center'
SPACE_BETWEEN = 'space-between'
SPACE_AROUND = 'space-around'

JUSTIFY_CONTENT_CHOICES = Choices(FLEX_START, FLEX_END, CENTER, SPACE_BETWEEN, SPACE_AROUND)

BASELINE = 'baseline'
STRETCH = 'stretch'

ALIGN_SELF_CHOICES = Choices(AUTO, FLEX_START, FLEX_END, CENTER, BASELINE, STRETCH)
ALIGN_ITEMS_CHOICES = Choices(AUTO, FLEX_START, FLEX_END, CENTER, BASELINE, STRETCH)

ALIGN_CONTENT_CHOICES = Choices(FLEX_START, FLEX_END, CENTER, SPACE_BETWEEN, SPACE_AROUND, STRETCH)


######################################################################
# Grid template (CSS-grid-1, Section 7)
######################################################################

GRID_TEMPLATE_CHOICES = Choices(None)  # track_list=True, auto_track_list=True)

GRID_TEMPLATE_AREA_CHOICES = Choices(None)  # strings=True), initial=None

GRID_AUTO_CHOICES = Choices(AUTO)  # track_sizes=True)

DENSE = 'dense'

GRID_AUTO_FLOW_CHOICES = Choices(ROW, COLUMN, DENSE)

######################################################################
# Grid placement (CSS-grid-1, Section 8)
######################################################################

GRID_PLACEMENT_CHOICES = Choices(AUTO)  # grid_line=True)

######################################################################
# Grid alignment (CSS-grid-1, Section 10)
######################################################################

GRID_GAP_CHOICES = Choices(percentage=True)

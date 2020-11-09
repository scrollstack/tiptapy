import tiptapy


s = r"""

{
  "type": "doc",
  "content": [
    {
      "type": "code_block",
      "attrs": {
          "language": "python"
      },
      "content": [
          {
              "type": "text",
              "text": "# Python Program to find the L.C.M. of two input number\n\ndef compute_lcm(x, y):\n\n   # choose the greater number\n   if x > y:\n       greater = x\n   else:\n       greater = y\n\n   while(True):\n       if((greater % x == 0) and (greater % y == 0)):\n           lcm = greater\n           break\n       greater += 1\n\n   return lcm\n\nnum1 = 54\nnum2 = 24\n\nprint(\"The L.C.M. is\", compute_lcm(num1, num2))"
          }
      ]
    },
    {
      "type": "blockquote",
      "content": [
        {
          "type": "paragraph",
          "content": [
            {
              "type": "text",
              "text": "Readability counts."
            }
          ]
        },
        {
          "type": "paragraph",
          "content": [
            {
              "type": "text",
              "marks": [
                {
                  "type": "link",
                  "attrs": { "href": "https://en.wikipedia.org/wiki/Zen_of_Python" }
                }
              ],
              "text": "Zen of Python"
            },
            {
              "type": "text", "text": " By "
            },
            {
              "type": "text",
              "marks": [
                {
                  "type": "bold"
                }
              ],
              "text": "Tom Peters"
            }
          ]
        }
      ]
    }
  ]
}
"""

print(tiptapy.to_html(s))
